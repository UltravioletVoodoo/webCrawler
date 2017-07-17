import requests
from bs4 import BeautifulSoup


url = "https://www.ece.uvic.ca/~panagath/ELEC360/ELEC360.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("h3") #The HTML tag to search for

for DATA in data:
	if "Assignment #" in str(DATA):
		print str(DATA.text)
		
		
		
exiter = raw_input("press any key to continue")


