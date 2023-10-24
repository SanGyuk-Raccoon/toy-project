def generateNumber():
    import random
    answer = random.sample(range(0, 10),3)
    return answer

def getUserInput():
    user_answer = input("please enter the number: ")
    return user_answer

def validateInput(user_answer):
    if user_answer.isdigit() == False:
        print("error : please enter the NUMBER")
        return False

    if len(user_answer) != 3:
        print("error : please enter the 3-digits number")
        return False

    if len(set(user_answer)) != 3:
        print("error : please enter the UNIQUE number")
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

    return strike, ball

def printResult(strike, ball):
    if strike == 0 and ball == 0:
        print("OUT!")
    elif strike == 3:
        print("you win!")
        return True
    else:
        print(strike,"S ",ball,"B")

###### 실제 게임 동작
answer = generateNumber()
print(answer)


while True:
    user_answer = getUserInput()
    if validateInput(user_answer) == True:
        strike_ball_count = compareAnswer(answer, user_answer)
        result = printResult(strike_ball_count[0], strike_ball_count[1])
        if result == True:
            break




