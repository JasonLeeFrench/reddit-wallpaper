import desktop
import imgur
import urllib
import random
import os, re, sys
import json

config = json.load(open(os.path.join(os.path.dirname(__file__), 'config/config.json')))

def write_to_file(location, image_name, url):
  try:
    purge(location, "reddit")
  except:
    sys.exit("can't delete old reddit desktop pictures! please run me as sudo, or change file permissions on %s" %location)
  try:
    write(url, image_name)
  except:
    sys.exit("can't write new reddit desktop picture! please run me as sudo, or change file permissions on %s" %location)

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
          os.remove(os.path.join(dir, f))

def write(url, name):
  f = open(name, 'wb')
  f.write(urllib.urlopen(url).read())
  f.close()

def main():
  if len(sys.argv) >= 2:
    query = sys.argv[1]
  else:
    query = config['default_subreddit']
  desktop_location = config['desktop_location']
  image_name = desktop_location + "reddit" + str(random.random())[2:] + '.jpg'
  url = imgur.get_image_url(query)
  write_to_file(desktop_location, image_name, url)
  desktop.set_background(image_name)