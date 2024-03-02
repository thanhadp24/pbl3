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
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    try:
        with webdriver.Chrome(options=chrome_options) as driver:        
            elements = get_info(driver, 5)
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
            save_company_into_DB(companyInfo)
            save_rank_into_DB(rankInfo)
            save_recruitment_into_DB(elements)
            
    except Exception as e:
        logger.error(f"Error occurred while scraping data: {e}")
    print('>> Done')
    
if __name__ == '__main__':
    craw_company_info()
    

