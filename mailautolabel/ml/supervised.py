import pandas
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

import csv_helper

def predictLabel(labelised, unlabelised):
	sample = {'id':'test', 'folder':'test'}
	return [sample, sample]

	"""
	On récupère les mails non labélisés et labélisés dans des df.
	On fait un TF-IDF pour séparer tous les mots et affiche un "score" pour chacun.
	On fait une régression logistique entre le body et le folder des mails déjà labélisé. Le Folder est seulement le nom d'un label.
	Une fois le classifier créé, on l'applique sur les mails non labélisés et on retourne un dictionnaire contenant tous les labels de prédictions.
	"""
	#On récupère les mails labélisés
	filename = csv_helper.getPath(''username)
	df = pandas.read_csv(filename, sep=",", engine="python", header=0)
	
	#On récupère les mails non labélisés
	filename = csv_helper.getPath("UNLABELISED_"+username)
	df2 = pandas.read_csv(filename, sep=",", engine="python", header=0)

	#On prépare les arguments
	X = df.drop(['folder'], axis=1)
	y = pandas.DataFrame(df['folder'])

	X_train = X
	y_train = y
	X_test = df2.drop(['Folder'], axis=1)
	
	print('X : {}\nY : {}'.format(X.shape, y.shape))
	print('X_train : {}\nX_test : {}\ny_train : {}\n'.format(X_train.shape, X_test.shape, y_train.shape))

	"""# TF-IDF vectorizer"""

	vectorizer = TfidfVectorizer(analyzer="word")
	X_train_vec = vectorizer.fit_transform(X_train['Message_body'].values.astype('U'))
	X_train_vec = pandas.DataFrame(X_train_vec.todense(), columns=vectorizer.get_feature_names())

	X_test_vec = vectorizer.transform(X_test['Message_body'].values.astype('U'))
	X_test_vec = pandas.DataFrame(X_test_vec.todense(), columns=vectorizer.get_feature_names())
	X_test_vec.shape

	print('X_train_vec {}\nX_test_vec {}'.format(X_train_vec.shape, X_test_vec.shape))

	"""# Logistic regression"""

	classifier = LogisticRegression(class_weight='balanced')
	y_train = np.ravel(y_train)
	print(classifier.fit(X_train_vec, y_train))

	predicts = classifier.predict(X_test_vec)

	return predicts
