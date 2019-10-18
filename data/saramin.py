import requests
import os
import json
from bs4 import BeautifulSoup
from googleMaps import Maps
from pprint import pprint as pp

apiKey = os.environ.get("SARAMIN_KEY")
URL = "http://oapi.saramin.co.kr/job-search/?access-key={}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&job_type=1,11&count=110&fields=keyword-code".format(
    apiKey)
res = requests.get(URL).json()
print(res["jobs"]["total"] + "개 공고가 있습니다.")
for data in res["jobs"]["job"]:
    path = "companies/{}.json".format(
        data["company"]["detail"]["name"])
    if not os.path.isfile(path):  # if no data
        # init company dictionary
        company = {}

        # company data part
        company["name"] = data["company"]["detail"]["name"]
        if data["company"]["detail"].get("href"):
            company["saramin_url"] = data["company"]["detail"]["href"]
        company["ind_code"] = data["position"]["industry"]["code"]
        company["ind_name"] = data["position"]["industry"]["name"]
        company["ind_key_code"] = data["position"]["industry-keyword-code"]

        # company scrap part
        res = requests.get(company["saramin_url"])
        res = requests.get(res.url.replace("view", "view-inner-salary"))
        soup = BeautifulSoup(res.text, "html.parser")
        salary_tag = soup.find("p", "average_currency")
        if salary_tag:
            salary_str = salary_tag.text.replace(",", "").replace("만원", "")
            company["avg_salary"] = int(salary_str.strip())
        else:
            company["avg_salary"] = 0
        start_tag = soup.find("p", "salary")
        if start_tag:
            salary_str = start_tag.text.replace(",", "").replace("만원", "")
            company["start_salary"] = int(salary_str.strip())
        else:
            company["start_salary"] = 0
        res = requests.get(
            "http://www.jobkorea.co.kr/Search/?stext={}&tabType=corp&Page_No=1".format(company["name"]))
        soup = BeautifulSoup(res.text, "html.parser")
        corp = soup.find("div", "post-list-corp clear")
        if corp:
            link = corp.find("a")
            if link:
                # if link.text != company["name"]:
                #     print("[Warning] Incorrect name :",
                #           link.text, company["name"])
                res = requests.get("http://www.jobkorea.co.kr" + link["href"])
                soup = BeautifulSoup(res.text, "html.parser")
                keys = soup.find_all("div", "field-label")
                keys = [key.text for key in keys]
                containers = soup.find_all("div", "value-container")
                scrap = {}
                for key, container in zip(keys, containers):
                    if key == "대졸초임":
                        salary_tag = container.find(
                            "div", "salary-average-item")
                        if salary_tag:
                            salary = int(salary_tag.text.replace(
                                ",", "").replace("만원", ""))
                            company["start_salary"] += salary
                            company["start_salary"] //= 2
                    elif key != "계열사":
                        value = container.find("div", "value")
                        scrap[key] = value.text
                company["scale"] = scrap.get("기업구분", "")
                company["address"] = scrap.get("주소 ", "")
                company["href"] = scrap.get("홈페이지", "")
                res = requests.get(res.url[:-4] + "Salary")
                soup = BeautifulSoup(res.text, "html.parser")
                salary_tag = soup.find("div", "salary")
                if salary_tag:
                    salary_str = salary_tag.find("div", "value").text
                    salary = int(salary_str.replace(",", ""))
                    # 혹시 모를 저작권, 불법 scrap 회피 용 사람인 + 잡코리아 연봉 평균 값 사용
                    company["avg_salary"] += salary
                    company["avg_salary"] //= 2
                    # 근속연수 scrap 문제될 거 같아서 스크랩 X
                    # detail_tag = soup.find("div", "detail")
                    # company["avg_worked"] = detail_tag.find_all(
                    #     "div", "detail-item")[1].text

                # 직급별 연봉 scrap 문제될 거 같아서 스크랩 X
                # index = res.text.find(
                #     '{"PartCode":0,"PartName":"직무전체","PartSalaryAvgList":')
                # temp = res.text[index:]
                # salary_list = json.loads(
                #     temp[:temp.find("]}") + 2])["PartSalaryAvgList"]
                # # 사원, 주임, 대리, 과장, 차장, 부장, 임원
                # company["salary_rank"] = {"min": [], "avg": [], "max": []}
                # for salary in salary_list:
                #     company["salary_rank"]["min"].append(salary["Lowest_Salary_Amt"])
                #     company["salary_rank"]["avg"].append(salary["Avg_Salary_Amt"])
                #     company["salary_rank"]["max"].append(salary["Max_Salary_Amt"])

        # map part
        place = Maps.places(company["name"])
        if not place and company.get("address"):
            place = Maps.places(company["address"])
            if not place:
                place = Maps.places(company["address"].split("(")[0])
        if place:
            company["address"] = place["formatted_address"]
            company["lat"] = place["geometry"]["location"]["lat"]
            company["lng"] = place["geometry"]["location"]["lng"]
            company["viewport"] = place["geometry"]["viewport"]
            company["place_id"] = place["place_id"]
        else:
            print("[Warning] No place result :",
                  company["name"], company.get("address"))
            continue

        # json data save
        with open(path, 'w', encoding="UTF-8") as f:
            json.dump(company, f, indent="  ", ensure_ascii=False)

    # job part
    path = "jobs/{}_{}.json".format(
        data["position"]["title"].replace("/", "+"), data["opening-timestamp"])
    if not os.path.isfile(path):  # if no data
        # init job dictionary
        job = {}
        job["saramin_url"] = data["url"]
        job["title"] = data["position"]["title"]
        job["job"] = data["position"]["job-category"]["name"]
        job["exp_min"] = data["position"]["experience-level"]["min"]
        job["exp_max"] = data["position"]["experience-level"]["max"]
        job["edu_code"] = data["position"]["required-education-level"]["code"]
        job["edu_name"] = data["position"]["required-education-level"]["name"]
        job["open"] = data["opening-timestamp"]
        job["close"] = data["expiration-timestamp"]
        job["close_type"] = data["close-type"]["code"]
        with open(path, 'w', encoding="UTF-8") as f:
            json.dump(job, f, indent="  ", ensure_ascii=False)
