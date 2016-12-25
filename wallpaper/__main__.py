import desktop
import imgur
import urllib
import random
import os, re, sys

def purge(dir, pattern):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))

def url_to_file(url, name):
  f = open(name, 'wb')
  f.write(urllib.urlopen(url).read())
  f.close()

def main():
  if os.getuid() != 0:
    sys.exit("i need to run as sudo 😐")
  if len(sys.argv) >= 2:
    query = sys.argv[1]
  else:
    query = 'natureporn'
  desktop_location = "/Library/Desktop Pictures/"
  purge(desktop_location, "reddit")
  image_name = desktop_location + "reddit" + str(random.random())[2:] + '.jpg'
  url = imgur.get_image_url(query)
  url_to_file(url, image_name)
  desktop.set_background(image_name)
