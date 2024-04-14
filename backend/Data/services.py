from util.ossUtil import ossUtil
import pandas as pd
import numpy as np
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)



local_dir = "static/"
def process_title(file_path):
  with open(file_path, 'r') as f:
    # 读取第一行，并且将其按逗号分割成列表
    first_line = f.readline().strip().split(',')

  # 创建一个空字典
  column_dict = {}

  # 遍历第一行的名称列表，并且将每个名称作为键，索引作为值存储到字典中
  for index, name in enumerate(first_line):
      column_dict[name] = index

  # 打印字典
  print(column_dict)

  return column_dict

def remove_outliers(data, threshold=10):
    # 计算每列的均值和标准差
    column_means = np.nanmean(data, axis=0)
    column_stds = np.nanstd(data, axis=0)

    # 检测异常值并设置为 NaN
    for i in range(data.shape[1]):
        z_scores = (data[:, i] - column_means[i]) / (column_stds[i] + 1e-7)
        data[abs(z_scores) >= threshold, i] = np.nan

    return data


def fill_null_with_mean(data):
    # 计算每列的平均值
    column_means = np.nanmean(data, axis=0)
    
    # 找出空值的索引
    nan_indices = np.isnan(data)
    
    # 将空值替换为每列的平均值
    data[nan_indices] = np.take(column_means, np.where(nan_indices)[1])
    
    return data

def clean_data(ori_data_url,task_type,data_description,del_cols,is_reverse,algorithm):
    #从oss下载文件
    if algorithm == "TimeGAN":
        return clean_data_in_TimeGAN(ori_data_url,task_type,data_description,del_cols,is_reverse)
    

def MinMaxScaler(data):
  """Min Max normalizer.
  
  Args:
    - data: original data
  
  Returns:
    - norm_data: normalized data
  """
  numerator = data - np.min(data, 0)
  denominator = np.max(data, 0) - np.min(data, 0)
  norm_data = numerator / (denominator + 1e-7)
  return norm_data

def clean_data_in_TimeGAN(ori_data_url,task_type,data_description,del_cols,is_reverse):
    try:
        file_path = ossUtil.download(ori_data_url)
        #读取文件
        df = pd.read_csv(file_path)
        # 将空值替换为 NaN
        df.replace('', pd.NA, inplace=True)
        #删除指定列
        df = df.drop(columns=del_cols)
        # 获取列名
        col_names = df.columns.tolist()
        # 将 DataFrame 转换为 NumPy 数组
        ori_data = df.to_numpy()
        # 将异常值设置为NaN
        ori_data = remove_outliers(ori_data)
        # 将nan值设置为平均值
        ori_data = fill_null_with_mean(ori_data)
        if is_reverse:
            ori_data = ori_data[::-1]
        # 将ori_data保存到本地
        df = pd.DataFrame(ori_data, columns=col_names)
        prefix = task_type + '/'
        befix = '.csv'
        file_name = f"{data_description}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        if not os.path.exists(local_dir + prefix):
            os.makedirs(local_dir + prefix)
        df.to_csv(local_dir + prefix + file_name + befix, index=False)
        #上传到oss
        cleaned_data_url = ossUtil.upload(prefix=prefix,file_name=file_name,local_file=local_dir + prefix + file_name + befix)
        os.remove(file_path)
        os.remove(local_dir + prefix + file_name + befix)
        return cleaned_data_url,"success"
    except Exception as e:
        logger.error(f"error:{e}")
        return None,str(e)

def preprocess_data(cleaned_or_marked_url,task_type,data_description,algorithm,data_type):
    if algorithm == "TimeGAN":
        return preprocess_data_in_TimeGAN(cleaned_or_marked_url,task_type,data_description,data_type)

def preprocess_data_in_TimeGAN(cleaned_or_marked_url,task_type,data_description,data_type):
    try:
        seq_len = 24
        file_path = ossUtil.download(cleaned_or_marked_url)
        #读取文件
        df = pd.read_csv(file_path)
        # 将 DataFrame 转换为 NumPy 数组
        cleaned_or_marked_data = df.to_numpy()
        #将数据归一化
        cleaned_or_marked_data = MinMaxScaler(cleaned_or_marked_data)
        # 预处理
        temp_data = []    
        # 截断数组
        for i in range(0, len(cleaned_or_marked_data) - seq_len):
            _x = cleaned_or_marked_data[i:i + seq_len]
            temp_data.append(_x)
        # 打乱顺序
        idx = np.random.permutation(len(temp_data))    
        data = []
        for i in range(len(temp_data)):
            data.append(temp_data[idx[i]])
        # 将data保存到本地
        prefix = task_type + '/'
        befix = '.npy'
        file_name = f"{data_description}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        if not os.path.exists(local_dir + prefix):
            os.makedirs(local_dir + prefix)
        np.save(local_dir + prefix + file_name + befix, data)
        #上传到oss
        preprocessed_data_url = ossUtil.upload(prefix=prefix,file_name=file_name,befix=".npy",local_file=local_dir + prefix + file_name + befix)
        os.remove(file_path)
        os.remove(local_dir + prefix + file_name + befix)
        return preprocessed_data_url,"success"
    except Exception as e:
        logger.error(f"error:{e}")
        return None,str(e)

