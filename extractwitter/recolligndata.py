import twitter

consumer_key ='dTG24NJgFeIZ8VkWN3H7ZFTYR'
consumer_secret = 'I0NnZaH000KS6IMAEB7AvnTJw6YLeRj5eazo64HfkkTv23D23z'
access_token ='1909906172-zhXPdYxASxriH5b5XWAiUze8RQgObpJ1kfvdaOp'
access_secret ='i5QCVH5yTbjdYudmMmBrOYqckO3C04w00VltmucNUGoEQ'

api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_secret)


print(api.VerifyCredentials())


friends = api.GetFriends()
followers = api.GetFollowers()
