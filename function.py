#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import requests
import bs4


def find_google(q):
    url = 'https://google.com/search?q=' + q
    
    request_result = requests.get( url )
      
    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")
                  
    heading_object = soup.find_all( 'h3' )
    
    heading_object=soup.find_all("div", {'data-attrid': 'wa:/description'})
    heading_object=soup.select('div["data-attrid":"wa:/description"]')
    
    texts = []
    for info in heading_object:
        texts.append(info.getText())
    
    text = str.join("</br>", texts)

    return { 'message': text }
    
    
def find_wikipedia(q):
    url = 'https://pt.wikipedia.org/w/index.php?search=' + q + \
        '&title=Especial%3APesquisar&profile=advanced&fulltext=1&ns0=1&searchengineselect=mediawiki'

    request_result = requests.get( url )
      
    soup = bs4.BeautifulSoup(request_result.text,
                             "html.parser")
                  
    heading_object = soup.select_one('.mw-search-result')

    a = heading_object.find('a')
    href = a.get('href')
    resu = a.getText()
    titl = heading_object.select_one('.searchresult').getText()
    text = 'Hum... acho que já li sobre isso aqui:<br><a href="https://pt.wikipedia.org' + str(href) + '">' + \
        str(resu) + '</a><br>' + titl

    return { 'message': text }    
    

def main(dict):
    q = dict.get('query','')
    return find_wikipedia(q)
