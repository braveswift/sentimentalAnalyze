# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pickle

from PreProcessTweets import PreProcessTweets
from buildTestSet import buildTestSet


#get data from Twitter API
from precessDataAndTrainModel import extract_features

search_keyword = input("Enter a search keyword:")
testDataSet = buildTestSet(search_keyword)


#precess test data
tweetProcessor = PreProcessTweets()
preprocessedTestSet = tweetProcessor.processTestData(testDataSet)

#get classifier
classifier_f = open("naivebayes2.pickle", "rb")
NBayesClassifier = pickle.load(classifier_f)
classifier_f.close()

NBResultLabels = [NBayesClassifier.classify(extract_features(tweet[0])) for tweet in preprocessedTestSet]
print(NBResultLabels)
if NBResultLabels.count('positive') > NBResultLabels.count('negative'):
    print("Overall Positive Sentiment")
    print("Positive Sentiment Percentage = " + str(100*NBResultLabels.count('positive')/len(NBResultLabels)) + "%")
else:
    print("Overall Negative Sentiment")
    print("Negative Sentiment Percentage = " + str(100*NBResultLabels.count('negative')/len(NBResultLabels)) + "%")
