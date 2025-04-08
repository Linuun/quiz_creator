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
# use write function to write the inputs of the user in the file
# ask the user if they want to continue
# break the loop if not