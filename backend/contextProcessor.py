from .models import Subject
from typing import List


def pairSemester(a: int, b: int) -> List[List]:
    x = Subject.objects.filter(semester=a)
    y = Subject.objects.filter(semester=b)
    _max = max(len(x), len(y))
    data = []
    for i in range(0, _max, 1):
        temp = []
        try:
            try:
                temp.clear()
                temp.append(x[i])
                temp.append(y[i])
            except:
                temp.clear()
                temp.append(x[i])
                temp.append(None)
        except:
            temp.clear()
            temp.append(None)
            temp.append(y[i])
        data.append(temp)
        print(temp)
    return data


def getSubjectTableData():
    first_year = pairSemester(1, 2)
    second_year = pairSemester(3, 4)
    third_year = pairSemester(5, 6)
    context = {
        'first_year': first_year,
        'second_year': second_year,
        'third_year': third_year,
    }

    return context
