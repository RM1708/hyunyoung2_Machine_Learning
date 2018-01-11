# python code to practice word embedding
# How to use tensorboard for WordEmbedding. 
import os
import tensorflow as tf

# word embedding function of tensorflowi
# look up embedding in Tensorflow

word_embeddings = tf.get_variable("word_embeddings_test", [2, 2])
embedded_word_ids = tf.nn.embedding_lookup(word_embeddings, 1)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    embedding_result_test, embedded_word_result_test = sess.run([word_embeddings, embedded_word_ids])
    print("=== the test result ===\n")
    print("The result of word_embedding:\n",embedding_result_test, "\n")
    print("The result of embedded_word_ids:\n",embedded_word_result_test, "\n")

# How to use tensorboard's embedding projector for WordEmbedding. 
# with metadata file 

LOG_DIR = os.path.join(os.getcwd(),"log/")
EMBEDDING_SIZE = 3
VOCA_SIZE = 3

print("the current working directory:", LOG_DIR, "\n")

LABEL_FILE = os.path.join(os.getcwd(), "log/lables.tsv")

print("the current LABEL_FILE:", LABEL_FILE, "\n")

LABEL_NUM = 3
LABEL = ["NLP", "Deep Learning", "test"]

# Write label file 
with open(LABEL_FILE,"w") as f:
    for i in range(LABEL_NUM):
        f.write(LABEL[i]+"\n")
    print("labels.tsv file Created!\n")

# word vector of embedding. 
embedding_input = tf.Variable([[0.1,0.2, 0.2],[0.5, 0.5, 0.5],[0.3,0.3,0.3]], dtype=tf.float32, name="input_embedding-no-label")

# For input of Tensorboard Projector
embeddings = tf.Variable(tf.zeros([VOCA_SIZE,EMBEDDING_SIZE], name="embedding_intial_tensor"), name="real_Embedding")
assignment = embeddings.assign(embedding_input)                       

# To initilize the variable. 
init = tf.global_variables_initializer()

# To add ops to save and restore all the variable
# When you want to make it
saver = tf.train.Saver()

with tf.Session() as sess:
    
    sess.run(init)
    
    # print embedding_input
    embedding_input_, embeddings_ = sess.run([embedding_input, embeddings])
    print("embedding_ipnut:\n", embedding_input_)
    print("embeddings:\n", embeddings_)
    assignment_, embeddings2_ = sess.run([assignment, embeddings])
    print("assignment:\n", assignment_)
    print("embeddings2:\n", embeddings2_)
    
    # Format: tensorflow/contrib/tensorboard/plugins/projector/projector_config.proto
    config = tf.contrib.tensorboard.plugins.projector.ProjectorConfig()
    # You can add multiple embeddings. Here we add only one.
    embedding_config = config.embeddings.add()
    embedding_config.tensor_name = embeddings.name
    # Link this tensor to its metadata file (e.g. labels).
    embedding_config.metadata_path = LABEL_FILE
    
    # Use the same LOG_DIR where you stored your checkpoint.
    summary_writer = tf.summary.FileWriter(LOG_DIR)
    
    # The next line writes a projector_config.pbtxt in the LOG_DtenIR. TensorBoard will
    # read this file during startup.
    tf.contrib.tensorboard.plugins.projector.visualize_embeddings(summary_writer, config)
    
    
    save_path1 = saver.save(sess, os.path.join(LOG_DIR, "test_embedding_model.ckpt"), global_step=1)
    print("\nModel Saved in file: %s" % save_path1)
