#Devs make way to many jokes about bugs, so let's see just how many reddit holds
#Demonstration purposes only
import urllib.request
import html.parser

class linkRetrieval(html.parser.HTMLParser):
    def getLinks(self,link,count):
        self.next=link
        self.list=[]
        
        for i in range(count):
            request = urllib.request.Request(self.next,headers={"User-Agent":"Magic Browser"})
            request = str(urllib.request.urlopen(request).read())
            self.feed(request)
        return self.list
    def handle_starttag(self,tag,attrs):
        if tag=="a":
            for att in attrs:
                if(att[0]=="class"):
                    temp=att[1]
                    if("comments" in temp):
                        for att in attrs:
                            if(att[0]=="href"):
                                self.list.append(att[1])
                if (att[0]=="href"):
                    if("https://old.reddit.com/r/ProgrammerHumor/top/" in att[1]):
                        self.next=att[1]
class commentRetrieval(html.parser.HTMLParser):
    def getComments(self,links):
        self.currentComment=""
        self.comments=[]
        
        for i in links:
            self.Record=False
            try:
                request = urllib.request.Request(i,headers={"User-Agent":"Magic Browser"})
                request = str(urllib.request.urlopen(request).read())
                self.feed(request)
            except:
                print("error")
        return self.comments
    def handle_starttag(self,tag,attrs):
        if tag=="div":
            for att in attrs:
                if att[0]=="class":
                    if att[1]=="md":
                        self.Record=True
                        self.currentComment=""
    def handle_data(self,data):
        if(self.Record==True):
            self.currentComment += data
    def handle_endtag(self,tag):
        if tag=="div":
            if self.Record==True:
                self.Record=False
                self.comments.append(self.currentComment)
linkGetter = linkRetrieval()
links = linkGetter.getLinks("https://old.reddit.com/r/ProgrammerHumor/top/",10)

commentGetter=commentRetrieval()
data =commentGetter.getComments(links)

print(data)
x=0
for i in data:
    if "bug" in i:
        x+=1
print(x)
        





