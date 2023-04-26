import json

import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv
import time

def get_html(url):
    header = {
        "Cookie":"DEFAULT_ENTERPRISE_IMG=company.jpg; APP_HEADER_NAME=%E6%B3%B0%E8%BF%AA%E5%86%85%E6%8E%A8; APP_TITLE=%E6%B3%B0%E8%BF%AA%E5%86%85%E6%8E%A8; APP_RESOURCE_SCOPE_NAME=%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83; APP_HELP_DOC_URL=http://45.116.35.168:8083/eb; REGISTER_URL=http://www.5iai.com:444/oauth/register",
        "Referer": "https://www.5iai.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=header).text
    return res
def getids2txt(res):
    json_data = json.loads(str(res))
    contents = json_data['data']['content']
    print(contents)
    with open("id_list.txt", "a+", encoding='utf-8') as f:
        for content in contents:
            id = content['id']
            f.write(id+'\n')
            print(id)



if __name__ == '__main__':
    for page in range(1, 158):

        url = 'https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber={}&willNature=&function=&wageList=%5B%5D&workplace=&keyword='.format(page)
        resposn = get_html(url)
        getids2txt(resposn)


