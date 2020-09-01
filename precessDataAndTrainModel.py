import csv
import pickle

import nltk
from PreProcessTweets import PreProcessTweets


def buildVocabulary(preprocessedTrainingData):
    all_words = []

    for (words, sentiment) in preprocessedTrainingData:
        all_words.extend(words)

    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()

    return word_features


def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features


corpusFile = "corpus.csv"
tweetDataFile = "tweetData.csv"
featuresFile = "features.csv"

trainingDataFromFile = []

with open(tweetDataFile, 'r') as csvfile:
    lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
    for row in lineReader:
        if (row[2] == "negative" or row[2] == "positive"):
            trainingDataFromFile.append(row)


#process training data
tweetProcessor = PreProcessTweets()
preprocessedTrainingSet = tweetProcessor.processTraningData(trainingDataFromFile)

#extrac features
word_features = buildVocabulary(preprocessedTrainingSet)
trainingFeatures = nltk.classify.apply_features(extract_features, preprocessedTrainingSet)

#train model
NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)

save_classifier = open("naivebayes2.pickle","wb")
pickle.dump(NBayesClassifier, save_classifier)
save_classifier.close()
