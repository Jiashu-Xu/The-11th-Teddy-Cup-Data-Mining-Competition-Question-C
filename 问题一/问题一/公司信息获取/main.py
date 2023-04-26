import requests
import pandas as pd
import json

data = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

def print_hi(page):
    url = f'https://www.5iai.com/api/enterprise/job/public/es?pageSize=10&pageNumber={page}' \
          '&willNature=&function=&wageList=%255B%255D&workplace=&keyword='
    response = requests.get(url, headers=headers)
    html = json.loads(response.text)
    for i in html["data"]["content"]:
        item = {'招聘信息id': i["id"], '公司地址': i["enterpriseAddress"]["detailedAddress"].replace('\xa0', ''),
                '岗位名称': i["positionName"], '公司类型': i["enterpriseExtInfo"]["personScope"],
                '最低薪资': i["minimumWage"], '最高薪资': i["maximumWage"],
                '岗位数量': i["enterpriseExtInfo"]["econKind"], '学历要求': i["educationalRequirements"],
                '岗位经验要求': i["exp"], '企业名称': i["enterpriseExtInfo"]["shortName"]}
        print(item)
        data.append(item)


def main():
    for j in range(1, 159):
        print_hi(page=j)
    df = pd.DataFrame(data)
    df1 = pd.DataFrame(range(1, len(df)+1), columns=['序号'])
    pd.concat([df1, df], axis=1).to_csv('data/result1-1(1).csv', encoding='utf-8-sig', index=None)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

