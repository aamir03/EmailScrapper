# importing modules
import re
import requests
from bs4 import BeautifulSoup
# Scraping Results
ui="applicant tracking system blog"
srch=requests.get("https://www.google.com/search?q="+ui)
soup=BeautifulSoup(srch.text,'html.parser')
srch_results=soup.select('.kCrYT a') # seraching a tag in class .kCrYT
# print(srch_results)
# Lists for storing final results
n=[]
m=[]

for link in srch_results:
    hreflink=link.get('href')
    # Checking if url contains word "Blog"
    if hreflink.find("blog")==-1:
        print("No Blog Word Found")
    else:
        word=[]
        word.append(hreflink)
        res = [str(sub.split('/url?q=')[1]) for sub in word] 
        # print("Yes")
        # print((res))
        for lnk in res:
            r=requests.get(lnk)
            htm=r.content
            # print(lnk)
            myfindword="Applicant Tracking System"
            newmyfindword=myfindword.lower()
            mynewsoup=BeautifulSoup(htm,'html.parser')
            # Checking if Web pages have word "Applicant Tracking System"
            if mynewsoup.find(newmyfindword)==-1:
                print("No Applicant Tracking System Word found")
            else:
                # Scraping Emails of website which contains blog word in url and ATS in webpage
                EMAIL_REGEX=r"[\w\.-]+@[\w\.-]+com"
                for rematch in re.findall(EMAIL_REGEX,r.text):
                    # print(rematch)
                    m.append(lnk)
                    n.append(rematch)
print(n)
print(m)
# Storing data in text file
with open('result.txt', 'w') as f:
    for (item1,item2) in zip(m,n):
        f.write("link:- "+item1+"\n"+"Emails:- "+item2+"\n")                    
                    
                
                                


        
