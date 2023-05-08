from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    list = read(path)
    industries_list = []
    for industry in list:
        industry_name = industry["industry"]
        if industry_name != "":
            if industry_name not in industries_list:
                industries_list.append(industry_name)
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    data = jobs
    filtered_jobs_industry = []
    for job in data:
        if job["industry"] == industry:
            filtered_jobs_industry.append(job)
    return filtered_jobs_industry
