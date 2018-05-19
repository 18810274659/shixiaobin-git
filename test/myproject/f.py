from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
def ngrams(input, n):
	input = input.split(' ')
	output = []
	for i in range(len(input)-n+1):
		output.append(input[i:i+n])
	return output
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-grams count is: "+str(len(ngrams)))
