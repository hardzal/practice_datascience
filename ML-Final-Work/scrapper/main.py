from bs4 import BeautifulSoup
import requests

import pandas as pd

link = 'https://jobs.github.com'
data_set = {"Job Title" : [], "Job Company": [], "Job Type": [], "Job Location": [], "Job Posted": [], "Job Link": [], "Job Description": []}

def search_jobs(jobs):
    for job in jobs:
        job_title = job.find('h4')
        job_company = job.find('a', class_='company')
        job_location = job.find('span', class_='location')
        job_type = job.find('strong')
        job_posted = job.find('span', class_='when relatize relatized')
        job_link = job_title.a['href']
        new_access = requests.get(job_link)
        job_detail = BeautifulSoup(new_access.content, 'lxml')
        job_description = job_detail.find('div', class_='column main')

        data_set["Job Title"].append(job_title.text) 
        data_set["Job Company"].append(job_company.text) 
        data_set["Job Type"].append(job_type.text) 
        data_set["Job Location"].append(job_location.text) 
        data_set["Job Posted"].append(job_posted.text)
        data_set["Job Link"].append(job_link) 
        data_set["Job Description"].append(job_description.text)

if __name__ == '__main__':
    next_link = True
    html_text = requests.get(f"{link}/positions")
    result = BeautifulSoup(html_text.content, 'lxml')
    jobs = result.find_all('tr', class_='job')
    next_link = result.find('div', class_='pagination')
    
    search_jobs(jobs)

    print(next_link.a['href'])

    while True: 
        next_result = []
        
        if(next_link): 
            new_html_text = requests.get(f"{link}{next_link.a['href']}")
            next_result = BeautifulSoup(new_html_text.content, 'lxml')
            new_jobs =  result.find_all('tr', class_='job')

            old_link = next_link.a['href']
            next_link = next_result.find('div', class_='pagination')
            if(next_link):
                print(next_link.a['href'])
            else:
                next_link = False

            search_jobs(new_jobs)
        else:
            print(old_link)
            break

    df = pd.DataFrame(data_set, columns=['Job Title', 'Job Company', 'Job Type', 'Job Location', 'Job Posted', 'Job Link', 'Job Description'])
    df.to_csv(r'D:\Code\Practice\python\scrapping\github_joblist\export_dataframe.csv', index = False, header=True)

    print(df)
    print(f"saved!{len(df)}")
        