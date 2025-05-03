# import libraries
import pygame
import tkinter as tk
from tkinter import filedialog
import random
import sys
# ask the user to choose the quiz text file
def choose_quiz_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Select a quiz file",
        filetypes=[("Text Files", "*.txt")]
    )
# use with and open function to open the file in read mode
def load_questions(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read().strip()
# split the contents of the file using a separator
# extract the question, possible answers, and correct answer
    question_blocks = content.split('=======================')
    questions = []

    for block in question_blocks:
        lines = block.strip().split('\n')
        if len(lines) < 6:
            continue

        question_line = lines[0]
        choices_lines = lines[1:5]
        answer_line = lines[5]

        if not question_line.startswith("Question:"):
            continue

        question = question_line[len("Question:"):].strip()
        choices = [line[4:].strip() for line in choices_lines if len(line) > 3 and line[1:4] == '.) ']
# convert answer letter to index
        question = question_line[len("Question:"):].strip()
        choices = [line[4:].strip() for line in choices_lines if len(line) > 3 and line[1:4] == '.) ']
# append (question, choices, correct_answer) to a list
# return list of all valid questions
        answer_letter = answer_line.split(":")[-1].strip()
        correct_index = ord(answer_letter.upper()) - ord('A')
        if 0 <= correct_index < len(choices):
            correct_answer = choices[correct_index]
            questions.append((question, choices, correct_answer))

    return questions
# create a text box with a background and padding 
# fill the background with some colors
# initialize pygame and sets up the game
# use while loop to run the game
# handle events like quitting the game
# checks answer and gives feedback
# update the score and goes to the next question or ends the game
# handles answer input
# shows the question and choices in styled text boxes
# shows the score and the instructions to exit the game
# updates the display and limits to 30 frames/second.
# run the entire program