# If you start the python setting 
# help(os-python keyword)

# -- MNIST data set -- 
# In order to Create Directory to store material
import os 
import sys
import tensorflow as tf

# -- The version of python is 3.5.2---
print("The version of python:", sys.version, "\n")

# -- The version of Tensorflow is 1.4 --
print("The version of tensorflow : ", tf.__version__ , "\n")

name_dir="MNIST_Dataset"

# Get current Directory from "https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory"
current_dir = os.getcwd()

# Create New Directory 
new_dir = current_dir+"/data/"
final_dir = new_dir+name_dir

# Checking whether 'new_dir' exist or not
if not os.path.isdir(new_dir) :
    os.makedirs(new_dir)
    print(" '%s' is now in the '%s' " % (final_dir, new_dir))

# Checking whether 'final_dir' exist or not
if not os.path.exists(final_dir) : 
    os.makedirs(final_dir)
    print(" '%s' exist " % final_dir)    

print("Creating a directory is done!")


# TensorFlow github : https://github.com/tensorflow
# Download MNIST data set : 
# the location related to MNIST's readfunction ->  tensorflow.contrib.learn.pyton.learn.datasets.mnist.py
# Data Structure checking 28*28 = 784 , this means one of image is 784 as a array.
# if you set "one_hot = True" up, when trainY[0] equals 7, 
# Index of array of trainY[0]   0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#           print(trainY[0]) = [0. 0. 0. 0. 0. 0. 0. 1. 0. 0]
# if you set "one_hot = False" up, when trainY[0] equals 7, 
#      print(trainY[0]) = 7
# Whatever variable is, it doesn't matter, If you enter a string.
# after creating directory named the string you chose, MNIST data is saved under the directory.
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(final_dir, one_hot=True)

# Load Data 
## For training 
trainX = mnist.train.images
trainY = mnist.train.labels

## For validation of hyperParameter
validationX = mnist.validation.images
validationY = mnist.validation.labels

## For test 
testX = mnist.test.images
testY = mnist.test.labels

print("\nMNIST dataset Complete!")
