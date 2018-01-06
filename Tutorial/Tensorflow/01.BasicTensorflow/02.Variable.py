import sys
import tensorflow as tf

print("=== System version ===")
print(sys.version, "\n")

print("=== Tensorflow version ===")
print(tf.__version__, "\n")


# practicing with tf.Variable and tf.get_variable.

# Create two variables with tf.Variable.
weights = tf.Variable(tf.random_normal([2, 3], stddev=0.35),
                      name="weights")
biases = tf.Variable(tf.zeros([2]), name="biases")

global_init_op = tf.global_variables_initializer()

# You can check  how to print symbolic variable and real value of a variable 
with tf.Session() as sess:
    sess.run(global_init_op)
    print("=== Direct printing ===")
    print(sess.run([weights, biases]))
    weights_, biases_ = sess.run([weights, biases])
    print("\n=== Check variables ==")
    print("weights:", weights)
    print("biases:", biases)    


print("\n\n")


# Checking if tf.Variable is created newly, when you calls several times. 
def variables():
    tf_variable = tf.Variable(tf.random_normal([2,2]), name="tf_variable_test")
    
    return tf_variable

# First create one tf_variable. 
result1 = variables()
# Second, Another variable is created in the second call. 
result2 = variables()

global_init_op = tf.global_variables_initializer()

# You can notice it is different between result1 and result2.
# So, whenever tf.Variable is called, tf.Variable create a new varialbe.
with tf.Session() as sess:
    sess.run(global_init_op)
    print("=== Direct printing ===")
    print(sess.run([result1, result2]))
    result1_, result2_ = sess.run([result1, result2])
    print("\n=== Check variables ==")
    print("result1:", result1_)
    print("result2:", result2_)    


print("\n\n")


# Create variable with tf.get_variable()

# if you don't specify initializer, by default, tf.glorot_uniform_initializer
my_variable = tf.get_variable("my_variable",  [2,2])
# Here specifying a certain initializer like tf.zeros_initializer)
my_specific_variable = tf.get_variable("my_specific_variable", [2,3], dtype=tf.int32, initializer=tf.zeros_initializer)

other_variable = tf.get_variable("other_variable", dtype=tf.int32, initializer=tf.constant([3, 2]))

global_init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(global_init_op)
    print("=== Direct printing ===")
    print(sess.run([my_variable, my_specific_variable, other_variable]))
    my_variable_, my_specific_variable_, other_variable_ = sess.run([my_variable, my_specific_variable, other_variable])
    print("\n=== Check variables ==")
    print("my_variable:", my_variable_)
    print("my_specific_variable:", my_specific_variable_)
    print("other_variable:", other_variable_)
