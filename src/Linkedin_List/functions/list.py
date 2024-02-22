'''
    "Scraping Everything from Linkedin" # 1 Job List

    Author: aiXpertLab@gmail.com
    Date: January 14, 2024
    Description: 
    This is a Python script for scraping job list.
    It's one of "Scraping Everything from Linkedin"

'''

# Libraries
import os
import pandas as pd    

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
user_name = os.getenv('LD_USR')
password  = os.getenv('LD_KEY')

print(user_name)
print(password)

driver = webdriver.Chrome()  
driver.get('https://www.linkedin.com/login')

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user_name)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()   # Login button
driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a').click()   #jobs

# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3800581161&geoId=105080838&keywords=Artificial%20Intelligence%20Engineer&location=New%20York%2C%20United%20States&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=R")

# above, Login to the Linkedin, and get the search results.
# Get all links for these offers
links = []
# Navigate 13 pages
print('Links are being collected now.')
try: 
    jobs_block = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list')
    jobs_list= jobs_block.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')

    for job in jobs_list:
        all_links = job.find_elements(By.TAG_NAME,'a')
        for a in all_links:
            if str(a.get_attribute('href')).startswith("https://www.linkedin.com/jobs/view") and a.get_attribute('href') not in links: 
                links.append(a.get_attribute('href'))
            else:
                pass
        # scroll down for each job element
        driver.execute_script("arguments[0].scrollIntoView();", job)

except:
    pass
print('Found ' + str(len(links)) + ' links for job offers')
# Create empty lists to store information
job_titles = []
company_names = []
company_locations = []
work_methods = []
post_dates = []
work_times = [] 
job_desc = []

# i = 0
j = 1
