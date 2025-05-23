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
        red = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        green = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        blue = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        pygame.draw.line(surface, (red, green, blue), (0, y), (surface.get_width(), y))
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
# checks answer and gives feedback
# update the score and goes to the next question or ends the game
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        correct_answer = questions[question_index][2]
                        selected_letter = user_input.strip().upper()

                        try:
                            selected_index = ord(selected_letter) - ord('A')
                            selected_answer = questions[question_index][1][selected_index]
                        except:
                            selected_answer = ""

                        if selected_answer == correct_answer:
                            feedback = "✅ Correct!"
                            feedback_color = (100, 255, 100)
                            score += 1
                        else:
                            feedback = f"❌ Incorrect! Correct: {correct_answer}"
                            feedback_color = (255, 100, 100)

                        user_input = ""
                        question_index += 1

                        if question_index >= len(questions):
                            game_over = True
# handles answer input
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    elif event.unicode.isalpha():
                        user_input = event.unicode.upper()
# shows the question and choices in styled text boxes
        margin_top = 50
        margin_left = 60

        if not game_over:
            question = questions[question_index][0]
            choices = questions[question_index][1]

            y = draw_text_box(screen, f"Question {question_index + 1}", font, (255, 255, 255), margin_left, margin_top, 780)
            y = draw_text_box(screen, question, font, (255, 255, 0), margin_left, y + 20, 780)

            for i, choice in enumerate(choices):
                y = draw_text_box(screen, f"{chr(65 + i)}) {choice}", small_font, (200, 200, 200), margin_left, y + 10, 780)

            y += 30
            draw_text_box(screen, f"Your Answer (A-D): {user_input}", small_font, (200, 200, 255), margin_left, y, 780)
            draw_text_box(screen, feedback, small_font, feedback_color, margin_left, y + 50, 780)
# shows the score and the instructions to exit the game
        else:
            y = draw_text_box(screen, "🎉 Quiz Complete!", font, (255, 255, 255), margin_left, margin_top, 780)
            y = draw_text_box(screen, f"Your score: {score} / {len(questions)}", font, (0, 255, 0), margin_left, y + 30, 780)
            draw_text_box(screen, "Press ESC to exit.", small_font, (180, 180, 180), margin_left, y + 60, 780)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
# updates the display and limits to 30 frames/second.
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
# run the entire program
if __name__ == "__main__":
    file = choose_quiz_file()
    if not file:
        print("No file selected.")
        sys.exit()

    questions = load_questions(file)
    if not questions:
        print("No valid questions found in the file.")
        sys.exit()

    run_quiz_game(questions)