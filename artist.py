# Import all required dependencies, with Tensorflow as Keras backend

import numpy as np

from scipy.optimize import fmin_l_bfgs_b
from scipy.misc import imsave

from PIL import Image

from keras import backend
from keras.models import Model
from keras.applications.vgg16 import VGG16


# Set default height and width for all images
height = 512
width = 512


# Open and resize original image
original_image = Image.open('/Users/maanavkhaitan/Downloads/hugo.jpg')
original_image = original_image.resize((height, width))

# Open and resize style image
style_image = Image.open('/Users/maanavkhaitan/Downloads/wave.jpg')
style_image = style_image.resize((height, width))


# Convert images to numerical form and add exra dimension so they can be concatenated into tensor later
original_array = np.asarray(original_image, dtype='float32')
original_array = np.expand_dims(original_array, axis=0)

style_array = np.asarray(style_image, dtype='float32')
style_array = np.expand_dims(style_array, axis=0)


# Subtract mean RGB value from each pixel and create inverse of image arrays (more efficient for model to train on)
original_array[:, :, :, 0] -= 103.939
original_array[:, :, :, 1] -= 116.779
original_array[:, :, :, 2] -= 123.68
original_array = original_array[:, :, :, ::-1]

style_array[:, :, :, 0] -= 103.939
style_array[:, :, :, 1] -= 116.779
style_array[:, :, :, 2] -= 123.68
style_array = style_array[:, :, :, ::-1]


# Create backend variables for both image arrays
original_image = backend.variable(original_array)
style_image = backend.variable(style_array)

# Create placeholder for output image with same dimensions
output_image = backend.placeholder((1, height, width, 3))

# Create tensor with all three images: original, style, and output
input_tensor = backend.concatenate([original_image, style_image, output_image], axis=0)


# Initialize VGG16 model in Keras and set default image classification weights
model = VGG16(input_tensor=input_tensor, weights='imagenet', include_top=False)

# Create dictionary of layers in VGG16 model
layers = dict([(layer.name, layer.output) for layer in model.layers])







