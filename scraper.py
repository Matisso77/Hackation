from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


def preatyData(tab):
    text = ""
    retTab = []
    f = 0
    if tab[-1][-1] is not '°' and tab[-1][-1] is not '%':
        for item in tab:
            text = text + " " + item
        text = text[1:]
        retTab.append(text)
        retTab.append("")
        retTab.append("")
    else:
        for item in tab:
            if item[-1] is '°' or item[-1] is '%':
                if f is 0:
                    text = text[1:]
                    retTab.append(text)
                    retTab.append(item)
                    f = 1
                else:
                    retTab.append(item)
            else:
                text = text + " " + item
    if len(retTab) < 3:
        if retTab[-1][-1] is '%':
            retTab.insert(1, '')
        else:
            retTab.append('')
    return retTab


def toDict(tab):
    dictList = []
    for item in tab:
        myDict = {
            "name": item[0],
            "promils": item[1],
            "percent": item[2],
            "priceL": item[3],
            "priceS": item[4]
        }
        dictList.append(myDict)
    return dictList


def getBeers(url):
    raw_html = simple_get(url)
    soup = BeautifulSoup(raw_html, 'html.parser')
    dataTab = []

    for p in soup.findAll("h4", {"class": "cml_shadow"}):
        tab = []
        flag = 0
        for i in p.text.split():
            if flag == 1:
                tab.append(i)
            if i == 'Brewery':
                flag = 1
        if tab:
            dataTab.append(preatyData(tab))

    i = 0
    for p in soup.findAll("div", {"class": "col-xs-5"}):
        price = p.text.split()

        if price:
            if len(price) > 2:
                try:
                    dataTab[i].append(price[2])
                except:
                    continue
            else:
                try:
                    dataTab[i].append('')
                except:
                    continue
            try:
                dataTab[i].append(price[0])
            except:
                continue

        else:
            try:
                dataTab[i].append('')
                dataTab[i].append('')
            except:
                continue

        i = i + 1

    return toDict(dataTab)

def aaa():
    raw_html = simple_get("https://ontap.pl/wroclaw/multitapy")
    soup = BeautifulSoup(raw_html, 'html.parser')
    tab = []
    for p in soup.findAll("a", {"style": "font-size: 16px; color: orange;"}):
        tmp=p.text.split()

        tab2=""
        for i in tmp:
            tab2=tab2+i+" "

        tab.append(tab2)


    return tab


def getData(url):
    raw_html = simple_get(url)
    soup = BeautifulSoup(raw_html, 'html.parser')

    sitesList = []
    for p in soup.findAll("div", {"class": "col-lg-3 col-md-4 col-xs-12 col-sm-6"}):
        sitesList.append(p["onclick"][17:-2])
    m=0
    tab=[]
    tab=aaa()
    for site in sitesList:

        print(site)
        print(tab[m])
        print(getBeers(site))
        m=m+1

getData('https://ontap.pl/wroclaw/multitapy')
