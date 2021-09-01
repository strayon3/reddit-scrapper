import praw
import pandas as pd
import datetime as dt
from secret import api_secret
from secret import user_secret
from secret import username
from secret import password

reddit = praw.reddit(client_id = #client id here, 
                    client_secret = #client secret here,
                    user_agent = "nsfw-scrraper",
                    username = username,
                    password = password
                     )

sub_reddit = reddit.subreddit('dankmemes')

new_subreddit = sub_reddit.new(limit=500)

for submission in sub_reddit.new(limit=1):
    print(submission.title, submission.id)

    new_posts = {
        "title":[],
        "id":[],
        "url": []
    }

for submisiion in new_subreddit:
    new_posts["title"].append(submisiion.title)
    new_posts["id"].append(submisiion.id)
    new_posts["url"].append(submisiion.url)

topics_data = pd.DataFrame(new_posts)


