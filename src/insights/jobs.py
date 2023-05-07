from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    list = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            list.append(row)
    return list


def get_unique_job_types(path: str) -> List[str]:
    list = read(path)
    job_types = []
    for job in list:
        job_name = job["job_type"]
        if job_name not in job_types:
            job_types.append(job_name)
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    data = jobs
    filtered_list = []
    for job in data:
        if job["job_type"] == job_type:
            filtered_list.append(job)
    return filtered_list
