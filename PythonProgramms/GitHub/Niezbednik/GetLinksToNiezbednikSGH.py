from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
import sqlite3 as sql
import os
import time
db = sql.connect('Niezbednik.db')
c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS Niezbednik(ID INTEGER PRIMARY KEY,PID INTEGER,Link TEXT,Przedmiot TEXT)')

number = '5999'
my_url = 'https://www.e-sgh.pl/niezbednik/karta_zgloszeniowa.php?pid='
start = 7595
end = 12000

# b =10
# for a in range(b):
	# os.system('clear')
	
	# print(str(round((a+1)/b,2)*100)  + ' % downloaded' + ' ' + str(round((a+1)/b*25)* '|' ))
	# time.sleep(1)
	#os.system('clear')
	#print(int(round((a+1/b)*20)), "downloaded")

for pid in range(start,end):
	uClient = uReq(my_url+str(pid))
	page_html = uClient.read()
	uClient.close()
			#print(my_url)
	page_soup = soup(page_html, "html.parser")
	definition_container = page_soup.findAll("h1")

	c.execute('INSERT INTO Niezbednik(PID, Link, Przedmiot) values(?,?,?)',(pid,my_url + str(pid), definition_container[0].text.strip()))
	db.commit()
	print("Added " + str(pid) + str(pid-start+1) + ' of ' + str(end-start) + ' ' + str(round((pid-start+1)/(end-start) *100,2)) + '%')
	# os.system('clear')
	
	# print(str(round((pid+1-start)/end,2)*100)  + ' % downloaded' + ' ' + str(round((pid+1-start)/end*25)* '|' ))
	# time.sleep(1)
print('Done')