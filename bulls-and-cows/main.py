def generateNumber():
    import random
    answer = random.sample(range(0,10),3)
    return answer
def getUserInput():
    user_answer = input("please enter the number: ")
    return user_answer

def validateInput(user_answer):
    user_answer_list = list(map(int, str(user_answer)))
    if len(user_answer) != 3:
        print("error : please enter the 3-digits number")
        return False
    elif len(set(user_answer_list)) != 3:
        print("error : please enter the UNIQUE number")
        return False
    elif user_answer.isdigit == False:
        print("error : please enter the NUMBER")
        return False

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
        print("strike :", strike, "ball", ball)
###### 실제 게임 동작

answer = generateNumber()
print(answer)


while True:
    user_answer = getUserInput()
    validateInput(user_answer)
    strike_and_ball = compareAnswer(answer, user_answer)
    result = printResult(strike_and_ball[0], strike_and_ball[1])
    if result == True:
        break




