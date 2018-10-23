#https://steemit.com/utopian-io/@ajmaln/part-1-web-scraping-using-mechanicalsoup

import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser() #StatefulBrowser instance

browser.open("http://maplestory2.nexon.net/en/news")

articles = list(browser.get_current_page().find_all('figure', class_='news-item'))[:10]

for child in articles:
	category = child.find('span', class_='news-category-tag').text
	title = child.h2.text
	link = 'http://maplestory2.nexon.net' + child.a.get('href') # Since the links are relative in the webpage, we should make it an absolute URL
	summary = child.find('div', class_='short-post-text').text# Printing the collected data
	print('Category : ' + category)
	print('Post title : ' + title)
	print('Post summary : ' + summary)
	print('Post link : ' + link)
	print()