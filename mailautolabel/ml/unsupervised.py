# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

def get_scores(data):
	# on transforme le corpus en une matrice TF-IDF
	vect = TfidfVectorizer(ngram_range=(1,2), max_df=5, stop_words='english')
	vect.fit(data['text'])
	terms = vect.get_feature_names()
	X = pd.DataFrame(vect.transform(data['text']).todense(), columns=terms)
	X.shape

	# Application de KMeans
	N_CLUSTERS = (10)
	kmeans = KMeans(n_clusters=N_CLUSTERS)
	kmeans.fit(X)

	# cluster du non supervisé comme cactégorie d'apprentissage
	data['categorie'] = (kmeans.labels_)

	order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
	for i in range(N_CLUSTERS):
		print("Cluster {}: ".format(i))
		for ind in order_centroids[i, :10]:
			print(' {}'.format(terms[ind]))

	clf = RandomForestClassifier(n_estimators=100, random_state=0)
	clf.fit(X, data['categorie'])
	importances = clf.feature_importances_
	indices = np.argsort(importances)[::-1]
	print(np.array(terms)[indices[:50]])
	print(clf.predict(X))

