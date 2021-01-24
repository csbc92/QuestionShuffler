import json
from classes.question import Question

def fetch(path):
    questions = []
    with open(path, encoding="utf8") as json_file:
        data = json.load(json_file)

        for q in data['questions']:
            priority = get_attribute_int(q, "priority")
            question = get_attribute_str(q, "question")
            answer = get_attribute_str(q, "answer")

            questions.append(Question(question, answer, priority))

    return questions


def get_attribute_str(json_object, attribute):
    value = None
    try:
        value = json_object[attribute]
    except:
        pass
    return value

def get_attribute_int(json_object, attribute):
    value = None
    try:
        value = int(json_object[attribute])
    except:
        pass
    return value