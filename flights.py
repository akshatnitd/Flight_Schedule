#!/usr/bin/python

from selenium import webdriver
import bs4
import sys
import os
from datetime import datetime


os.system('clear')


status=open('search_result.txt','a')

def results():
    src=raw_input("Enter the airport code of the source:")
    dst=raw_input("Enter the airport code of the destination:")
    jourtyp=input("Enter 1 for one-way and 2 for round trip:")
    if (jourtyp == 1):
                    strtdate=raw_input("Enter start of journey date in DD/MM/YYYY format:")
                    rtrdate=""
                    typstr="O"
    else:
                    strtdate=raw_input("Enter start date of journey in DD/MM/YYYY format:")
                    rtrdate=raw_input("Enter return date of journey in DD/MM/YYYY format:")
                    typstr="R"

    adult=input("Enter no. of adults:")
    child=input("Enter no. of children:")
    infant=input("Enter no. of infant:")
    
    if(jourtyp == 1):
        url="http://flight.yatra.com/air-search-ui/dom2/trigger?type="+str(typstr)+"&viewName=normal&flexi=0&noOfSegments="+str(jourtyp)+"&origin="+str(src)+"&originCountry=IN&destination="+str(dst)+"&destinationCountry=IN&flight_depart_date="+str(strtdate)+"&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home-pg"
    else:
        url="http://flight.yatra.com/air-search-ui/dom2/trigger?type="+str(typstr)+"&viewName=normal&flexi=0&noOfSegments="+str(jourtyp)+"&origin="+str(src)+"&originCountry=IN&destination="+str(dst)+"&destinationCountry=IN&flight_depart_date="+str(strtdate)+"&arrivalDate="+str(rtrdate)+"&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home-pg" 
   
    driver =webdriver.Chrome()
    driver.get(url)

    html2 = driver.execute_script("return document.documentElement.innerHTML;")
    soup=bs4.BeautifulSoup(html2,"lxml")
    rows=soup.findAll("articlewithbanner")
    rowlen=len(rows)
    goinglen=len(soup.select("#resultList_0 articlewithbanner"))
    cominglen=rowlen-goinglen
    flag=0
    
    print '\n\t\t\t\t\t\t\t\t\t<<<<RESULTS>>>>\n'
    status.write('\n\t\t\t\t\t\t\t\t\t<<<<RESULTS>>>>\n')
    print 'Found '+str(rowlen)+' results!'
    status.write('Found '+str(rowlen)+' results!')
    print '\n\n\n Showing results for '+str(src)+' to '+str(dst)+' on '+str(strtdate)+'\n\n\n'
    status.write('\n\n\n Showing results for '+str(src)+' to '+str(dst)+' on '+str(strtdate)+'\n\n\n')
    print "\t\tFlight Name\t\t\tDeparture\t\tArrival    \t\tDuration\t\t\t\t\tPrice(per adult)\n\n"
    status.write("\t\tFlight Name\t\t\tDeparture\t\tArrival    \t\tDuration\t\t\t\t\tPrice(per adult)\n\n")
    
    

    for row in rows:
        var_li=row.select('li')
        
        name=var_li[0].get_text(" | ", strip=True)
        
        time=var_li[1].select('div')
        depart=time[0].get_text(" | ", strip=True)
        arrival=time[1].get_text(" | ", strip=True)
        duration=time[2].get_text(" | ", strip=True)
        
        price=""
        price_div=var_li[5].select('div')
        
        if(jourtyp==1):
            price_label=price_div[0].select('label')
            if len(price_label)>0:
                price_del=price_label[0].select('del')
                price=price_del[0].get_text("", strip=True)
        
        else:
            price_p=price_div[1].select('p')
            if len(price_p)>0:
                price_span=price_p[0].select('span')
                price=price_span[0].get_text("", strip=True)
            
        if(len(price)>4):
            ans=str("\t\t"+name+"\t\t"+depart+"\t\t"+arrival+"\t\t"+duration+"\t\t\t"+price+"\t\t")
            print str(ans)
            status.write (ans)
            
            
            if(goinglen>0):
                goinglen=goinglen-1
                
            print '-----------------------------------------------------------------------------------------------------------------------------------------------------------------------'
            status.write ('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            if(goinglen==0)and(flag==0)and(jourtyp==2):
                print '\n\n\n Showing results for '+str(dst)+' to '+str(src)+' on '+str(rtrdate)+'\n\n\n'
                status.write('\n\n\n Showing results for '+str(dst)+' to '+str(src)+' on '+str(rtrdate)+'\n\n\n')
                print "\t\tFlight Name\t\t\tDeparture\t\tArrival    \t\tDuration\t\t\t\t\tPrice(per adult)\n\n"
                status.write("\t\tFlight Name\t\t\tDeparture\t\tArrival    \t\tDuration\t\t\t\t\tPrice(per adult)\n\n")
                flag=1
            else:
                    cominglen=cominglen-1
    driver.close()
    
    
results()        
print "\n\n\nSearch Reults as on  "+str(datetime.now())+"\n\n\n\n"

status.close()

