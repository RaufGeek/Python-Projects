quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Azerbaijan",
        "answer": "Baku"
    },
    "question3": {
        "question": "What is the capital of Turkey",
        "answer": "Ankara"
    },
    "question4": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },"question5": {
        "question": "What is the capital of China?",
        "answer": "Pekin"
    },
      "question6": {
        "question": "What is the capital of Russia?",
        "answer": "Moskow"
    },
      "question7": {
        "question": "What is the capital of Iran?",
        "answer": "Tehran"
    },
      "question8": {
        "question": "What is the capital of Iraq?",
        "answer": "Bagdad"
    },
      "question9": {
        "question": "What is the capital of Norway?",
        "answer": "Oslo"
    },
      "question10": {
        "question": "What is the capital of Portugal?",
        "answer": "Lissabon"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'] . lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 10 questions correctly")
print("Your percentage is " + str(int(score/10 * 100)) + "%")
