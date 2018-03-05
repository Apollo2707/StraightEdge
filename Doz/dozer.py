import urllib3
import json
debug = False
count = 0 
def getRawData(url):
	global debug
	http = urllib3.PoolManager()
	r = http.request('GET',url)
	html = str(r.data)
	if (debug):
		print(html)

def getJson(url):
	global debug
	http = urllib3.PoolManager()
	r = http.request('GET',url)
	html = str(r.data)
	html = json.loads(r.data)
	if(debug):
		print (html)
	return html 

def parseRedditCommentsByUser(username):
  count = 0
  run = True
  data = getJson("https://www.reddit.com/user/" + username + "/comments.json?limit=100")
  for x in data["data"]["children"]:
    count += 1
    comment = x["data"]
    #print(comment["subreddit"])
    #print(comment["body"])
  tail = ""
  
  
  while (run):
    if(tail == data["data"]["children"][-1]["data"]["name"]):
      break
    tail = data["data"]["children"][-1]["data"]["name"]
    data = getJson("https://www.reddit.com/user/" + username + "/comments.json?limit=100&after="+ tail)
    if(data["data"]["children"].count == 0):
      break
    for x in data["data"]["children"]:
      count += 1
      comment = x["data"]
      print (str(count))
      print(comment["subreddit"])
      print(comment["body"])
		  
parseRedditCommentsByUser("shady2707")
