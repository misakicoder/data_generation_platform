from itertools import chain
from tqdm import tqdm
from model import LSTM
import torch
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

def get_mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def test(args, Dte, path, m, n):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    pred = []
    y = []
    print('loading models...')
    input_size, hidden_size, num_layers = args.input_size, args.hidden_size, args.num_layers
    output_size = args.output_size
    model = LSTM(input_size, hidden_size, num_layers, output_size, batch_size=args.batch_size).to(device)
    # models = LSTM(input_size, hidden_size, num_layers, output_size, batch_size=args.batch_size).to(device)
    model.load_state_dict(torch.load(path)['models'])
    model.eval()
    print('predicting...')
    for (seq, target) in tqdm(Dte):
         
        target = list(chain.from_iterable(target.data.tolist()))
        y.extend(target)
        seq = seq.to(device)
        with torch.no_grad():
            y_pred = model(seq)
            y_pred = list(chain.from_iterable(y_pred.data.tolist()))
            pred.extend(y_pred)
 
    y, pred = np.array(y), np.array(pred)
    y = (m - n) * y + n
    pred = (m - n) * pred + n
    print('mape:', get_mape(y, pred))
    print('mae:', mean_absolute_error(y, pred))
    print('mse:', mean_squared_error(y, pred))
    print('rmse:', np.sqrt(mean_squared_error(y, pred)))
    print('r2:', r2_score(y, pred))
    # plot
    x = [i for i in range(1, 151)]
    x_smooth = np.linspace(np.min(x), np.max(x), 900)
    y_smooth = make_interp_spline(x, y[150:300])(x_smooth)
    plt.plot(x_smooth, y_smooth, c='green', marker='*', ms=1, alpha=0.75, label='true')
 
    y_smooth = make_interp_spline(x, pred[150:300])(x_smooth)
    plt.plot(x_smooth, y_smooth, c='red', marker='o', ms=1, alpha=0.75, label='pred')
    plt.grid(axis='y')
    plt.legend()
    plt.show()