survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

set_survey = list()

for set_item in survey_results:
    set_survey.append(set(set_item))

intersection_set = set.intersection(*set_survey)



print(intersection_set)