from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import json

def get_image(id):
	url = f"https://ethiopialearning.com/content/page?id={id}"
	data = urlopen(url)
	html_byte = data.read()
	html = html_byte.decode("utf-8")
	soup = bs(html,"html.parser")
	a = soup.find_all("img")
	return (a[0]["src"])

def get_id(subject,grade,page):

	with open("data/ids.json","r") as w:
		data = json.loads(w.read())
	book_id = data[grade][subject][0]
	max_page = data[grade][subject][1]
	
	if page != 0 and page <= max_page:
		return (book_id-1) + page
	return False
