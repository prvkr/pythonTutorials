import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#soldByThirdParty > span.a-size-medium.a-color-price.inlineBlock-display.offer-price.a-text-normal.price3P')
    return elems[0].text.strip()



price = getAmazonPrice('https://www.amazon.in/Automate-Boring-Python-Albert-Sweigart/dp/1593275994/ref=sr_1_2?ie=UTF8&qid=1530080985&sr=8-2&keywords=automating+the+boring+stuff')
print('The price is ' + price)
