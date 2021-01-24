from classes.question import Question
import xml.etree.ElementTree as ET

def fetch(path):
    questions = []

    tree = ET.parse(path)
    root = tree.getroot()

    for q in root.findall("questions/element"):
        priority = get_xml_attribute_int(q, "priority")
        question = get_xml_attribute_str(q, "question")
        answer = get_xml_attribute_str(q, "answer")

        questions.append(Question(question, answer, priority))

    return questions

def get_xml_attribute_str(parent_node, child_str):
    value = None
    try:
        value = parent_node.find(child_str).text
    except:
        pass
    return value

def get_xml_attribute_int(parent_node, child_str):
    value = None
    try:
        value = int(parent_node.find(child_str).text)
    except:
        pass
    return value