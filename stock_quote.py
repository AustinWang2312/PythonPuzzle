import urllib.request
import re

def get_quote(symbol):
	base_url = 'http://finance.google.com/finance?q='
	with urllib.request.urlopen(base_url + symbol) as url:
		content = url.read().decode()
#		print (content)
	#m = re.search(r'\id="ref_694653_l".*?>(.*?)\<', content)
#		m = re.search('\="price"(.*?)\/', content)
#		m= re.search('\id="ref_12607212_l">(.*?)\<',content)

		price= re.search('\_l">(.*?)\<',content)
		net= re.search('\_c">(.*?)\<',content)
		percent= re.search('\_cp">(.*?)\<',content)
#		m = re.search('\content="(.*)\"', content)
#		m = re.search(r'\<met"(.*?)\=', content)
		
#	print(m)
	if price:
		price1 = price.group(1)
		net1=net.group(1)
		percent1=percent.group(1)
		print (price1, net1, percent1)
	else:
		price = 'no quote available for: ' + symbol
#	return price
symbol=input("What is the company symbol")
get_quote(symbol)


#content = urllib.request.urlopen(base_url + symbol).read().decode()
