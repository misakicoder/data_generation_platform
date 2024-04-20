import torch.multiprocessing as mp
import time
import torch
import os
import django
import pandas as pd
import zipfile
import os

from .ossUtil import ossUtil,local_dir
import numpy as np
import sys
sys.path.append('D:\\data_generation_platform\\backend')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Api.settings")

# 防止 django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet. 错误
django.setup()

def train_load_generate(task_id,preprocessed_data_url,model_url,data_type,result_num):
    from Task.models import Task
    from Data.models import Result,ori_data_cols,Data
    task = Task.objects.get(task_id=task_id)
    data_path = ossUtil.download(preprocessed_data_url)
    data = np.load(data_path).tolist()
    data_id =  Data.objects.get(preprocessed_data_url=preprocessed_data_url).data_id
    cols_str = ori_data_cols.objects.get(data_id=data_id).cols
    cols = cols_str.split(",")
    # model_path = ossUtil.download(model_url)
    model_path = ""
    if task.task_algorithm == "TimeGAN":
        from Model.TimeGAN.generate import Generate_Model
        from Model.TimeGAN.lib.metrics.visualization_metrics import visualization
        model = Generate_Model(data,model_path)
        generated_data = model.generation(num_samples=len(data))
        print(generated_data)
        print(len(generated_data))
        result = Result.objects.create(
            task_id=task,
            result_url="",
        )
        img_paths =[]
        result_id = str(result.result_id)
        pca_img_path = local_dir + result_id + "_pca_img.png"
        visualization(data,generated_data,analysis='pca',img_path=pca_img_path)
        img_paths.append(pca_img_path)
        tsne_img_path = local_dir + result_id + "_tsne_img.png"
        visualization(data,generated_data,analysis='tsne',img_path=tsne_img_path)
        img_paths.append(tsne_img_path)
        csv_path = local_dir + result_id + "_result.csv"
        extract_csv(data,csv_path,cols)
        result_zip_path = zip_files(img_paths,csv_path)
        result_url = ossUtil.upload(prefix="result/",file_name=result_id+"_result",befix=".zip",local_file=result_zip_path)
        ossUtil.upload(prefix="result/",file_name=result_id+"_pca_img",befix=".png",local_file=pca_img_path)
        ossUtil.upload(prefix="result/",file_name=result_id+"_tsne_img",befix=".png",local_file=tsne_img_path)
        result.result_url = result_url
        result.save()
        task.result_id = result.result_id
        task.save()
        os.remove(pca_img_path)
        os.remove(tsne_img_path)
        os.remove(csv_path)
        os.remove(result_zip_path)
    
    #todo:删除相关文件
    os.remove(data_path)
    task.task_state = "ready"
    task.save()

def zip_files(img_paths,result_csv_path):
    result_zip_path = local_dir + "result.zip"
    with zipfile.ZipFile(result_zip_path, 'w') as z:
        for img_path in img_paths:
            z.write(img_path, arcname=os.path.basename(img_path))
        z.write(result_csv_path, arcname=os.path.basename(result_csv_path))
    return result_zip_path


def extract_csv(data,csv_path,cols):
    data = np.array(data)
    first_rows = data[:, 0, :]
    # 将数据转换为 pandas DataFrame
    df = pd.DataFrame(first_rows, columns=cols)
    # 保存为 CSV 文件
    df.to_csv(csv_path, index=False)


def worker(gpu_id, task_queue):
    print(f"worker {gpu_id} start")
   
    task_lock = mp.Lock()
    while True:
        print(f"task_queue size: {task_queue.qsize()}")
        task_id,task_type,args = task_queue.get()
        print(f"get task {task_type} {args}")
        with task_lock:
            if task_type == "load_generate":
                preprocessed_data_url,model_url,data_type,result_num = args
                train_load_generate(task_id,preprocessed_data_url,model_url,data_type,result_num)


def create_global_task_queue():
    global manager
    global task_queue
    manager = mp.Manager()
    task_queue = manager.Queue()


def worker_multiprocessing():
    mp.set_start_method("spawn", force=True)
    gpu_num = torch.cuda.device_count()

    _processes = []
    for i in range(gpu_num):
        _process = mp.Process(target=worker, args=(i, task_queue))
        _process.start()
        _processes.append(_process)