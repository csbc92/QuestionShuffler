import sys
import random
from parsers import xmlparser as xml, jsonparser as json


def get_question_file():
    question_file = "data/questions.json"

    if len(sys.argv) > 1:
        question_file = sys.argv[1]

    return question_file


def load_questions(path):
    if path.endswith(".json"):
        return json.fetch(path)
    elif path.endswith(".xml"):
        return xml.fetch(path)
    else:
        raise Exception("File format not supported.")


def print_header(header, pad):
    print("#" * pad)
    print("# " + header)
    print("#")


def print_footer(footer, pad):
    print("#")
    print("# " + footer)
    print("#" * pad)


def print_regular(output):
    lines = output.split("\n")
    for line in lines:
        print("# " + line)


def select_question(questions):
    selected = False
    while not selected:
        random_selected_question_index = random.randint(0, len(questions) - 1)
        random_question = questions[random_selected_question_index]

        if random_question not in answered_questions:
            selected = True
        elif len(answered_questions) == len(questions):
            print("\n\nYou have answered all questions.. " + str(len(answered_questions)) + "/" + str(len(questions)))
            exit(0)

    return random_question


def wait_for_input():
    while True:
        pressed_key = input("#\n# Press the Enter-key to reveal the answer..\n")

        if pressed_key == "":
            answered_questions.append(random_question)
            break
        else:
            print("Invalid option..")


def use_prioritized_questions():
    valid_input = False

    while not valid_input:
        prioritize = input("Use prioritized questions only? y/n\n")

        if prioritize == "y" or prioritize == "n":
            valid_input = True

    return prioritize == "y"


def prioritized_questions_only(questions):
    return list(filter(remove_nonprioritized_questions, questions))


def remove_nonprioritized_questions(question):
    return question.priority == 1


def get_progress(answered_questions, questions):
    return str(len(answered_questions) + 1) + "/" + str(len(questions))


if __name__ == '__main__':
    question_file = get_question_file()
    questions = load_questions(question_file)
    answered_questions = []

    if use_prioritized_questions():
        questions = prioritized_questions_only(questions)

    while True:
        random_question = select_question(questions)

        print_header("Question no. " + get_progress(answered_questions, questions) + ":", pad=150)
        print_regular(random_question.question)

        wait_for_input()

        print_regular("ANSWER:\n" + random_question.answer)
        print_footer("", pad=150)
        print("\n")
