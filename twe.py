#!/usr/bin/python
import os
import sys
import json
import time
import math
import subprocess as sp
from tweepy import Cursor
from twitter_client import get_twitter_client
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

sp.call('clear',shell=True)

MAX_FRIENDS = 15000

def GetCluster(username):
    from collections import defaultdict
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans


    filename = "users/"+ username + "/followers.jsonl"
    k = 5
    with open(filename) as f:
        # load data
        users = []
        for line in f:
            profile = json.loads(line)
            users.append(profile['description'])
    # create vectorizer
    vectorizer = TfidfVectorizer(max_df=0.8,
                                 min_df=2,
                                 max_features=None,
                                 stop_words='english',
                                 ngram_range=(1, 2),
                                 use_idf=True)
    # fit data
    X = vectorizer.fit_transform(users)
    print("Data dimensions: {}".format(X.shape))
    # perform clustering
    km = KMeans(n_clusters=k)
    km.fit(X)
    clusters = defaultdict(list)
    for i, label in enumerate(km.labels_):
        clusters[label].append(users[i])
    # print 10 user description for this cluster
    for label, descriptions in clusters.items():
        print "\n" + Fore.BLUE + "-"*80
        print( Fore.BLUE + 'Follower Cluster {}'.format(label +1))
        print Fore.BLUE + "-"*80
        for desc in descriptions[:50]:
            print(desc)

def EagleAUser(username):


    print Fore.GREEN + "\nRunning Module 1 : Get User Timeline"
    sp.call('python twitter_get_user_timeline.py ' + username,shell=True)

    print Fore.GREEN + "\nRunning Module 2 : Hashtag Frequency"
    time.sleep(2)
    sp.call('python twitter_hashtag_frequency.py users/'+ username +
            '/user_timeline_'+ username +'.jsonl', shell=True)

    print Fore.GREEN + "\nRunning Module 3 : Hashtag Stats"
    time.sleep(2)
    sp.call('python twitter_hashtag_stats.py users/'+ username +
            '/user_timeline_'+ username +'.jsonl', shell=True)

    print Fore.GREEN + "\nRunning Module 4 : Mention Frequency"
    time.sleep(2)
    sp.call('python twitter_mention_frequency.py users/'+ username +
        '/user_timeline_'+ username +'.jsonl', shell=True)

    print Fore.GREEN + "\nRunning Module 5 : Term Frequency"
    time.sleep(2)
    sp.call('python twitter_term_frequency.py users/'+ username +
        '/user_timeline_'+ username +'.jsonl', shell=True)

    print Fore.GREEN + "\nRunning Module 6 : Exporting Term Frequency Graph"
    time.sleep(2)
    sp.call('python twitter_term_frequency_graph.py users/'+ username +
        '/user_timeline_'+ username +'.jsonl', shell=True)
    print Fore.GREEN + "\nDone..."

    print Fore.GREEN + "\nRunning Module 7 : Dowloading User Data ..."
    time.sleep(2)
    sp.call('python twitter_get_user.py '+ username, shell=True)

    print Fore.GREEN + "\nRunning Module 7 : Getting User Follower Data"
    time.sleep(2)
    sp.call('python twitter_followers_stats.py '+ username, shell=True)

    print Fore.GREEN + "\nRunning Module 8 : Minning the followers' data"
    GetCluster(username)

def EagleStream(tags):
    print Fore.GREEN + "\nRunning Module 1 : Streaming Twitter Data for event - {}".format(tags)

    sp.call('python twitter_streaming.py '+ tags, shell=True)



from pyfiglet import Figlet
f = Figlet(font='nancyj')
print "\n" + Fore.MAGENTA + f.renderText('Tweagle')
print  Fore.MAGENTA + "~ by Mohammad Shahebaz"

print "-"*80


task_list = ("Analyze a twitter user/page", "Stream an event")
for i,c in enumerate(task_list):
    print "{}.{}".format(i+1,c)

choice = input("Enter an option: ")

if choice == 1:
    screen_name = raw_input("Enter twitter username: ")
    EagleAUser(screen_name)
elif choice == 2:

    tags = raw_input("Enter event Hashtag. Seperate by spaces: ")

    tag_list = []
    for i in tags.split(' '):
        tag_list.append("\\" + "#" + i)
    tags_proccssed =  " ".join(tag_list)

    EagleStream(tags_proccssed)


else:
    ValueError("Invalid Input")
