#!/usr/bin/python
import os
import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    user = sys.argv[1]
    client = get_twitter_client()
    dirname = "users/{}".format(user)
    try:
        os.makedirs(dirname, mode=0o755)
    except OSError:
        print("Directory {} already exists".format(dirname))
        sys.exit(1)
    except Exception as e:
        print("Error while creating directory {}".format(dirname))
        print(e)
        sys.exit(1)
    print "Building timeline JSON file for {}...".format(user)
    fname = "{}/user_timeline_{}.jsonl".format(dirname,user)
    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json)+"\n")
    print "Timeline successfully exported to {}".format(dirname)
