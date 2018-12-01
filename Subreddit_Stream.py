import praw
import time



def word_freq(subreddit='todayilearned', type_of='new', num_posts=15 ):
    reddit = praw.Reddit(client_id = 'XGjxaJpnWVWazA', client_secret='Vqd2l6Q_SATMu2_H8nGas9hlAnE', username='Computerdude123', password='garik676',user_agent='bob')
    subreddit = reddit.subreddit(subreddit)

    new_python = subreddit.new(limit=num_posts)

    listr = []
    for sub in new_python:
        if not sub.stickied:
            listr.append(sub.title)

    all_words = {}
    for post in listr:
        words = post.split()
        for word in words:
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

    sorted_by_value = sorted(all_words.items(), key=lambda kv: kv[1], reverse=True)

    # for key in list(sorted_by_value.keys()):
    #     if sorted_by_value[key] == 1"
    #         del hand[key]

    for key, value in sorted_by_value:
        print(key, ':', value)


# for comment in subreddit.stream.comments():
#     parent_id = str(comment.parent())

word_freq()
