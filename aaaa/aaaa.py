import tensorflow as tf

sess = tf.Session()
hello = tf.constant("hello")
sess.run(hello)
print(sess.run)