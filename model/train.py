###############################################################################
# Trains classifier on given images.
###############################################################################
from config import Config
from os import path
import torch.optim.adam
import torch.utils.data.dataloader as dl
import torch.nn as nn


# 1. Load classifier if continuing training, else create new classifier.
# Avoids retraining on old data, which could be superfluous and thus inefficient
# or even lead to overfitting.
def _loadModel(default_arch):
    if path.isfile(Config.MODEL_SAVE_PATH):
        return torch.load(Config.MODEL_SAVE_PATH)
    else:
        return default_arch()


# 2. Train classifier
def _train(net :nn.Module, loss_fn, dataloader :dl.DataLoader):
    optimizer = torch.optim.Adam(net.parameters())
    for epoch in range(Config.EPOCHS):
        for _, data in enumerate(dataloader):
            images, labels = data   # unzip
            optimizer.zero_grad()
            logits = net.forward(images)
            loss = loss_fn(logits, labels)
            loss.backward()
            optimizer.step()


# 3. Save classifier state
def _saveModel(net):
    torch.save(net, Config.MODEL_SAVE_PATH)


def __main__(dataloader :dl.DataLoader, default_arch :nn.Module, loss_fn):
    net = _loadModel(default_arch)
    _train(net, loss_fn, dataloader)
    _saveModel(net)