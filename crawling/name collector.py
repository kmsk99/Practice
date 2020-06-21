import urllib.request
from bs4 import BeautifulSoup
 
mbtis = ["enfj", "enfp", "entj", "entp", "esfj", "esfp", "estj", "estp", "infj", "infp", "intj", "intp", "isfj", "isfp", "istj", "istp"]

for mbti in mbtis:
    url = "https://www.idrlabs.com/{}.php".format(mbti)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req).read()
    
    soup = BeautifulSoup(res,'html.parser')
    keywords = soup.find_all('h3',class_='type-person-name')
    keywords = [each_line.get_text().strip() + "\n" for each_line in keywords[:]]

    a = open('{}.txt'.format(mbti), mode='wt', encoding='utf-8')
    a.writelines(keywords)
    a.close()

    print(keywords)
