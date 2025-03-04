from model import LSTM
import torch
from torch.optim.lr_scheduler import StepLR
import torch.nn as nn
import numpy as np
import copy
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO,filename="log.log")

def get_val_loss(args, model, Val):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.eval()
    loss_function = nn.MSELoss().to(device)
    val_loss = []
    for (seq, label) in Val:
        seq = seq.to(device)
        label = label.to(device)
        y_pred = model(seq)
        loss = loss_function(y_pred, label)
        val_loss.append(loss.item())
    return np.mean(val_loss)


def train(args, Dtr, Val, path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    input_size, hidden_size, num_layers = args.input_size, args.hidden_size, args.num_layers

    model = LSTM(input_size, hidden_size, num_layers, output_size=args.output_size ,batch_size=args.batch_size).to(device)
 
    loss_function = nn.MSELoss().to(device)
    if args.optimizer == 'adam':
        optimizer = torch.optim.Adam(model.parameters(), lr=args.lr,
                                     weight_decay=args.weight_decay)
    else:
        optimizer = torch.optim.SGD(model.parameters(), lr=args.lr,
                                    momentum=0.9, weight_decay=args.weight_decay)
    #学习率定制器
    scheduler = StepLR(optimizer, step_size=args.step_size, gamma=args.gamma)
    # training
    min_epochs = 10
    best_model = None
    min_val_loss = 5
    for epoch in tqdm(range(args.epochs)):
        train_loss = []
        for (seq, label) in Dtr:
            seq = seq.to(device)
            label = label.to(device)
            y_pred = model(seq)
            loss = loss_function(y_pred, label)
            train_loss.append(loss.item())
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
 
        scheduler.step()
        # validation
        val_loss = get_val_loss(args, model, Val)
        if epoch > min_epochs and val_loss < min_val_loss:
            min_val_loss = val_loss
            best_model = copy.deepcopy(model)
        logging.info('epoch {:03d} train_loss {:.8f} val_loss {:.8f}'.format(epoch, np.mean(train_loss), val_loss))
        model.train()
 
    state = {'models': best_model.state_dict()}
    torch.save(state, path)