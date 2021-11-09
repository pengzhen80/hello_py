import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

def add_layer(inputs,in_size,out_size,activation_function=None):
  weights = tf.Variable(tf.random.normal([in_size,out_size]))
  biases = tf.Variable(tf.zeros([1,out_size])+0.1)
  wx_plus_b = tf.matmul(inputs,weights)+biases
  if activation_function is Node:
    outputs = wx_plus_b
  else:
    outputs = activation_function(wx_plus_b)
  return outputs