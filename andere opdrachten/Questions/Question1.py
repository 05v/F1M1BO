# Question 1
def Question1():

    print("Question blablabla:")
    print("[A]: ")
    print("[B]: ")
    print("[C]: ")
    question_input = input("Answer: ")

    # Activates Answer A for question2
    if question_input == "A" or question_input == "a":

        question2_a()

    # Activates Answer B for question2
    elif question_input == "B" or question_input == "b":

        question2_b()

    # Activates Answer C for question2
    elif question_input == "C" or question_input == "c":

        question2_c()

    # Else output
    else:
        print("That's not an option, try again")
        print(question_input)