import concurrent.futures
from venv import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Get_info import get_info
from DB import *

def removeIfDuplicate(data):
    tmp = []
    for i in data:
        if i not in tmp:
            tmp.append(i)
        else:
            continue
    return tmp


def craw_company_info():
    links = ['https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=7&page=2&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=13&occupation_ids%5B%5D=13&page=2&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=18&page=2&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=12&page=4&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=26&page=2&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=8&page=2&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=3&page=2&sort_q=',
             'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=21&page=2&sort_q=']
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    try:
        id = 1
        for link in links:
            with webdriver.Chrome(options=chrome_options) as driver:        
                elements = get_info(driver, 5, link)
                elements = list(filter(None, elements)) # filter none element

                companyInfo = []
                rankInfo = []
                
                for element in elements:
                    tmp = []
                    tmp.append(element[0])
                    tmp.append(element[1])
                    rankInfo.append(element[2])
                    companyInfo.append(tmp.copy())
                    
                companyInfo = removeIfDuplicate(companyInfo)
                rankInfo = removeIfDuplicate(rankInfo)
                print(len(elements))
                print(len(companyInfo))
                print(len(rankInfo))

                
                save_company_into_DB(companyInfo, str(id))
                id += 1
                save_rank_into_DB(rankInfo)
                save_recruitment_into_DB(elements)
                
            
    except Exception as e:
        logger.error(f"Error occurred while scraping data: {e}")
    print('>> Done')
    
if __name__ == '__main__':
    craw_company_info()
    

