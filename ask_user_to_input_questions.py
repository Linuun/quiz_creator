# create a file using with and open function in append mode
with open("quiz.txt", "a") as file:
# use while loop
    while True:
# ask user to input a question, the possible answers, and the correct answer
        print("\n Let's build a fun quiz!")
        question = input("Enter a question: ")
        answer_a = input("A.) ")
        answer_b = input("B.) ")
        answer_c = input("C.) ")
        answer_d = input("D.) ")
        correct_answer = input("Enter the correct answer: ").upper()
# print "Invalid Answer" if correct answer is not in choice
        if correct_answer not in ["A", "B", "C", "D"]:
            print("Invalid Answer! Please enter A, B, C, or D")
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
# break the loop if not