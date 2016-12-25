from imgurpython import ImgurClient
import json
import random
import os

user = json.load(open(os.path.join(os.path.dirname(__file__), 'secret/user.json')))
client = ImgurClient(user['id'], user['secret'])

def get_subreddit_gallary(query):
    return client.subreddit_gallery(query, sort='time')

def is_image(item):
    return item.link.endswith('.jpg') or item.link.endswith('.png')

def get_image_url(query):
  gallary = get_subreddit_gallary(query)
  if not gallary:
    return False
  url = random.choice([item.link for item in gallary if is_image(item)])
  return url

if __name__ == "__main__":
    import sys
    print get_image_url(sys.argv[1])
