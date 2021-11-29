import praw
import time
from textblob import TextBlob

reddit = praw.Reddit('bot')

counter = 0
submissions = list(reddit.subreddit('BotTown2').top(limit=None))
for submission in submissions:
    submission_text = TextBlob(submission.title + ' ' + submission.selftext)
    print('title of submission = ', submission.title)
    print('submission_text = ', submission_text)
    if 'biden' in submission_text.lower() and submission_text.sentiment.polarity > 0.5:
        submission.upvote()
        counter += 1
        print('upvoted a submission. number: ', counter)
    elif 'biden' in submission_text.lower() and submission_text.sentiment.polarity < -0.5:
        submission.downvote()
        counter += 1
        print('downvoted a submission. number: ', counter)

    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    print('len(all_comments) = ', len(all_comments))
    for comment in all_comments:
        comment_text = TextBlob(comment.body)
        if 'biden' in comment_text.lower() and comment_text.sentiment.polarity > 0.5:
            comment.upvote()
            counter += 1
            print('upvoted a comment. number: ', counter)
        elif 'biden' in comment_text.lower() and comment_text.sentiment.polarity < -0.5:
            comment.downvote()
            counter += 1
            print('downvoted a comment. number: ', counter)
    time.sleep(30)