import random

#Returns a random integer within a specified range
def Generate_Random_Integer(min_value, max_value):
    """
    Random Integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

#Returns a random Mathematical operator between '+' , '-' , '*'
def Get_Random_Operator():
    return random.choice(['+', '-', '*'])

#Perform an Arithmetic Operation on two numbers and return expression and result
def Generate_Mathematical_Expression_Result(num_1, num_2, operator):
    expression = f"{num_1} {operator} {num_2}"      #expression generation
    if operator == '+': 
        result = num_1 + num_2   #Addition operation
    elif operator == '-': 
        result = num_1 - num_2   #Subtraction operation
    else:
         result = num_1 * num_2     #Multiplication operation
    return expression, result       #Returns expression with its result

def math_quiz():
    score = 0       #Score counter
    total_questions = 3    #Total number of questions for the quiz
  
    #Welcome message 
    print(" Welcome to the Math Quiz Game! ")
    print(" You will be presented with math problems, and you need to provide the correct answers.")

    #for loop for generating random number and operator, performing arithmatic operation and returning result
    for _ in range(total_questions):
        num_1 = Generate_Random_Integer(1, 10); 
        num_2 = Generate_Random_Integer(1, 5); 
        operator = Get_Random_Operator()

        PROBLEM, ANSWER = Generate_Mathematical_Expression_Result(num_1, num_2, operator)

        print(f"\nQuestion: {PROBLEM}")

        #User can enter their answer
        user_answer = input("Your answer: ") 
        user_answer = int(user_answer)

        #If User input is not an Integer/Invalid
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid Input !!!. Please Enter an Integer.")
            continue

        #If user provides correct answer for the question
        if user_answer == ANSWER:
            print("Barvo! Correct! You earned a point.")
            score += 1          #Increment the score counter by 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")    #If user answer is wrong

    print(f"\nGame Over! Your score is: {score}/{total_questions}")     #End message with final score

if __name__ == "__main__":
    math_quiz()
