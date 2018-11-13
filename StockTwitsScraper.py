import requests
import pprint
import json
import csv
import time
from datetime import date


class Post:
    id = 0
    sentiment = ""
    PostBody = ""
    ticker = ""

pp = pprint.PrettyPrinter(indent=4)

filename = "output/" + str(date.today()) + '.csv'
with open(filename, mode='w') as nfile:
    writer = csv.writer(nfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(filename)

PrevPosts = {"AMD":[], "TLRY":[], "MU":[], "BABA":[], "IQ":[], "JD":[], "TCEHY":[], "APRN":[]}
CurrPosts = {"AMD":[], "TLRY":[], "MU":[], "BABA":[], "IQ":[], "JD":[], "TCEHY":[], "APRN":[]}

for timesQueried in range(0, 30):
    for key in PrevPosts:
        NumBullsih = 0
        NumBearish = 0
        
        r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/"+key+".json")
        JsonResponse = r.json()
        for post in JsonResponse['messages']:
            # Check if post has been previously found
            PrevUsedPost = False
            oldPosts = 0
            newPosts = 0
            for PrevPost in PrevPosts[key]:
                if PrevPost.id == post["id"]:
                    newPosts += 1
                    PrevUsedPost = True
                else:
                    oldPosts += 1
            if not PrevUsedPost:
                PostObj = Post()
                PostObj.id = post["id"]
                CurrSentiment = post['entities']['sentiment']
                if CurrSentiment != None:
                    PostObj.PostBody = post["body"]
                    PostObj.ticker = key
                    if CurrSentiment['basic'] == "Bullish":
                        NumBullsih += 1
                        PostObj.sentiment = "Bullish"
                    elif CurrSentiment['basic'] == "Bearish":
                        NumBearish += 1 
                        PostObj.sentiment = "Bearish"
                    CurrPosts[key].append(PostObj)
        
        PrevPosts[key] = CurrPosts[key].copy()
        CurrPosts[key].clear()

    # # write to csv with date and time
    # for ticker in PrevPosts:
    #     print("\n Numeber of posts in",ticker,"is",len(PrevPosts[ticker]),"\n")

    time.sleep(120)
    
    with open(filename, mode='a') as nfile:
        writer = csv.writer(nfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for ticker in PrevPosts:
            for post in PrevPosts[ticker]:
                writer.writerow([post.id, post.ticker, post.sentiment, post.PostBody])
                # print(post.id, post.ticker, post.sentiment, post.PostBody)
            # print("\n Numeber of posts in",ticker,"is",len(PrevPosts[ticker]),"\n")


    