import random
import praw
import time

'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''

madlibs = [
    "Joe Biden is [LEFT] leaning. He is [FIT] to lead the [COUNTRY]. Politically, he is the [RIGHT] choice. He has really [GOOD] [FOREIGN] policy.",
    "Joseph Robinette Biden is [CERTAINLY] the [BEST] choice for this [COUNTRYS] presidency. Without him [PEOPLE] would be [DYING] at [MUCH] higher rates.",
    "Sanders is a close [MATCH] to Biden. His [SOCIAL] policies are more [INTENSE], but it shows that he [CARES] about the people. They are both also very [OLD].",
    "It is very sad that Biden's son died, [HOWEVER] it makes him a stronger [PERSON]. He has had to [DEAL] with many [CHALLENGES] throughout his [LIFE].",
    "Although, Clinton [CAME] close to [BEATING] Trump, she had too many [ISSUES]. Biden [HAS] none of those [PROBLEMS].",
    "[BIDEN] is an old but wise [MAN]. His 50+ years of [EXPERIENCE] can only make him [AMONG] the best [CANDIDATES] for the country."
    ]

replacements = {
    'LEFT' : ['left', 'liberal', 'far-left'],
    'FIT' : ['fit', 'equipped'],
    'COUNTRY' : ['country', 'nation'],
    'RIGHT' : ['right', 'correct', 'appropriate'],
    'GOOD'  : ['good', 'thoughtful', 'high quality'],
    'FOREIGN' : ['foreign', 'fiscal', 'green'],
    'CERTAINLY' : ['certainly', 'definitely', 'absolutely'],
    'BEST' : ['best', 'prime', 'ultimate'],
    'COUNTRYS' : ['country\'s', 'nation\'s'],
    'PEOPLE' : ['people', 'folks', 'residents'],
    'DYING' : ['dying', 'perishing', 'passing away'],
    'MUCH' : ['much', 'significantly'],
    'MATCH' : ['match', 'rival'],
    'SOCIAL' : ['social', 'fiscal'],
    'INTENSE' : ['intense', 'radical', 'extreme'],
    'CARES' : ['cares', 'thinks'],
    'OLD' : ['old', 'ancient'],
    'HOWEVER' : ['however', 'but'],
    'PERSON' : ['person', 'individual'],
    'DEAL' : ['deal', 'get through'],
    'CHALLENGES' : ['challenges', 'difficulties', 'tough times'],
    'LIFE' : ['life', 'tenure', 'career'],
    'CAME' : ['came', 'was'],
    'BEATING' : ['beating', 'defeating'],
    'ISSUES' : ['issues', 'problems'],
    'HAS' : ['has', 'posseses'],
    'PROBLEMS' : ['problems', 'downsides', 'issues'],
    'BIDEN' : ['Biden', 'Joe Biden'],
    'MAN' : ['man', 'guy', 'individual'],
    'EXPERIENCE' : ['experience', 'expertise'],
    'AMONG' : ['among', 'one of'],
    'CANDIDATES' : ['candidates', 'presidents']
    }

reddit = praw.Reddit('bot', user_agent='cs40')
def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('[' + k + ']', random.choice(replacements[k]))
    
    return s

submission = reddit.submission('qr05je')
for i in range(101):
    submission.reply(generate_comment())
    time.sleep(20)
    print('comment' + str(i))
for i in range(10):
    submission.comments[i].reply(generate_comment())
    time.sleep(10)
    print('reply')

