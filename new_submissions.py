import praw
import time
import random

reddit = praw.Reddit('bot')

submissions = list(reddit.subreddit('liberal').top(limit=None))

subs = []
for submission in submissions:
    if submission.over_18 == False:
        the_submission = {
            'title': submission.title,
            'body': submission.selftext,
            'url': submission.url
        }
        subs.append(the_submission)

print('len(subs)=', len(subs))
bottown_sub = reddit.subreddit('BotTown2')
counter = 0

for sub in subs:
    if sub['body'] != '':
        print(sub['body'][:10])
        bottown_sub.submit(title=sub['title'], selftext=sub['body'])
        counter += 1
        print('made text submission. number: ', counter)
    else:
        bottown_sub.submit(title=sub['title'], url=sub['url'])
        counter += 1
        print('made url submission. number: ', counter)
    time.sleep(90)