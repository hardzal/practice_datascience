from bs4 import BeautifulSoup
import requests

import pandas as pd

link = 'https://jobs.github.com'

def search_jobs(jobs):
    row_list = []
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

        dict_data = {}
        dict_data.update({"Job Title" : job_title.text, "Job Company": job_company.text, "Job Type": job_type.text, "Job Location": job_location.text, "Job Posted": job_posted.text, "Job Link": job_link, "Job Description": job_description.text})
        row_list.append(dict_data)
    return row_list


if __name__ == '__main__':
    row_data = []
    next_link = True
    html_text = requests.get(f"{link}/positions")
    result = BeautifulSoup(html_text.content, 'lxml')
    jobs = result.find_all('tr', class_='job')
    next_link = result.find('div', class_='pagination')
    row_data.append(search_jobs(jobs))
    while True: 
        next_result = []
        
        if(next_link): 
            new_html_text = requests.get(f"{link}{next_link.a['href']}")
            next_result = BeautifulSoup(new_html_text.content, 'lxml')

            old_link = next_link.a['href']
            next_link = next_result.find('div', class_='pagination')
            row_data.append(search_jobs(jobs))
            if(next_link):
                print(next_link.a['href'])
            else:
                next_link = False
        else:
            print(old_link)

    df = pd.DataFrame(row_data)
    df.to_csv(r'D:\Code\Practice\python\scrapping\github_joblist\export_dataframe.csv')
    print(df)
    print(f"saved!{len(df)}")
        