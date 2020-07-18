import requests, sys, webbrowser, bs4


def searchG(inpt):
    # res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))  #create request
    res = requests.get('https://google.com/search?q='+''.join(inpt))  #create request
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    linkElements = soup.select('.r a')
    linkToOpen = min(3, len(linkElements))  # HOW MENY LINKS YOU WANT TO OPEN
    for i in range(linkToOpen):
        webbrowser.open('https://google.com'+linkElements[i].get('href'))
    
    return (inpt)

searchG(input('Enter about DIU : \n'))



