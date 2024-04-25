from torch.utils.data import Dataset, DataLoader
import pandas as pd
import numpy as np
import torch

def load_data(file_path):
    df = pd.read_csv(file_path, encoding='utf-8')
    numeric_columns = df.iloc[:, 1:].select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    return df
 
 
class MyDataset(Dataset):
    def __init__(self, data):
        #实际的样本元组
        self.data = data
 
    def __getitem__(self, item):
        return self.data[item]
 
    def __len__(self):
        return len(self.data)
     
     
def nn_seq_us(B,file_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('data processing...')
    dataset = load_data(file_path)
    # split
    train = dataset[:int(len(dataset) * 0.6)]#前60%作为线下训练集
    val = dataset[int(len(dataset) * 0.6):int(len(dataset) * 0.8)]#20%作为线下验证集
    test = dataset[int(len(dataset) * 0.8):len(dataset)]#最后剩下的20%作为测试集
    #得出线下训练集的load字段的最大值，最小值，方便后面进行归一化处理
    m, n = np.max(train[train.columns[1]]), np.min(train[train.columns[1]])
    print('max:', m, 'min:', n)
    def process(data, batch_size, shuffle):
        load = data[data.columns[1]]
        load = np.array(load.tolist())
        data = data.values.tolist()
        load = (load - n) / (m - n)#归一化操作
        seq = []
        for i in range(len(data) - 24):
            train_seq = [] #shape：24*1
            train_label = []
            for j in range(i, i + 24):
                x = [load[j]]
                train_seq.append(x)
            # for c in range(2, 8):
            #     train_seq.append(data[i + 24][c])
            train_label.append(load[i + 24])
            train_seq = torch.FloatTensor(train_seq)
            train_label = torch.FloatTensor(train_label).view(-1)
            seq.append((train_seq, train_label))
        # print(seq[-1])
        seq = MyDataset(seq)
        #drop_last会使最后不够一整批的样本被丢弃
        seq = DataLoader(dataset=seq, batch_size=batch_size, shuffle=shuffle, num_workers=0, drop_last=True)
 
        return seq
 
    Dtr = process(train, B, True)
    Val = process(val, B, True)
    Dte = process(test, B, False)
 
    return Dtr, Val, Dte, m, n