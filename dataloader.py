from torch.utils import data
import torch
import torch.nn.functional as F
import sklearn
import numpy as np



class load_dataset(data.Dataset):

    def __init__(self,
                 data = [],
                 labels = [],
                 num_classes = 2,
                 augment=None,
                 ):


        self.augment = augment
        self.data = data
        self.labels = labels
        self.num_classes = num_classes
                    

    def __len__(self):
        return len(self.data)

    def augment_traces(self, X):

        return y

    def normalize99(self, X):
    
        sklearn.preprocessing.minmax_scale(X, feature_range=(0, 1), axis=0, copy=True)
            
        return X
    
    def rescale01(self, X):
            
        X = (X - np.min(X)) / (np.max(X) - np.min(X))
            
        return X

    def postprocess(self, X, y):
        
        X = self.normalize99(X)
        X = self.rescale01(X)
        
        # Typecasting
       
        X = torch.from_numpy(X.copy()).float()
        X = torch.unsqueeze(X,0)
        
        y = F.one_hot(torch.tensor(y), num_classes=self.num_classes).float()


        return X, y

    def __getitem__(self, index: int):

        X, y = self.data[index], self.labels[index]
        
        # if self.augment:
        #     X = self.augment_traces(X)
        
        X, y = self.postprocess(X, y)
        
        return X, y