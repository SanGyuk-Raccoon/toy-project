import random

def generateNumber():
    answer = random.sample(range(0, 10), 3)
    return answer


def getUserInput():
    user_answer = input("please enter the number: ")
    return user_answer


def validateInput(user_answer):
    if not user_answer.isdigit():
        print("error : please enter the NUMBER")
        return False

    if len(set(user_answer)) != 3:
        print("error : please enter the 3-digits or UNIQUE number")
        return False

    return True


def compareAnswer(answer, user_answer):
    user_answer_list = list(map(int, str(user_answer)))
    strike = 0
    ball = 0

    for i in range(len(answer)):
        for j in range(len(user_answer_list)):
            if answer[i] == user_answer_list[j] and i == j:
                strike += 1
            elif answer[i] == user_answer_list[j] and i != j:
                ball += 1

    out = 3 - strike - ball

    return strike, ball, out


def printResult(strike, ball, out):
    if strike == 3:
        print("you win!")
    elif out == 3:
        print("strike out!")
    else:
        print(strike, "S ", ball, "B ", out, "O")
