import sys
import tensorflow as tf

print("=== System version ===")
print(sys.version, "\n")

print("=== Tensorflow version ===")
print(tf.__version__, "\n")

# === What is the rank of tensor? ===
# Rank 0 (scalar)
animal = tf.Variable("Elephant", tf.string)
integer = tf.Variable(451, tf.int32)
# Rank 1 (1-dimension, vector)
floating_array  = tf.Variable([3.14159, 2.71828], tf.float32)
# Rank 2 (2-dimension, matrix)
# Normally, A rank 2 tensor object consists of as least one row and at least one column.
matrix = tf.Variable([[7],[11]], tf.int32)
# To check what version of rank each variables is?
rank0 = tf.rank(animal)
rank1 = tf.rank(floating_array)
rank2 = tf.rank(matrix)

global_init_op = tf.global_variables_initializer() 

with tf.Session() as sess:
    sess.run(global_init_op)
    #print(sess.run([animal, integer, floating_array, matrix, rank0, rank1, rank2]))
    animal_, integer_, floating_array_, matrix_, rank0_, rank1_, rank2_ = sess.run([animal, integer, floating_array, matrix, rank0, rank1, rank2])
    print("=== check each variables ===")
    print("animal:", animal_, "|", "integer:", integer_)
    print("floating array:", floating_array_, "|", "matrix:", matrix_)
    print("rank0:", rank0_, "|", "rank1:", rank1_, "|", "rank2", rank2_)


print("\n\n")


# === What is the rank of shape? ===
# Every element in a tensor is one 
rank_three_tensor = tf.ones([3, 2, 1])
# To check the shape of a tensor
shape_rank_three_tensor = tf.shape(rank_three_tensor)
# To reshape of a tensor(rank 2)
matrix = tf.reshape(rank_three_tensor, [1, 6])
# To check evaluating with some number after reshaping 
m = matrix + 2
# To Check what kind of shape matrix has
shape = tf.shape(matrix)
shape0 = tf.shape(matrix)[0]
shape1 = tf.shape(matrix)[1]

global_init_op = tf.global_variables_initializer() 

with tf.Session() as sess:
    sess.run(global_init_op)
    #print(sess.run([rank_three_tensor, shape_rank_three_tensor, matrix, shape, shape0, shape1]))
    rank_three_tensor_, shape_rank_three_tensor_, matrix_, shape_, shape0_, shape1_, m_ = sess.run([rank_three_tensor, shape_rank_three_tensor, matrix, shape, shape0, shape1, m])
    print("=== check each variables ===")
    print("rank three tensor\n:", rank_three_tensor_)
    print("matrix of rank three tensor reshaped:", matrix)
    print("shape of matrix:", shape_, "|", "shape[0] of matrix:", shape0_, "|", "shape[1] of matrix:", shape1_)
    print("matrix + 2 after reshaping:", m_)
