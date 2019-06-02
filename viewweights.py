import h5py 
import numpy as np

def isGroup(obj):
    if isinstance(obj,h5py.Group):
        return True

def isDataset(obj):
    if ininstace(obj,h5py.Dataset):
        return True
    return False

def getDatasetFromGroup(datasets,obj):
    if isGroup(obj):
        for key in obj:
            x = obj[key]
            getDatasetFromGroup(datasets,x)
    else:
        datasets.append(obj)

def getWeightsForLayer(layerName,f):
    weights = []
    for key in f:
        if layerName in key:
            obj = f[key]
            datasets = []
            getDatasetFromGroup(datasets,obj)
            
            for dataset in datasets:
                w = np.array(dataset)
                weights.append(w)
    return weights
##-----------------main--------------------------------------##
f = h5py.File('mobilenet_1_0_224_tf.h5',mode='r')
print(f.keys())
layer = input("Enter the Layer Name: ")
weights = getWeightsForLayer(layer,f)
print(weights)
