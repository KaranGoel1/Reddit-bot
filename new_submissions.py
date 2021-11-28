import praw
import time
import random

reddit = praw.Reddit('bot')

submissions = list(reddit.subreddit('democrats').top(limit=200))

subs = []
for submission in submissions:
    if submission.over_18 == False and submission.is_self:
        the_submission = {
            'title': submission.title,
            'body': submission.selftext,
            'url': submission.url
        }
        subs.append(the_submission)

print('len(subs)=', len(subs))
bottown_sub = reddit.subreddit('BotTown1')
counter = 0

for sub in subs:
    randomizer = ['text', 'url']
    txt_or_url = random.choice(randomizer)
    if txt_or_url == 'text':
        bottown_sub.submit(title=sub['title'], selftext=sub['body'])
        counter += 1
        print('made text submission. number: ', counter)
    elif txt_or_url == 'url':
        bottown_sub.submit(title=sub['title'], url=sub['url'])
        counter += 1
        print('made url submission. number: ', counter)
    time.sleep(20)