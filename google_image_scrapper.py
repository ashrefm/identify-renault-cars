import os
import time
import sys
import urllib
import shutil
import re

def get_raw_html(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page    
        except:
            return"Page Not found"
  
        
'''def next_link(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('class="rg_di')
        start_content = s.find('imgurl=',start_line+1)
        end_content = s.find('&amp;',start_content+1)
        content_raw = str(s[start_content+7:end_content])
        return content_raw, end_content
         
    

def get_links(page, nmax=1000):
    links = []
    counter = 0
    while True:
        link, end_content = next_link(page)
        if link == "no_links" or counter >= nmax:
            break
        else:
            links.append(link)      #Append all the links in the list named 'Links'
            #time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
            counter +=1
    return links'''

    
def download_images(links, search_keyword, save_dir, nmax):

    '''choice = input("Do you want to save the links? [y]/[n]: ")
    if choice=='y' or choice=='Y':
        #write all the links into a test file. 
        f = open('links.txt', 'a')        #Open the text file called links.txt
        for link in links:
            f.write(str(link))
            f.write("\n")
        f.close()   #Close the file'''
    '''num = input("Enter number of images to download (max 100): ")'''
    counter = 1
    search_keyword = search_keyword.replace("%20","_")
    directory = save_dir+search_keyword+'/'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for link in links:
        if counter<=int(nmax):
            file_extension = link.split(".")[-1]
            filename = directory + search_keyword.lower() + "_" + str(counter) + "."+ file_extension
            print(str(counter)+'/'+str(nmax))
            #urllib.urlretrieve(link, filename)
            try :
                req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
                shutil.copyfileobj(urllib.request.urlopen(req), open(filename, 'wb'))
            except:
                pass
            
        counter+=1


def search():
    
    t0 = time.time()   #start the timer
    search_keywords = input("Enter the search query: ")
    
    for keyword in search_keywords.split():
        print('Looking for '+keyword+'...\n')
        #Download Image Links
        #links = []
        keyword = keyword.replace(" ","%20")
        url = 'https://www.google.com/search?q=' + keyword + '&tbas=0&tbs=isz:m&tbm=isch&tbas=0&source=lnt&sa=X&ved=0ahUKEwi9oL63yKrWAhXIaRQKHW_HBjsQpwUIHA&biw=1920&bih=947&dpr=1'
        raw_html =  (get_raw_html(url))
        open('./Web Scrapping/raw_html_'+keyword+'.txt', 'a').write(raw_html)
    
        #links = links + (get_links(raw_html, nmax=10))
        links = re.findall("\"http[^\"]*\.jpg\"", raw_html)
        links = [re.sub("\"", "", x) for x in links]
        print("Total Image Links = "+str(len(links)))
        print("\n")
    
        download_images(links, keyword, save_dir='./Web Scrapping/', nmax=len(links))

    t1 = time.time()    #stop the timer
    total_time = t1-t0   #Calculating the total time required to crawl
    print("Total time taken: "+str(total_time)+" Seconds")


if __name__ == '__main__':
	search()


    
    
    






