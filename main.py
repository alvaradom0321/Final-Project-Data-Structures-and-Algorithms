# Python scrape a web page using BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# If you start your own repl, click on Packages (box) on left, search for BeautifulSoup4 and add.
# On a local system, pip install urllib bs4
#Mackenzie Alvarado
import tkinter as tk
import tkinter.messagebox
from urllib.request import urlopen
from bs4 import BeautifulSoup

#word_count function
#why did we put text?
def word_count(text):
  word_frequency = {}
  words = text.split()
  for w in words:
    if w in word_frequency is not None:
      word_frequency[w] += 1
    else:
      word_frequency[w] = 1
  print(word_frequency)
  #Big0(n)

#max value and key
  max_value = max(word_frequency.values())
  print(max_value)
  max_key = max(word_frequency, key=word_frequency.get)
  print("Max key is: " + max_key)
  return max_key
#https://datagy.io/python-get-dictionary-key-with-max-value/


rootSite = ("http://citelms.net/Internships/Summer_2018/Fan_Site/")

#LinksQueue list
linksQueue = []

#VisitedLinks
visitedLinks  = []

#dictionary
myDict = {}

linksQueue.append(rootSite + "index.html")
#Big0(n)^2
while len(linksQueue) != 0:
  print("The length of LinksQueue is " + str(len(linksQueue)))
  link1 = (linksQueue[0])
  file = urlopen(link1)
  print (link1)
  linksQueue.pop(0)

  if link1 not in visitedLinks:
    visitedLinks.append(link1)
    file = urlopen(link1)
#print(file.read())
    soup = BeautifulSoup(file, 'html.parser')
# beautifulsoup makes it easy to find tags like <title>
    titletag = soup.find('title')
    print(titletag)
    print(titletag.get_text())

  # capture the URLs of links in that web page
    links = soup.find_all('a')
    myDict[titletag.text.lower()] = link1
    
    max_key = word_count(soup.text)
    myDict[max_key.lower()] = link1
    
    


  #NEXT Loop through all the matches (in C#: For each Match m in the MatchCollection returned by Matches, save the link m.Groups[1].Value):
    for link in soup.find_all('a', href = True):
    #Add rootSite + link to the LinksQueue???
    #if statement good link first and doesn't contain https or etc.
      if "http" not in link["href"] and "javascript" not in link["href"]      and "void" not in link["href"] and "png" not in link["href"] and "pdf" not in link["href"] and "collapse" not in link["href"]:
        var = link["href"]
        linksQueue.append(rootSite + var)
        print(var)
        #Big0(n)
      

#GUI

window = tk.Tk()
window.title("Web Crawler")
window.geometry("500x300")

def button1Click():
  search = entry1.get()
  search = search.lower()
  if search in myDict:
    label2.configure(text="Links that contain this word: " + myDict[search])
  else:
    label2.configure(search + " is not found in dictionary")

#search button
button1 = tk.Button(window, text="Search", 
          bg="violet", fg="black", width=7, height = 2, 
          command = button1Click)

label1 = tk.Label(window, text="Enter a word to search for:", width=25,)
label1.grid(row=1,column=1)

label2 = tk.Label(window, text="Links that contain this word:", bg="yellow")
label2.grid(row=10,column=1)

entry1 = tk.Entry(window)
entry1.grid(row=1, column=3)

button1.grid(row=2, column=3)

window.mainloop()
