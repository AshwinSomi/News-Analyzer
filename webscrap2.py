from bs4 import BeautifulSoup
import requests
link='https://www.google.com/search?q=times+of+india&rlz=1C1CHBF_enIN883IN883&tbas=0&tbs=sbd:1&tbm=nws&tbas=0&source=lnt&sa=X&ved=2ahUKEwix3aiigqnxAhWHcn0KHRKNA5QQpwV6BAgHEB4&biw=1536&bih=722&dpr=1.25'

def nextnews(link):
    htt=requests.get(link).text
    soup=BeautifulSoup(htt,'lxml')
    newss=soup.find_all('div',class_='ZINbbc xpd O9g5cc uUPGi')
    for i in newss:
        title=i.find('div',class_='BNeawe vvjwJb AP7Wnd').text.replace(',','')
        link=(i.find('a',href=True)['href'].split('/url?q=')[1]).split('&sa=U')[0]
        time = i.find('span', class_='r0bn4c rQMQod').text
        tex = i.find('div', class_='BNeawe s3v9rd AP7Wnd').text
        discrip = (tex.split("ago ")[1]).replace('.','').replace(',','')
        publisher=i.find('div',class_='BNeawe UPmit AP7Wnd').text
        print('>>',title)
        print(link)
        print(time)
        print(discrip)
        print(publisher)

        document=open('data.csv', 'a')
        document.write('{}, {}, {},{}, {}\n'.format(title, publisher ,time, discrip, link))
        document.close()

    #print(soup)
    next=soup.find('a',attrs={'aria-label':"Next page"})['href']
    link='https://www.google.com'+next
    #nextnews(link)
    #print(link)
nextnews(link)


"""tex=i.find('div',class_='BNeawe s3v9rd AP7Wnd')"""
