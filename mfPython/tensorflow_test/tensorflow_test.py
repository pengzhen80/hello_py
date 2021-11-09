import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

###create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

###create tensorflow structure start
weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = weights*x_data+biases

loss = tf.reduce_mean(tf.square(y-y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initializer_all_variables()
###create tensorflow structure end

sess = tf.session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.show()

for step in range(201):
    sess.run(train)
    if 0 == step%20:
        print(step,sess.run(weights),sess.run(biases))