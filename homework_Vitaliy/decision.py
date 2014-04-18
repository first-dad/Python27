# -*- coding: utf-8 -*-


import operator


class Candidate(object):
    def __init__(self, name, age, sex, job, test, educ):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job
        self.test = test
        self.educ = educ


class Criteria(object):
    priorities = {
        'sex': {
            'm': 1,
            'f': 1,
            'mf': 1
        },
        'test': 1,
        'age': 1,
        'educ': {
            'high': 1,
            'middle': 25,
            'low': 1
        },
        'job': 1
    }

    sex_dict = {
        'm': 2,
        'f': 1,
        'mf': 0
    }

    def __init__(self, candidate):
        self.points = None
        self.candidate = candidate

    def set_points(self):
        self.points = {
            'sex': self.sex_dict[self.candidate.sex],
            'age': self.get_age_points(self.candidate.age),
            'job': self.get_job_points(self.candidate.job),
            'educ': self.get_educ_points(self.candidate.educ),
            'test': self.get_test_points(self.candidate.test)
        }

        return self

    def get_age_points(self, age):
        age_points = 0

        if 20 <= age < 40:
            age_points = 7
        elif 40 <= age <= 60:
            age_points = 3

        return age_points * self.priorities['age']

    def get_job_points(self, job):
        return (50 if job > 50 else job) * self.priorities['job']

    def get_points_sum(self):
        sum = 0

        for key, value in self.points.items():
            sum += value

        return sum

    def get_educ_points(self, educ):
        educ_points = 0

        if educ == 'high':
            educ_points = 4
        elif educ == 'middle':
            educ_points = 2
        elif educ == 'low':
            educ_points = 1

        return educ_points * self.priorities['educ'][educ]

    def get_test_points(self, test):
        return (30 if test > 30 else test) * self.priorities['test']


class Decision(object):
    def __init__(self, candidates):
        self.criterias = {}
        for candidate in candidates:
            self.criterias[candidate.name] = Criteria(candidate).set_points().get_points_sum()

        self.criterias = sorted(
            self.criterias.iteritems(),
            key=operator.itemgetter(1),
            reverse=True
        )

    def __str__(self):
        return str(self.criterias)


if __name__ == '__main__':
    print Decision([
        Candidate('John', 23, 'm', 30, 20, 'high'),
        Candidate('Tom', 23, 'f', 20, 23, 'low'),
        Candidate('Bill', 23, 'mf', 10, 28, 'middle')
    ])