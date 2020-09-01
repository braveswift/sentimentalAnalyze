from api import twitter_api


def buildTestSet(search_keyword):
    try:

        tweets_fetched = twitter_api.GetSearch(search_keyword, count=150)

        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        tweets = []
        for status in tweets_fetched:
            tweets.append({"text": status.text, "label": None})
        return tweets
    except:
        print("Unfortunately, something went wrong..")
        return None
