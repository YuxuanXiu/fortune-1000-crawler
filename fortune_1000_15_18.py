# -*- coding: utf-8 -*-
# Fortune 1000 grabber. Download and parse companies information

# Import libraries
# Original code used python 2.7. I did it using python 3.6. Also, this code works for the current website.
# Also. I added a little more meta-data.
# last checked : 8th Spetember, 2017

from json import JSONDecodeError
import urllib.request
import json
import unicodecsv

dict_api_code = {'2015': '1141696', '2016': '1666518', '2017': '2013055', '2018': '2358051'}

class Company:
    ranking = 0
    fullname = ""
    ticker = ""
    industry = ""
    sector = ""
    hqlocation = ""
    hqaddr = ""
    website = ""
    yearsonlist = 0
    ceo = ""
    eps = 0
    employees = 0
    mktval=0
    global500rank = 0
    revenues = 0
    revchange = 0.0
    profits = 0
    prftchange = 0.0
    hqstate = ""
    hqzip = ""

def grab(year_code):
    # Obtaining post id
    companies = []

    # Fetch for pages with data and process JSONs
    for i in range(0, 1000, 100):
        page_url = "http://fortune.com/api/v2/list/" + year_code + "/expand/item/ranking/asc/{postid}/{index}/".format(postid=str(i), index=str(100))

        try:
            page_data = json.loads(urllib.request.urlopen(page_url).read().decode('utf-8'), encoding='utf-8')

            for item in page_data["list-items"]:
                company = Company()
                try:
                    company.ranking = item["meta"]["ranking"]
                    company.fullname = item["meta"]["fullname"]
                    # company.ticker = item["meta"]["ticker"].upper()
                    company.industry = item["meta"]["industry"]
                    company.sector = item["meta"]["sector"]
                    company.hqlocation = item["meta"]["hqlocation"]
                    company.hqaddr = item["meta"]["hqaddr"]
                    # company.yearsonlist = item["meta"]["yearsonlist"]
                    company.ceo = item["meta"]["ceo"]
                    # company.eps = item["meta"]["eps"]
                    # company.employees = item["meta"]["employees"]
                    # company.revenues = item["meta"]["revenues"]
                    # company.profits = item["meta"]["profits"]
                    # company.hqzip = item["meta"]["hqzip"]
                    company.website = item["meta"]["website"]
                    # company.mktval = item["meta"]["mktval"]
                    # company.global500rank = item["meta"]["global500-rank"]
                    # company.revchange = item["meta"]["revchange"]
                    # company.prftchange = item["meta"]["prftchange"]
                    # company.hqstate = item["meta"]["hqstate"]
                except KeyError:
                    print("Keyerror has occurered for " + str(company.fullname))

                print(str(company.ranking) + ". " + str(company.fullname) + " ; " + str(company.ceo))

                companies.append(company)
        except JSONDecodeError:
            print(str(i) + " to " + str(i+100) + " has JSONDecodeError.")

    return companies


if __name__ == "__main__":
    for i in range(2015, 2019):
        year_code = dict_api_code[str(i)]
        # Obtain companies
        companies = grab(year_code)
        f = open("fortune1000-" + str(i) + ".csv", "wb")

        try:
            # writer = csv.writer(f)
            writer = unicodecsv.writer(f, encoding='utf-8')
            writer.writerow(
                ("ranking", "full name", "ceo", "sector", "industry", "hq location", "hq address",
                 "website"))
            for company in companies:
                writer.writerow((company.ranking, company.fullname, company.ceo, company.sector, company.industry,
                                 company.hqlocation, company.hqaddr, company.website))
        finally:
            f.close()