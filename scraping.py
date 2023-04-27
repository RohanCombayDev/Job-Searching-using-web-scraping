# scraping real website

from bs4 import BeautifulSoup
import requests
import time

# scraping times job website to find jobs in pune based on user's skills

# taking skills as input from user
skill = input('>')
print(f'''Searching for jobs consisting of your {skill}''')


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=&txtLocation=pune').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info = job.header.h2.a['href']

        if skill in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Company Name: {company_name.strip()}\n")
                f.write(f"Required Skills: {skills.strip()}\n")
                f.write(f"More info: {more_info}")
            print(f'File Saved: {index}')


find_jobs()

