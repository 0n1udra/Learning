from urllib.request import urlopen
from bs4 import BeautifulSoup as soup


graphicsCardURL = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
# link of website

uClient = urlopen(graphicsCardURL)
# opens connection to site
pageHTML = uClient.read()
# gets the html from site and saves it in a var. one long string
uClient.close()
# closes connection from website

pageSoup = soup(pageHTML, "html.parser")
# parses html with soup(bs4)

#product
containers = pageSoup.findAll("div", {"class": "item-container"})
# grabs each product(knows it works on graphics card)

def pricing(product):
    return product.div.find("div", {"class": "item-action"}).ul.find("li", {"class": "price-current"}).strong.get_text() +\
            product.div.find("div", {"class": "item-action"}).ul.find("li", {"class": "price-current"}).sup.get_text()
    # gets the price from: div item-container > div item-info > div item-action > ul price has-label-membership > li price-current

print(len(containers), "Products found.")
# prints how many objects(products it found on pave)
#print(containers[0])
# prints first object, i did this to see the code and see what i need more specifiably. I use http://jsbeautifier.org to make code look better

for product in containers:
    brand = product.div.div.a.img["title"]
    title = product.a.img["title"]

    try:
        price = pricing(product)
    except:
        print("Can't get price for", title)
        price = 0

    # features of graphics card
    #features = {item.split(":") for item in [li.get_text() for li in product.div.ul.findAll("li")]}
    features = [li.get_text() for li in product.div.ul.findAll("li")]
    #featurs = {item.split(":") for item in features}
    for item in features:
        print(item)
    #print(featurs)
    # for li in product.div.ul.findAll("li"):
    #     features.append(li.get_text())
    # features are in a html ul/li format, and there stored with <strong> tag. this is a loop to get all the features with get_text() function

    #print("Name: {}, Price: {}, Features: {}".format(title, price, features))




if __name__ == "__main__":
    print("Loaded.")
else:
    print("Imported.")
