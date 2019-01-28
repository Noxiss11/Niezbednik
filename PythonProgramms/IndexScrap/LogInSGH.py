from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import re

driver = webdriver.Firefox()




def LogInSGH():
    
    driver.get('https://www.e-sgh.pl/niezbednik/logowanie.php')

    #providing the login
    login = driver.find_element_by_name('login')
    login.send_keys('kj78081')

    #providing the password
    password = driver.find_element_by_name('password')
    password.send_keys('dAWbl2^2i6du8')

    logbutton = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/button')
    logbutton.click()

def GoToInz():

    subject = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[2]/div[9]/h4/a')
    subject.click()

    grupa = driver.find_element_by_xpath('/html/body/div[2]/div/nav/ul/li[3]/a')
    grupa.click()



LogInSGH()
#GoToInz()



global link
link=('https://www.e-sgh.pl/niezbednik/grupa.php?pid=9347')
#links =input('provide the link')

def getdata():

    #for link in links:

        driver.get(link)
        
        grupa = driver.find_element_by_xpath('/html/body/div[2]/div/nav/ul/li[3]/a')
        grupa.click()


        elem = driver.find_element_by_xpath('//*')
        source = elem.get_attribute('outerHTML')


        page_soup = soup(source,'html.parser')

        names = page_soup.findAll('li', id = re.compile('list'))
        code = page_soup.findAll('li')

        path = link + '&'

    ##    file = open('Inekst.csv','a')
        

        for a in names:
            
            file = open('Inekst.csv','a')
           

            #names = page_soup.findAll('tr', {'class':'profil'})
            start = int(str(a).find('show='))
            show = str(a)[start:start+10]
    ##        print(path+show)
            driver.get(path + show)
    ##        print('niew')
            elem2 = driver.find_element_by_xpath('//*')
            source2 = elem2.get_attribute('outerHTML')
            page_soup2 = soup(source2,'html.parser')

    ##        print(page_soup2)

            

            
            indeks = page_soup2.findAll('td')
    ##        print(indeks)
    ##        space = a.text.strip().find(' ')
    ##        person = a.text.strip()
    ##        name = person[0:space-1]
    ##        lastname = person[space+1:len(person)]

            lineOftxt = ''
            for td in indeks:
                lineOftxt = lineOftxt + ' , ' + str(td.text.rstrip())
            lineOftxt = lineOftxt + '\n'
            file.write(lineOftxt)
            lineOftxt = None
            
        file.close()



getdata()