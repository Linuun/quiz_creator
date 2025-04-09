RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
CYAN = '\033[96m'
# create a file using with and open function in append mode
with open("quiz.txt", "a") as file:
# use while loop
    while True:
# ask user to input a question, the possible answers, and the correct answer
        print("\n⚒️ Let's build a fun quiz!")
        question = input(f"{GREEN}Enter a question: ")
        answer_a = input(f"{BLUE}A.) ")
        answer_b = input(f"{BLUE}B.) ")
        answer_c = input(f"{BLUE}C.) ")
        answer_d = input(f"{BLUE}D.) ")
        correct_answer = input("Enter the correct answer: ").upper()
# print "Invalid Answer" if correct answer is not in choice
        if correct_answer not in ["A", "B", "C", "D"]:
            print(f"{RED}Invalid Answer!🚫 Please enter A, B, C, or D")
# use write function to write the inputs of the user in the file
        file.write(f"Question: {question}\n")
        file.write(f"A.) {answer_a}\n")
        file.write(f"B.) {answer_b}\n")
        file.write(f"C.) {answer_c}\n")
        file.write(f"D.) {answer_d}\n")
        file.write(f"The correct answer is: {correct_answer}\n")
        file.write(f"=======================\n")
# ask the user if they want to continue
        again = input("Do you want to add another question? (YES/NO): ").upper()
# break the loop if not and save it to the file
        if again != "YES":
            print(f"\n{CYAN}🛠️ All done! You've built a fun and exciting quiz.🛠️")
            print(f"\n{CYAN} All your questions have been saved in quiz.txt.")
            break