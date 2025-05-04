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
def draw_text_box(surface, text, font, color, x, y, width, padding=10, bg_color=(40, 40, 60), border_radius=12):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x + padding, y + padding)
    box_rect = pygame.Rect(x, y, width, text_rect.height + 2 * padding)
    pygame.draw.rect(surface, bg_color, box_rect, border_radius=border_radius)
    surface.blit(text_surface, text_rect)
    return box_rect.bottom
# fill the background with some colors
def draw_gradient(surface, color_top, color_bottom):
    for y in range(surface.get_height()):
        ratio = y / surface.get_height()
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (surface.get_width(), y))
# initialize pygame and sets up the game
def run_quiz_game(questions):
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Quiz Master")
    font = pygame.font.SysFont("arial", 28, bold=True)
    small_font = pygame.font.SysFont("arial", 22)
    clock = pygame.time.Clock()

    random.shuffle(questions)
    question_index = 0
    user_input = ""
    feedback = ""
    feedback_color = (255, 255, 255)
    score = 0
    game_over = False
    running = True
# use while loop to run the game
    while running:
        draw_gradient(screen, (15, 20, 45), (30, 60, 90))
# handle events like quitting the game
# checks answer and gives feedback
# update the score and goes to the next question or ends the game
# handles answer input
# shows the question and choices in styled text boxes
# shows the score and the instructions to exit the game
# updates the display and limits to 30 frames/second.
# run the entire program