import praw
import time



def word_freq(subreddit='todayilearned', type_of='hot', num_posts=30 ):
    reddit = praw.Reddit(client_id = 'XGjxaJpnWVWazA', client_secret='Vqd2l6Q_SATMu2_H8nGas9hlAnE', username='Computerdude123', password='garik676',user_agent='bob')
    subreddit = reddit.subreddit(subreddit)

    new_python = subreddit.hot(limit=num_posts)
    
    #adds all posts into a master list (lsitr)
    listr = []
    for sub in new_python:
        if not sub.stickied:
            listr.append(sub.title)
            
    #split the posts by words to get the counts
    all_words = {}
    for post in listr:
        words = post.split()
        
        #add the word to the dict or increase count by 1 if already found in dict
        for word in words:
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1
                
    # sorts the dict to have most frequent words in the beginnging
    sorted_by_value = sorted(all_words.items(), key=lambda kv: kv[1], reverse=True)

    # for key in list(sorted_by_value.keys()):
    #     if sorted_by_value[key] == 1"
    #         del hand[key]

    #prints results from the dict
    for key, value in sorted_by_value:
        print(key, ':', value)


# for comment in subreddit.stream.comments():
#     parent_id = str(comment.parent())

word_freq()
