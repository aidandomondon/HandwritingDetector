###############################################################################
# Classifies the given image
###############################################################################
from config import Config
import torch.optim.adam
import torch.utils.data.dataloader as dl
import torch.nn as nn


# 1. Load classifier.
def _loadModel():
    return torch.load(Config.MODEL_SAVE_PATH)


# 2. Train classifier
def _classify(net :nn.Module, image :list[list[int]]):
    return torch.argmax(net.forward(image))


def __main__(image :list[list[int]]):
    net = _loadModel()
    return _classify(net, image)