###############################################################################
# Trains classifier on given images.
###############################################################################
import os
import torch.optim.adam
import json
import torch.utils.data.dataloader as dl
import torch.nn as nn

# Configurations
with open('config.json', 'r') as jsonfile:
    config = json.load(jsonfile)


# 1. Load classifier if continuing training, else create new classifier.
# Avoids retraining on old data, which could be superfluous and thus inefficient
# or even lead to overfitting.
def _loadModel(default_arch):
    saves = os.listdir(config.MODEL_SAVE_PATH)
    if saves == []:
        net = default_arch()
    else:
        net = torch.load(config.MODEL_SAVE_PATH)
    return net


# 2. Train classifier
def _train(net, loss_fn, dataloader :dl.DataLoader):
    optimizer = torch.optim.Adam(net.parameters())
    for epoch in config.epochs:
        for i, data in enumerate(dataloader):
            images, labels = data
            optimizer.zero_grad()
            logits = net.forward(images)
            loss = loss_fn(logits, labels)
            loss.backward()
            optimizer.step()


# 3. Save classifier state
def _saveModel(net):
    torch.save(net, config.MODEL_SAVE_PATH)


def __main___(dataloader :dl.DataLoader, default_arch :nn.Module, loss_fn):
    net = _loadModel(default_arch)
    _train(net, dataloader, loss_fn)
    _saveModel(net)