from selenium import webdriver
import telebot
import re
import urllib.request
import requests
from bs4 import BeautifulSoup
import time


def get_page(url):
	page = ''
	while page == '':
	    try:
	        response = requests.get(url)
	        break
	    except:
	        print("Connection refused by the server..")
	        print("Let me sleep for 5 seconds")
	        print("ZZzzzz...")
	        time.sleep(5)
	        print("Was a nice sleep, now let me continue...")
	        continue
	return response

def get_sector(url, soup):
	quotes = soup.find_all('td')
	sector = quotes[len(quotes)-10].text
	sector.strip()
	sector = sector.split()
	sector = ''.join(sector)
	return (sector)

ticket = input("Тикет: ")
driver = webdriver.Chrome(executable_path='chromedriver.exe')

url = 'https://finbull.ru/stock/' + ticket + '/'
driver.get(url)
description = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[2]/div[1]/div[2]')
health = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/div')
sector = driver.find_elements_by_xpath('//*[@id="css_cs_cursor"]')
rating = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]')
profitability = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[4]/div[2]/div/div[1]/div[2]/div')
pespective = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[4]/div[3]/div/div[1]/div[2]/div')
priceActual = driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[4]/div[4]/div/div[1]/div[2]/div')

response = get_page(url)
soup = BeautifulSoup(response.text, 'lxml')
sector = get_sector(url, soup)

if description:
	description = description[0].text
else:
	description = 'Не удалось получить описание компании.'
rating = rating[0].text
health = health[0].text
profitability = profitability[0].text
pespective = pespective[0].text
priceActual = priceActual[0].text


print(description)
print(f'\nСектор: {sector}\nОбщий рейтинг: {rating}\nЗдоровье компании:{health}\nПрибыльность: {profitability}\nПерспектива: {pespective}\nАктуальность цены: {priceActual}')

driver.close()
'''


def get_rating(url, soup):
	quotes = soup.find_all('td', class_='mini_bold')
	return (quotes[1].text)

def get_health(url, soup):
	if soup.find_all('div', class_='procent_line procent_line_title bcolor2_4'):
		quotes = soup.find_all('div', class_='procent_line procent_line_title bcolor2_4')
	else:
		quotes = soup.find_all('div', class_='procent_line procent_line_title bcolor2_2')
	print(quotes)
	return (quotes[0].text)

def get_profitability(url, soup):
	quotes = soup.find_all('div', class_='procent_line procent_line_title bcolor2_3')
	return (quotes[0].text)

def get_perspective(url, soup):
	quotes = soup.find_all('div', class_='procent_line procent_line_title bcolor2_4')
	return (quotes[1].text)

def get_pe_and_futurePe(url, soup):
	quotes = soup.find_all('td', class_='right_td')
	pe = quotes[13].text
	futurePe = quotes[14].text
	return pe, futurePe

ticket = input("Введите тикет компании: ")
url = 'https://finbull.ru/stock/' + ticket + '/'
response = get_page(url)
soup = BeautifulSoup(response.text, 'lxml')
sector = get_sector(url, soup)
rating = get_rating(url, soup)
health = get_health(url, soup)
profitability = get_profitability(url, soup)
pespective = get_perspective(url, soup)
pe, futurePe = get_pe_and_futurePe(url, soup)



#[<td class="right_td">17.23</td>, <td class="right_td">0.86</td>, <td class="right_td">0.02</td>, <td class="right_td">0.18</td>, <td class="right_td">10.14%</td>, <td class="right_td">10.16%</td>, <td class="right_td">4.77</td>, <td class="right_td">4.11</td>, <td class="right_td">4.5%</td>, <td class="right_td">-1.9%</td>, <td class="right_td">10.98%</td>, <td class="right_td">-20.8%</td>, <td class="right_td">12.00</td>, <td class="right_td">59.54</td>, <td class="right_td">22.61</td>, <td class="right_td">2.71</td>, <td class="right_td">6.01</td>, <td class="right_td">24.9</td>, <td class="right_td">24.85</td>, <td class="right_td">75.84</td>, <td class="right_td">5.97</td>, <td class="right_td">4.38</td>, <td class="sort wight58 right_td" data-param="PROPERTY_finviz_MARKET_CAP" data-sort="desc,nulls" style="width: 90px;">Кап,<br/>млрд$</td>, <td class="right_td">84.04</td>, <td class="right_td">92.30</td>, <td class="right_td">81.35</td>, <td class="right_td">97.27</td>, <td class="right_td">118.22</td>, <td class="right_td">552.54</td>, <td class="right_td">704.76</td>, <td class="right_td">423.86</td>, <td class="right_td">164.48</td>, <td class="right_td">59.38</td>, <td class="right_td">133.32</td>, <td class="right_td">147.52</td>, <td class="right_td">43.49</td>, <td class="right_td">0.98</td>, <td class="right_td">342.64</td>, <td class="right_td">15.18</td>, <td class="right_td">169.72</td>, <td class="right_td">27.50</td>, <td class="right_td">105.37</td>, <td class="right_td">1.90</td>]
'''