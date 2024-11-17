#Exercise 1: Temperature Advice

import random

# Function to get random temperature
def get_random_temp(season):
    if season == 'winter':
        return random.randint(-10, 16)
    elif season == 'spring':
        return random.randint(5, 20)
    elif season == 'summer':
        return random.randint(20, 40)
    elif season == 'autumn' or season == 'fall':
        return random.randint(5, 25)
    else:
        return "Invalid season"

# Function to give advice based on temperature
def main():
    # Ask the user for the season (or month)
    season = input("Enter the season (summer, autumn, winter, spring): ").lower()

    # Get random temperature based on season
    temp = get_random_temp(season)
    
    # Output the temperature
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    # Give friendly advice based on the temperature
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather! A light jacket should be enough.")
    elif 24 <= temp <= 32:
        print("Warm day! A t-shirt will do.")
    elif 32 < temp <= 40:
        print("It's really hot! Stay cool and drink plenty of water.")

# Run the main function
main()

data = [
    {"question": "What is Baby Yoda's real name?", "answer": "Grogu"},
    {"question": "Where did Obi-Wan take Luke after his birth?", "answer": "Tatooine"},
    {"question": "What year did the first Star Wars movie come out?", "answer": "1977"},
    {"question": "Who built C-3PO?", "answer": "Anakin Skywalker"},
    {"question": "Anakin Skywalker grew up to be who?", "answer": "Darth Vader"},
    {"question": "What species is Chewbacca?", "answer": "Wookiee"}
]

# Function to ask quiz questions and track answers
def take_quiz():
    correct_answers = 0
    wrong_answers = []
    
    # Ask each question
    for q in data:
        answer = input(q["question"] + " ")
        if answer.lower() == q["answer"].lower():
            correct_answers += 1
        else:
            wrong_answers.append((q["question"], answer, q["answer"]))
    
    return correct_answers, wrong_answers

# Function to display results
def display_results(correct, wrong):
    print(f"\nYou got {correct} correct answers!")
    if wrong:
        print("\nHere are the questions you answered wrong:")
        for q, answer, correct_answer in wrong:
            print(f"Question: {q}\nYour answer: {answer}\nCorrect answer: {correct_answer}\n")
    if len(wrong) > 3:
        print("Too many wrong answers! Try again.")
    else:
        print("Good job!")

# Main function
def main():
    correct, wrong = take_quiz()
    display_results(correct, wrong)

# Run the quiz
main()





#Exercise 3: When will I retire?

from datetime import datetime

# Function to calculate age
def get_age(year, month, day):
    current_date = datetime.now()
    birth_date = datetime(year, month, day)
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# Function to check if the person can retire
def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)
    
    # Retirement age
    if gender == 'm' and age >= 67:
        return True
    elif gender == 'f' and age >= 62:
        return True
    else:
        return False

# Main function
def main():
    gender = input("Enter your gender (m/f): ").lower()
    date_of_birth = input("Enter your date of birth (yyyy/mm/dd): ")
    
    if can_retire(gender, date_of_birth):
        print("You can retire!")
    else:
        print("You cannot retire yet.")

# Run the program
main()





#Exercise 4: X + XX + XXX + XXXX

# Function to calculate X + XX + XXX + XXXX
def calculate_value(x):
    # Treat the number as a string for concatenation
    x_str = str(x)
    result = int(x_str) + int(x_str * 2) + int(x_str * 3) + int(x_str * 4)
    return result

# Test the function
print(calculate_value(3))  # Output: 3702 (3 + 33 + 333 + 3333)