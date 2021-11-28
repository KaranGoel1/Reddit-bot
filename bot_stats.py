import praw

# FIXME:
# login to reddit with your bot's credentials;
# recall that this requires creating a praw.ini file
# 
# WARNING:
# If you include any credential information in your final submission,
# you will receive NEGATIVE POINTS on your lab!!!
reddit = praw.Reddit('bot', user_agent='cs40')

# connect to the "Main Discussion Thread" reddit submission
submission = reddit.submission(url='https://old.reddit.com/r/BotTown/comments/qqmr8l/main_discussion_thread/')

# FIXME:
# Click the "view more comments" buttons in the reddit submission in order to download all comments.
#
# HINT:
# This step takes a long time.
# It takes the PRAW library about 1 second to "click" a link,
# and so it takes about 1 minute total to click all of them.
# I recommend saving this step for last since it will slow down your ability to run the steps below considerably.
# Get those working, then come back here and get this working.

# FIXME:
# Loop through all the top level comments to calculate:
# 1. The total number of non-deleted top level comments,
# 2. The total number of deleted top level comments,
# 3. The total number of comments sent by each user.
#    You should use a dictionary where the keys are the username and the values are the total number of comments.
print('='*40)
print('top level comments')
print('='*40)
comments_per_user = {}
non_deleted_top_comments = 0
deleted_top_comments = 0

for top_level_comment in submission.comments:
    if top_level_comment.author is not None:
        non_deleted_top_comments += 1
    if top_level_comment.author is None:
        deleted_top_comments += 1
    try:
        comments_per_user[top_level_comment.author] = comments_per_user[top_level_comment.author] + 1
    except KeyError:
        comments_per_user[top_level_comment.author] = 1

print('non_deleted_top_lvl_comments = ', non_deleted_top_comments)
print('deleted_top_level_comments = ', deleted_top_comments)

print('='*40)
print('top level comments authors')
print('='*40)

del comments_per_user[None]
for author in comments_per_user:
    print(author, ': ', comments_per_user[author])
# FIXME:
# Repeat the calculations above,
# but do it for ALL comments,
# not just top level comments.
print('='*40)
print('all comments')
print('='*40)
comments_per_user = {}
non_deleted_comments = 0
deleted_comments = 0

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    if comment.author is not None:
        non_deleted_comments += 1
    if comment.author is None:
        deleted_comments += 1
    try:
        comments_per_user[comment.author] = comments_per_user[comment.author] + 1
    except KeyError:
        comments_per_user[comment.author] = 1

print('non_deleted_comments = ', non_deleted_comments)
print('deleted_comments = ', deleted_comments)

print('='*40)
print('all comments authors')
print('='*40)

del comments_per_user[None]
for author in comments_per_user:
    print(author, ': ', comments_per_user[author])