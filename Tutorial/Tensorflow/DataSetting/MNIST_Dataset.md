{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# What is the MNIST ?\n",
    "\n",
    "    MNIST is a simple computer vision dataset. this image consists of handwirtten digits like these :\n",
    "\n",
    "![](https://github.com/hyunyoung2/Machine_Learning/tree/master/Tutorial/Tensorflow/DataSetting/images/MNIST.png)\n",
    "\n",
    "    It also includes labels for each image, telling us which digit it is. For example, the labels for the above images ar 5, 0, 4, and 1.  \n",
    "\n",
    "### The MNIST Data\n",
    "\n",
    "    This MNIST data is hosted on __[Yann LeCun's websit](http://yann.lecun.com/exdb/mnist/)__. If you want to download and read MNIST data, these two lines is enough. \n",
    "    \n",
    "```python\n",
    "from tensorflow.examples.tutorials.mnist import input_data\n",
    "mnist = input_data.read_data_sets(\"MNIST_data/\", one_hot=True)\n",
    "# one_hot means MNIST's label is the representaion of one-hot vector. (if one_hot is true)\n",
    "# if ont_hot is false, MNIST' label is just digit between 0 and 9 like these :\n",
    "# if MNIST's label is 3, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]\n",
    "```\n",
    "    The MNIST data is split into three parts: \n",
    "    \n",
    "        - 55,000 data points of training data(minst.train)  \n",
    "        - 10,000 points of test data(mnist.test)\n",
    "        - 5000 points of validation data(mnist.validation)\n",
    "    \n",
    "    The above thing is basic segmentaion of dataset in machine learning. as I mentioned early, MNIST have two part, images and their correspoding labels. for exmapel, **mnist.train.images** for traing images, and **mnist.train.labels** for their correspoding labels. \n",
    "  \n",
    "    Each of images is 28*28 pixels. if we interpret the each of images as a array, the size of a array is 28*28=784. \n",
    "  \n",
    "![](https://github.com/hyunyoung2/Machine_Learning/tree/master/Tutorial/Tensorflow/DataSetting/images/MNIST-Matrix.png)\n",
    "\n",
    "    After making 28*28 pixels into a array(784), we just interpert each of image as a vector in vector space. i.e The MNIST images are just a bunch of points in a 784-dimensional vector space. \n",
    "  \n",
    "    The below is how to download MNIST Dataset, When you want to implement tensorflow with MNIST. \n",
    "\n",
    "## Reference \n",
    "\n",
    "    [MNIST's official site](http://yann.lecun.com/exdb/mnist/)\n",
    "\n",
    "    [MNIST of tensorflow](https://www.tensorflow.org/get_started/mnist/beginners)\n",
    "   \n",
    "    [Github of tensorflow](https://github.com/tensorflow)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The version of tensorflow :  1.3.0 \n",
      "\n",
      "Creating a directory is done!\n"
     ]
    }
   ],
   "source": [
    "# If you start the python setting \n",
    "# help(os-python keyword)\n",
    "\n",
    "# -- the version of python : 3.5 --\n",
    "# -- MNIST data set -- \n",
    "# In order to Create Directory to store material\n",
    "import os \n",
    "import tensorflow as tf\n",
    "\n",
    "# -- The version of Tensorflow is 1.3 --\n",
    "print (\"The version of tensorflow : \", tf.__version__ , \"\\n\")\n",
    "\n",
    "name_dir=\"MNIST_Dataset\"\n",
    "\n",
    "# Get current Directory from \"https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory\"\n",
    "current_dir = os.getcwd()\n",
    "\n",
    "# Create New Directory \n",
    "new_dir = current_dir+\"/data/\"\n",
    "final_dir = new_dir+name_dir\n",
    "\n",
    "# Checking whether 'new_dir' exist or not\n",
    "if not os.path.isdir(new_dir) :\n",
    "    os.makedirs(new_dir)\n",
    "    print(\" '%s' is now in the '%s' \" % (final_dir, new_dir))\n",
    "\n",
    "# Checking whether 'final_dir' exist or not\n",
    "if not os.path.exists(final_dir) : \n",
    "    os.makedirs(final_dir)\n",
    "    print(\" '%s' exist \" % final_dir)    \n",
    "\n",
    "print (\"Creating a directory is done!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TensorFlow github : https://github.com/tensorflow\n",
    "# Download MNIST data set : \n",
    "# the location related to MNIST's readfunction ->  tensorflow.contrib.learn.pyton.learn.datasets.mnist.py\n",
    "### Data Structure checking 28*28 = 784 , this means one of image is 784 as a array.\n",
    "### if you set \"one_hot = True\" up, when trainY[0] equals 7, print(trainY[0]) = [0. 0. 0. 0. 0. 0. 0. 1. 0. 0. ]\n",
    "### if you set \"one_hot = False\" up, when trainY[0] equals 7, print(trainY[0]) = 7\n",
    "from tensorflow.examples.tutorials.mnist import input_data\n",
    "mnist = input_data.read_data_sets(\"final_dir\", one_hot=True)\n",
    "\n",
    "# Load Data \n",
    "## For training \n",
    "trainX = mnist.train.images\n",
    "trainY = mnist.train.labels\n",
    "\n",
    "## For validation of hyperParameter\n",
    "validationX = mnist.validation.images\n",
    "validationY = mnist.validation.labels\n",
    "\n",
    "## For test \n",
    "testX = mnist.test.images\n",
    "testY = mnist.test.labels\n",
    "\n",
    "print (\"\\nMNIST dataset Complete!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# For test about what it looks \n",
    "print (\"===what MNIST looks===\") # for new line\n",
    "print (\"the shape of trainX data :\", trainX.shape, trainX.dtype)\n",
    "print (\"the shape of trainY data :\", trainY.shape, trainY.dtype)\n",
    "print (\"trainY[0] :\", trainY[0])\n",
    "print () # for newline\n",
    "print (\"the shape of validationX data :\", validationX.shape, validationX.dtype)\n",
    "print (\"the shape of validationY data :\", validationY.shape, validationY.dtype)\n",
    "print (\"validationY[0] :\", validationY[0])\n",
    "print () # for newline\n",
    "print (\"the shape of testX data :\", testX.shape, testX.dtype)\n",
    "print (\"the shape of testY data :\", testY.shape, testY.dtype)\n",
    "print (\"testY[0]:\", testY[0])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
