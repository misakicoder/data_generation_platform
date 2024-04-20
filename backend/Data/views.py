from django.shortcuts import render
from django.http import JsonResponse
from django.http import FileResponse
from django.views import View
from Task.models import Task
from User.models import User
from Model.models import Model
from .models import Data,ori_data_cols,Result
from util.ossUtil import ossUtil
import json
import logging
from .services import *
from Model.services import *
from datetime import datetime
import os
from util.worker import task_queue
logger = logging.getLogger(__name__)
import chardet
local_dir = "static/"
# Create your views here.
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

class data(View):
    def post(self, request):
        kwargs:dict = json.loads(request.POST.get("body")) 
        try:
            file = request.FILES.get("file")
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            data_type = kwargs.get("data_type")
            task_type = kwargs.get("task_type")
            data_description = kwargs.get("data_description")
            prefix = task_type +"/"
            befix = ".csv"
            file_name = f"{data_description}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            if not os.path.exists(local_dir + prefix):
                os.makedirs(local_dir + prefix)
            with open(local_dir + prefix + file_name + befix, "wb") as f:
                f.write(file.read())
            ori_data_url = ossUtil.upload(prefix=prefix,file_name=file_name,local_file=local_dir + prefix + file_name + befix)
            user = User.objects.get(user_id=user_id)
            now_data = Data.objects.create(
                data_type=data_type,
                data_description=data_description,
                ori_data_url=ori_data_url,
                task_type=task_type,
                user_id=user,
            )
            encoding = detect_encoding(local_dir + prefix + file_name + befix)
            print(encoding)
            ori_data = pd.read_csv(local_dir + prefix + file_name + befix)
            cols = ori_data.columns.tolist()
            cols_str = ",".join(cols)
            ori_data_cols.objects.create(
                data_id=now_data,
                cols=cols_str
            )
            os.remove(local_dir + prefix + file_name + befix)
            return JsonResponse({"status": "success", "message": "Data post successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)}) 


class ori_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            ori_datas = Data.objects.filter(user_id=user_id,task_type=task_type).values()
            return JsonResponse({"status": "success", "message": "Get ori data successful", "ori_datas": list(ori_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class data_cols(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            data_id = request.GET.get("data_id")
            data =  Data.objects.get(data_id=data_id)
            cols_str = ori_data_cols.objects.get(data_id=data).cols
            return JsonResponse({"status": "success", "message": "Get data columns successful", "data_cols": cols_str})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class cleaned_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            algorithm = request.GET.get("algorithm")
            cleaned_datas = Data.objects.filter(
                user_id=user_id,
                task_type=task_type,
                data_algorithm=algorithm
            ).exclude(cleaned_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get cleaned data successful", "cleaned_datas": list(cleaned_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})
    
    def post(self, request):
        kwargs:dict = json.loads(request.body) 
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            ori_data = kwargs.get("ori_data")
            del_cols = kwargs.get("del_cols")
            is_reverse = kwargs.get("is_reverse")
            algorithm = kwargs.get("algorithm")
            cleaned_data_url,msg = clean_data(
                ori_data_url=ori_data['ori_data_url'],
                task_type=ori_data['task_type'],
                data_description=ori_data['data_description'],
                del_cols=del_cols,
                is_reverse=is_reverse,
                algorithm=algorithm
            )


            if cleaned_data_url is None:
                return JsonResponse({"status": "error", "message": msg+"请去除掉包含字符串的列"})
            cleaned_data,created = Data.objects.get_or_create(
                ori_data_url=ori_data['ori_data_url'],
                data_algorithm=algorithm,
                defaults={
                    "data_type":ori_data['data_type'],
                    "cleaned_data_url":cleaned_data_url,
                    "task_type":ori_data['task_type'],
                    "user_id":User.objects.get(user_id=user_id),
                    "data_description":"已经清洗过的数据"+"_"+ori_data['data_description']
                }
            )
            
            if not created:
                cleaned_data.cleaned_data_url = cleaned_data_url
                cleaned_data.save()
            
            #更新列名称
            ori_data_col = ori_data_cols.objects.get(data_id=Data.objects.get(data_id=ori_data['data_id']))
            cols_str = ori_data_col.cols
            cols = cols_str.split(",")
            cols = [col for col in cols if col not in del_cols]
            cols_str = ",".join(cols)
            if created:
                ori_data_cols.objects.create(
                    data_id=cleaned_data.data_id,
                    cols=cols_str
                )
            else:
                ori_data_col.cols = cols_str
                ori_data_col.save()

            return JsonResponse({"status": "success", "message": "clean data successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})
    

class marked_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            algorithm = request.GET.get("algorithm")
            marked_datas = Data.objects.filter(
                user_id=user_id,
                task_type=task_type,
                data_algorithm=algorithm
                ).exclude(marked_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get marked data successful", "marked_datas": list(marked_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class preprocessed_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            algorithm = request.GET.get("algorithm")
            preprocessed_datas = Data.objects.filter(
                user_id=user_id,
                task_type=task_type,
                data_algorithm=algorithm
            ).exclude(preprocessed_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get preprocessed data successful", "preprocessed_datas": list(preprocessed_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})
    
    def post(self, request):
        kwargs:dict = json.loads(request.body) 
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            cleaned_or_marked_data = kwargs.get("cleaned_or_marked_data")
            if cleaned_or_marked_data['marked_data_url'] != '':
                is_mark = True
                cleaned_or_marked_url = cleaned_or_marked_data['marked_data_url']
            else:
                is_mark = False
                cleaned_or_marked_url = cleaned_or_marked_data['cleaned_data_url']
            preprocessed_url,msg = preprocess_data(
                cleaned_or_marked_url=cleaned_or_marked_url,
                task_type=cleaned_or_marked_data['task_type'],
                data_description=cleaned_or_marked_data['data_description'],
                algorithm=cleaned_or_marked_data['data_algorithm'],
                data_type=cleaned_or_marked_data['data_type']
            )
            print(f"preprocessed_url:{preprocessed_url}")
            if preprocessed_url is None:
                return JsonResponse({"status": "error", "message": "preprocess data failed" + msg})
            #更新预处理链接
            data = Data.objects.get(data_id = cleaned_or_marked_data['data_id'])
            if is_mark == False:
                data.preprocessed_data_url = preprocessed_url
            else:
                data.marked_preprocessed_data_url = preprocessed_url
            data.data_description = "预处理过的数据"+"_"+cleaned_or_marked_data['data_description']
            data.save()
            return JsonResponse({"status": "success", "message": "preprocess data successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class marked_preprocessed_data(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_type = request.GET.get("task_type")
            marked_preprocessed_datas = Data.objects.filter(user_id=user_id,task_type=task_type).exclude(marked_preprocessed_data_url='').values()
            return JsonResponse({"status": "success", "message": "Get marked preprocessed data successful", "marked_preprocessed_datas": list(marked_preprocessed_datas)})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})

class result(View):
    def get(self, request):
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_id = request.GET.get("task_id")
            task =  Task.objects.get(task_id=task_id)
            result_id = task.result_id
            if result_id == "":
                return JsonResponse({"status": "error", "message": "No result"})
            img_paths = get_img_result(result_id)
            return JsonResponse({"status": "success", "message": "Get result successful", "img_results": img_paths})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})
    
    def post(self, request):
        kwargs:dict = json.loads(request.body) 
        try:
            user_id = request.session.get("user_id")
            if user_id is None:
                return JsonResponse({"status": "error", "message": "Authentication required"}, status=401)
            task_id = kwargs.get("task_id")
            data_id = kwargs.get("data_id")
            model_id = kwargs.get("model_id")
            result_num = kwargs.get("result_num")
            data = Data.objects.get(data_id=data_id)
            model = Model.objects.get(model_id=model_id)
            task = Task.objects.get(task_id=task_id)
            task.task_state = "running"
            task.save()

            preprecessed_data_url = data.preprocessed_data_url
            model_url = model.model_url
            args = (preprecessed_data_url,model_url,data.data_type,result_num)
            task_queue.put((task_id,task.task_type,args))
            
            #存储到数据库
            return JsonResponse({"status": "success", "message": "result post successful"})
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})


class result_zip(View):
    def get(self, request):
        try:
            task_id = request.GET.get("task_id")
            result_id = Task.objects.get(task_id=task_id).result_id
            result_url = Result.objects.get(result_id=result_id).result_url
            local_zip_path = get_zip_result(result_url)
            response = FileResponse(open(local_zip_path, 'rb'))
            response['Content-Type'] = 'application/zip'
            response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(local_zip_path)
            return response
        except Exception as e:
            logger.error(f"error:{e}")
            return JsonResponse({"status": "error", "message": str(e)})