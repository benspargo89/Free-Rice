import json
import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as soup

def get_words(word):
	words = []
	search = f'https://api.datamuse.com/words?ml={word}'
	request = requests.get(search)
	for answer in json.loads(request.text):
		words.append(answer['word'])
	return words

def extract_words():
	words = []
	while len(words) != 4:
		html = driver.page_source
		page_soup = soup(html, 'html.parser')
		word = page_soup.find_all("div", {"class": "card-title"})[0].text.split()[0]
		words = [entry.text for entry in page_soup.find_all("div", {"class": "card-button fade-appear-done fade-enter-done"})]
	return word, words


def parse():
	word, words = extract_words()
	answer_set = get_words(word)
	print(words)
	if len(words) == 0:
		print(html)
	for i, w in enumerate(words):
		for w2 in w.split():
			if w2 in answer_set:
				driver.find_element_by_xpath(f"//*[text()='{w}']").click()
				return 
	driver.find_element_by_xpath(f"//*[text()='{w}']").click()
	return 

url = f"https://freerice.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/button').click()
sleep(2)
html = driver.page_source

	
while True:
	parse()
	
