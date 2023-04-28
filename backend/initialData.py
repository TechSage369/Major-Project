from .models import Note, Subject, Video_Lecture

subject_data = [
    [1, 'Programming Fundamentals using C', 'CC-12'],
    [1, 'Computer System Architecture', 'CC-13'],
    [1, 'Environmental Science', 'AE-11'],
    [1, 'Mathematics', 'GE14'],
    [1, 'Programming Fundamentals using C Lab', 'CC-12L'],
    [1, 'Computer System Architecture Lab', 'CC-13L'],

    [2, 'Programming in JAVA', 'CC-22'],
    [2, 'Discrete Structures', 'CC-23'],
    [2, 'English', 'AEC-21'],
    [2, 'Mathematics', 'GE-24'],
    [2, 'Programming in JAVA Lab', 'CC-22L'],
    [2, 'Discrete Structures Tutorial', 'CC-23T'],

    [3, 'Data Structures', 'CC-31'],
    [3, 'Operating System', 'CC-32'],
    [3, 'Computer Networks', 'CC-33'],
    [3, 'Physics', 'GE-34'],
    [3, 'Data Structures Lab', 'CC-31L'],
    [3, 'Operating System Lab', 'CC-32L'],
    [3, 'Computer Networks Lab', 'CC-33L'],
    [3, 'Website Design with HTML and PHP', 'SEC-35TL-E2'],

    [4, 'Design and Analysis of Algorithms', 'CC-41'],
    [4, 'Software Engineering', 'CC-42'],
    [4, 'Database Management System', 'CC-43'],
    [4, 'Physics', 'GE-44'],
    [4, 'Design and Analysis of Algorithms Lab', 'CC-41L'],
    [4, 'Software Engineering Lab', 'CC-42L'],
    [4, 'Database Management System Lab', 'CC-43L'],
    [4, 'Programming in MATLAB', 'SEC-45TL-E2'],

    [5, 'Internet Tehcnologies', 'CC-51'],
    [5, 'Theory of Computation', 'CC-52'],
    [5, 'Microprocessor', 'DSE-53-E1'],
    [5, 'Combinatorial Optimization', 'DSE-54-E2'],
    [5, 'Internet Tehcnologies Lab', 'CC-51L'],
    [5, 'Theory of Computation', 'CC-52T'],
    [5, 'Microprocessor Lab', 'DSE-53L-E1L'],
    [5, 'Combinatorial Optimization Lab', 'DSE-54L-E2L'],

    [6, 'Artificial Intelligence', 'CC-61'],
    [6, 'Computer Graphics', 'CC-62'],
    [6, 'Data Mining', 'DSE-63-E3'],
    [6, 'Artificial Intelligence Lab', 'CC-61L'],
    [6, 'Computer Graphics Lab', 'CC-62L'],
    [6, 'Data Mining Lab', 'DSE-63L-E3L'],

]


def insertSubject():
    for data in subject_data:
        x = Subject(data[0], data[1], data[2])
        x.save()
