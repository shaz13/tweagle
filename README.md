# Tweagle
 
 ![alt](https://github.com/shaz13/tweagle/blob/master/Screen%20Shot%202018-02-12%20at%208.17.55%20PM.jpg)
 
## Requirements
1. Tweepy
2. Pyfiglet
3. Scikit-learn
3. Numpy

## Setup Instructions

1. Clone or download the the repository.
2. Replace the following tokens in `twitter_client.py`
```
 consumer_key = "YOUR_KEY"
 consumer_secret = "CONSUMER SECRET"
 access_token = "ACCESS TOKEN"
 access_secret = "ACCESS SECRET"
 ```
 3. Navigate to the *tweagle-master* folder and run `twe.py` file to launch tweepy

 4. Enter 1 for analyzing user/pages and 2 for streaming event
 
 
 
 
 ## Files and Folders
 A directory `user` is created in the parent folder which consists of folders named on the `usernames`. The streaming data is created in the parent directory itself. Make a note that streaming doesn't stop until CTRL-Z interrupts. \b
 
 
 
 
## Credits
 - Marco Bonanini, Data Scientist
```
The code base is heavily inspired from Marco's book on Social Media paltforms. Tweagle is a port of his work for Twitter Analytics. 
```
