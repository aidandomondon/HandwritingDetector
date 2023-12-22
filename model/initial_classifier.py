import torch.nn as nn

class InitialClassifier(nn.Module):
    '''
    Initial implementation of a classifier for quick mocking.
    '''
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(1, 32, (3, 3)),
            nn.Conv2d(32, 64, (3, 3)),
            nn.Conv2d(64, 25, (3, 3)),
            nn.Flatten(),
            nn.Linear(128, 75),
            nn.ReLU(),
            nn.Linear(75, 25),
            nn.ReLU(),
            nn.Linear(25, 10),
            nn.ReLU(),
            nn.Softmax()
        )
    
    def forward(self, X):
        return self.layers(X)