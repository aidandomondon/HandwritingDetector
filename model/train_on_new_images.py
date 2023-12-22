from torch.nn import CrossEntropyLoss
from model import fetch_new_images, initial_classifier, train

def __main__():
    '''
    Starts training the neural net on any images that might not have
    been fetched.
    '''
    dl = fetch_new_images.__main__()
    arch = initial_classifier.InitialClassifier
    loss_fn = CrossEntropyLoss()
    train.__main__(dl, arch, loss_fn)