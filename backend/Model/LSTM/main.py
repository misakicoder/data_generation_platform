from data_preprocess import nn_seq_us
from train import train
from test import test
import argparse
from datetime import datetime

if __name__ == '__main__':
    #解析参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_size', type=int, default=1)
    parser.add_argument('--hidden_size', type=int, default=64)
    parser.add_argument('--num_layers', type=int, default=1)
    parser.add_argument('--output_size', type=int, default=1)
    parser.add_argument('--batch_size', type=int, default=5)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--lr', type=float, default=0.001)
    parser.add_argument('--weight_decay', type=float, default=0)
    parser.add_argument('--optimizer', type=str, default='adam')
    parser.add_argument('--step_size', type=int, default=10)
    parser.add_argument('--gamma', type=float, default=0.1)
    args = parser.parse_args()
    #训练
    Dtr, Val, Dte, m, n = nn_seq_us(args.batch_size, 'data/data.csv')
    # train(args, Dtr, Val, f'model/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pth')
    #测试
    test(args, Dte, 'model/2024-04-24_20-03-25.pth', m, n)