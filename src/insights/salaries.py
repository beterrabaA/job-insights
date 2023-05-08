from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    list = read(path)
    salaries_list = []
    for data in list:
        salary = data["max_salary"]
        if salary.isdigit():
            salaries_list.append(int(salary))
    return max(salaries_list)


def get_min_salary(path: str) -> int:
    list = read(path)
    salaries_list = []
    for data in list:
        salary = data["min_salary"]
        if salary.isdigit():
            salaries_list.append(int(salary))
    return min(salaries_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job and "max_salary" not in job:
        raise ValueError("Job does not have salary range")
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if min_salary > max_salary:
            raise ValueError("Invalid salary range")
        return min_salary <= int(salary) <= max_salary
    except Exception:
        raise ValueError("Invalid salary range")


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
