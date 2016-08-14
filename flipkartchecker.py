import requests, bs4
import webbrowser  #for playing song
import time
# enter url of that product which you want to track
url = "http://www.flipkart.com/rosemary-hand-held-bag/p/itme4vayc6pwjhta?pid=HMBE4VAYSRY6HE62&al=V8F%2BxdIuOjJsDCscMKlBjsldugMWZuE793A%2Fmg2RE3ZnIefskghhWVhdu%2F0hFMgEKLnE2zPGcbM%3D&ref=L%3A1374965094592825966&srno=p_1&otracker=start&ss=8230e77c24ddeabccb5a4db64561b7a9"
raw = requests.get(url)
soup = bs4.BeautifulSoup(raw.text,'html.parser')
myprice= 15000 #enter the price in which you are interested
def fetchDataAndCheckPrice(url):
	objectItem = soup.find_all("span",{"class":"selling-price omniture-field"})
	if objectItem:
		for ob in objectItem:
			price = ''.join(ob.findAll(text=True))
			print price
		price = price[4:].replace(",","") 	
		print price
		return price
	else:
		return -1
		
while 1:
	price = fetchDataAndCheckPrice(url);
	if(int(price)==-1):
		print "Sorry your wish is out of stock :("  #if item is out of stock
		break	
	elif(int(price)<myprice):
		print "Yes"
		break;
	else:
		print "No"	
		time.sleep(100)		#if price is not low run this code again after 5 seconds
	