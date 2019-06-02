# Extracting_and_visualizing_weights
Visualize and view the weights from a .h5 file using python

Visualize weights

get the desired .h5 file 

./h5pyViewer 

use the above command to launch the h5 Viewer the select the h5 file you want to view 

Read the values directly using h5py module

import h5py
f = h5py.File('mobilenet_1_0_224_tf.h5','r')
print(f.keys())
x1 = f['conv1']
x2 = x1['conv']
x3 = x2['kernel:0']
x3.value

