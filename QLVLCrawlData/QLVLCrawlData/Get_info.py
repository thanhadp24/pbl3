from venv import logger 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
from DB import *
from get_24 import *
def get_profile_urls_24(driver, url):
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        class_name = 'relative lg:h-[115px] w-full flex rounded-sm border lg:mb-3 mb-2 lg:hover:shadow-md !hover:bg-white !bg-[#FFF5E7] border-se-blue-10'
        a = page_source.find_all('a', class_=class_name)
        all_profile_urls = []
        for profile in a:
            profile_url = 'https://vieclam24h.vn' + profile.get('href')
            if profile_url not in all_profile_urls:
                all_profile_urls.append(profile_url)
        return all_profile_urls
    except Exception as e:
        logger.error(f"Error occurred while extracting profile URLs from {url}: {e}")
        return []
    
def get_profile_info_24(driver, url):
    try:
        driver.get(url)
        sleep(2)
        page_source = BeautifulSoup(driver.page_source, 'html.parser')
        company_name = get_company_name_24(page_source)
        title = get_title_24(page_source)
        deadline_date = get_Date_24(page_source)
        salary = get_Salary_24(page_source)
        exp_year = get_Exp_24(page_source)
        level = get_level_24(page_source)
        num_of_employee = get_NumEmployee_24(page_source)
        edu = get_Edu_24(page_source)
        src_pic = get_SrcPic_24(page_source)
        address = get_headquater_24(page_source) #address of company
        description = get_Description_24(page_source)
        requirement = get_Requirement_24(page_source)
        #job = get_job_24(page_source)   
        time = get_Time_24(page_source) #new
        place = get_Place_24(page_source) # place of working
        age = get_Age_24(page_source)
        sex = get_Sex_24(page_source)
        probation = get_probation(page_source)
        #way = get_Way_24(page_source) #WORKING_MODELS
        right = get_right_24(page_source)
        return [company_name, address, level, title, salary, time, deadline_date, exp_year,  
                 num_of_employee, age, sex, edu, probation, place, description, right, requirement, src_pic] 
    except Exception as e:
        logger.error(f"Error occurred while scraping data from {url}: {e}")
        return []
    
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=7&page=2&sort_q= >> IT hardware-network-telecommunication
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=13&occupation_ids%5B%5D=13&page=2&sort_q= >> Business
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=18&page=2&sort_q= >> Finance-Investment
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=12&page=4&sort_q= >> Marketing
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=26&page=2&sort_q= >> Auditing
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=8&page=2&sort_q=  >> IT software
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=3&page=2&sort_q=  >> Design - creative arts
# https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=21&page=2&sort_q= >> HealthCare
def get_info(driver, num_pages):
    try:
        page_start = 1
        data = []
        while page_start <= num_pages:
            url = f'https://vieclam24h.vn/tim-kiem-viec-lam-nhanh?occupation_ids%5B%5D=21&page={page_start}&sort_q='

            driver.get(url)
            sleep(2)
            profile_urls = get_profile_urls_24(driver, url)
           
            for i in profile_urls:
                info = get_profile_info_24(driver, i)
                data.append(info)
            page_start += 1
        return data
    except Exception as e:
        print(f"Error occurred while get data 24h: {e}")
        return []
   

    