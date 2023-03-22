# import gensim
# from nltk.data import find
#
# word2vec_sample = find('models/word2vec_sample/pruned.word2vec.txt')
# w2v_model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)
#
# # write your code here
# # w2v_model.most_similar('piano', topn=5)
# print(w2v_model.similarity('piano', 'guitar'))
import re

_list = ["bee", "ben", "be", "bat", "bed"]
for i in _list:
    print(i, re.match(r"be.", i))
    print(i, re.match(r"bee?", i))