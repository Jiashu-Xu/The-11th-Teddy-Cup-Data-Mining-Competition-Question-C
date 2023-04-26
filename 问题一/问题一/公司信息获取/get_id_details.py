import json

import requests
from lxml import etree
import csv
import time



def get_source(id):
    url = 'https://www.5iai.com/api/enterprise/job/public?id={}'.format(id)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    html = res.text
    return html
def get_info(index,html):
    try:
        lis_data = []
        json_data = json.loads(str(html))
        id = json_data['data']['id']  #招聘信息id
        enterpriseName = json_data['data']['enterpriseName'] #企业名称
        positionName = json_data['data']['positionName']  #招聘岗位

        minimumWage = json_data['data']['minimumWage']  # 最低工资
        maximumWage = json_data['data']['maximumWage']  # 最高工资
        leixing = json_data['data']['willNature'] # 工作类型  0：实习，2：全职
        education = json_data['data']['educationalRequirements'] # 学历要求  0：不限学历，1：技工，2：大专，3：本科
        exp = json_data['data']['exp']  # 工作经验要求
        count = json_data['data']['count'] # 招聘人数  0：不限人数 

        keywordList = json_data['data']['keywordList']
        keywords = []  
        if len(keywordList)!=0:
            for keyword in keywordList:
                labelName = keyword['labelName']  # 职位关键词
                labelId = keyword['labelId'] 
                s = labelName+','+labelId+','
                keywords.append(labelName)
        else:
            keywords.append('无')

        skillsList = json_data['data']['skillsList']
        skills = []  #技能关键词，id
        if len(skillsList) !=0:
            for skill in skillsList:
                skill_labelName = skill['labelName']
                skill_labelId = skill['labelId']
                ss = skill_labelName+","+skill_labelId+","
                skills.append(skill_labelName)
        else:
            skills.append('无')


        welfare = json_data['data']['welfare']    # 职位福利
        detailedAddress = json_data['data']['enterpriseAddress']['detailedAddress'] # 工作地点

        jobRequiredments = json_data['data']['jobRequiredments'] # 职位描述




        print(id,enterpriseName,positionName,minimumWage,maximumWage,leixing,education,exp,count,keywords,skills,welfare,detailedAddress,jobRequiredments)
        print("-----------------------")
        lis_data.append([index,id,enterpriseName,positionName,minimumWage,maximumWage,leixing,education,exp,count,keywords,skills,welfare,detailedAddress,jobRequiredments])

        with open('data/result1-1(2).csv', 'a+', encoding='utf-8', newline='') as csvFile:
            for rows in lis_data:
                csv.writer(csvFile).writerow(rows)



    except:
        pass



def reads_txt():
    f=open('id_list.txt')
    data = f.readlines()  # 直接将文件中按行读到list里，效果与方法2一样
    f.close()  # 关
    print(data) #返回list
    return data

if __name__ == '__main__':
    with open('data/result1-1(2).csv', 'a+', encoding='utf-8', newline='') as csvFile:
        csv.writer(csvFile).writerow(['序号','招聘信息id','企业名称','招聘岗位','最低工资','最高工资','工作类型','学历要求','工作经验要求',
                                      '招聘人数','职位关键词(职位关键词id)','技能关键词(技能关键词id)','职位福利','工作地点','职位描述','公司类型','岗位数量'])
    csvFile.close()
    ids = reads_txt()
    for index,id in enumerate(ids):
        print("爬取第{}个,id为{}".format(index+1,id))
        print("-----------------------------------")
        res = get_source(id.strip())
        get_info(index+1,res)





