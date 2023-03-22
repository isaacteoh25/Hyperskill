import gensim
from nltk.data import find

word2vec_sample = find('models/word2vec_sample/pruned.word2vec.txt')
w2v_model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)