import os
import sys
import re

allowed_topics = ["stacks", "trees", "linked-lists", "graphs", "dynamic-programming", ]

def validate_name(name):
    if not all(c.isalnum() or c == '_' or c == '-' for c in name):
        raise ValueError("Invalid characters in the folder name. Only alphanumeric, hyphen, and underscore are allowed.")

def get_problem_name(input_string):
    modified_string = re.sub(r'^\d+_', '', input_string)
    return modified_string

def validate_topic(topic):
    if topic not in allowed_topics:
        raise ValueError(f"Invalid topic: {topic}. Allowed topics are: {', '.join(allowed_topics)}")

def create_topic_folder(topic):
    if not os.path.exists(topic):
        print(f"Dir {topic} created.")
        os.makedirs(topic)
    else:
        print(f"Dir {topic} already exists. Skipping creation.")

def create_question_folder(topic, question):
    question_folder = ''.join(c for c in question if c.isalnum() or c == '_' or c == '-')
    question_path = os.path.join(topic, question_folder)
    if not os.path.exists(question_path):
        print(f"Dir {question_path} created.")
        os.makedirs(question_path)
    else:
        print(f"Dir {question_path} already exists. Skipping creation.")
    return question_folder

def render_code_file(topic_folder_name, question_folder, problem_name):
    code_file_content = f"""# This code was AUTOGENERATED.
# Change it to fit your test case.
class Solution:
    pass
"""
    code_file_path = os.path.join(topic_folder_name, question_folder, f"{problem_name}.py")

    # Check if the file already exists
    if not os.path.exists(code_file_path):
        # Ensure that the directory structure leading to the file exists
        os.makedirs(os.path.dirname(code_file_path), exist_ok=True)

        with open(code_file_path, 'w') as test_file:
            test_file.write(code_file_content)
    else:
        print(f"File '{code_file_path}' already exists. Skipping creation.")


def render_test_file(topic_folder_name, question_folder, problem_name):
    test_file_content = f"""# This code was AUTOGENERATED.
# Change it to fit your test case.
import {problem_name}
import pytest

@pytest.mark.parametrize(
    ("input_1", "input_2", "output"),
    [
        # parametrized test case 1
        ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2, [[1, 1, 3], [3, 4, 5], [7, 8, 9]]),
        # parametrized test case 2
        ([1,3,3,2,7,3], 2, []),
    ]
)

def test_problem(input_1, input_2, output):
    s = {problem_name}.Solution()
    # Call your program here. For example:
    # calculated_res = s.fn_name(input_1, input_2)
    # assert calculated_res == output
"""
    # Check if the file already exists
    test_file_path = os.path.join(topic_folder_name, question_folder, f"{problem_name}_test.py")
    if not os.path.exists(test_file_path):

        # Ensure that the directory structure leading to the file exists
        os.makedirs(os.path.dirname(test_file_path), exist_ok=True)

        with open(test_file_path, 'w') as test_file:
            test_file.write(test_file_content)
    else:
        print(f"File '{test_file_path}' already exists. Skipping creation.")


def render_md_file(topic_folder_name, question_folder, problem_name):
    md_file_content = f"""## Details for question

Links   
[Question](problem-link-here) <br>
Python  
    - [Code file]({problem_name}.py)  
    - [Test file]({problem_name}_test.py)

Tags: adhoc, bit

Description:

- Point 1

Questions:

- Point 1

Observations:

- Point 1

Complexity:

- Time:
- Space:
"""
    md_file_path = os.path.join(topic_folder_name, question_folder, f"{problem_name}.md")

    # Check if the file already exists
    if not os.path.exists(md_file_path):
        # Ensure that the directory structure leading to the file exists
        os.makedirs(os.path.dirname(md_file_path), exist_ok=True)

        with open(md_file_path, 'w') as md_file:
            md_file.write(md_file_content)
    else:
        print(f"File '{md_file_path}' already exists. Skipping creation.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <topic-folder-name> <question-folder-name>")
        sys.exit(1)

    topic_folder_name = sys.argv[1]
    question_folder_name = sys.argv[2]

    try:
        print("...Starting...!")
        validate_topic(topic_folder_name)
        validate_name(question_folder_name)
        create_topic_folder(topic_folder_name)
        question_folder = create_question_folder(topic_folder_name, question_folder_name)
        problem_name = get_problem_name(question_folder_name)
        render_code_file(topic_folder_name, question_folder, problem_name)
        render_test_file(topic_folder_name, question_folder, problem_name)
        render_md_file(topic_folder_name, question_folder, problem_name)
        print("...Done...!")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
