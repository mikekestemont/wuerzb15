from pystyl.corpus import Corpus
corpus = Corpus(language='en')
corpus.add_directory('data/victorian')
corpus.preprocess()
corpus.tokenize(max_size=50000)
corpus.vectorize(mfi=100, ngram_type='word', vector_space='tf')
X = corpus.vectorizer.X
print(X.shape)
titles = corpus.titles
print(titles)
authors = [corpus.target_idx[i] for i in corpus.target_ints]
print(authors)
words = corpus.vectorizer.feature_names
print(words)
import pickle
pickle.dump((titles, authors, words, X.toarray()), open("dummy.p", "wb"))