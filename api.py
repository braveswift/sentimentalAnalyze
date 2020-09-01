import twitter
twitter_api = twitter.Api(consumer_key = 'wJIfySEjtlX0xwCJgySazTAgC',consumer_secret = '8uUWiTUWdQJlZeacLmgcQxMS97de1oZpbOzU28OfaiO5VcSb3j',
                          access_token_key = '1169853504006942721-zg2jkjBU0j5huCP3secBB2IO7KX6QW',
                          access_token_secret = 'IwLS1Fe298HyLr6KcXKhgIO1o64tXRPqyLDg5z0NxjV6f' )

print (twitter_api.VerifyCredentials())
