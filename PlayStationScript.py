import re
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open("https://account.sonyentertainmentnetwork.com/liquid/cam/media/media-list.action?filter=games&displayNavigation=false")

#for form in br.forms():
#	print form

br.select_form(nr=0)

br.form['j_username'] = '11samype@gmail.com'
br.form['j_password'] = '74p62p74p62p'

br.submit()

print(br.geturl())

soup = BeautifulSoup(br.response().read())

#print(soup.table.tbody.prettify())

pcontrol = soup.find('span', {'class':'pcontrol'}).getText()
pcontrols = pcontrol.split()

page = int(pcontrols[0])
last_page = int(pcontrols[2])

print(last_page)

items = []

while page < last_page:

	for el in soup.findAll('tr'):
		title = el.find('section', {'class':'productTitleSection'})#.getText()
		if title is not None:
			print(title.getText())
			items.append(title.getText())

	pcontrol = soup.find('span', {'class':'pcontrol'}).getText()
	pcontrols = pcontrol.split()

	page = int(pcontrols[0])
	print(page)
	
	req = br.click_link(text='Next')
	br.open(req)
	
	soup = BeautifulSoup(br.response().read())

#t_body = soup.table.tbody

#for child in t_body.descendants:
#	print(child)
