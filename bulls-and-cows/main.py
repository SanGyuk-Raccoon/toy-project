def generateNumber():
    import random
    answer = random.sample(range(0,10),3)
    return answer
def getUserInput():
    user_answer = input("please enter the number: ")
    return user_answer
def validateInput(answer, user_answer):
    strike = 0
    ball = 0
    for i in range(len(answer)):
        if answer[i] == user_answer[i]:
            strike += 1
        elif user_answer in answer:
            ball += 1
    return strike, ball
def compareAnswer():
    # n(strike)
    # n(Ball)
    # print(n(strike, n(Ball)))
    return
def printResult(result):
    return
###### 실제 게임 동작

answer = generateNumber()
print(answer)

while True:
    user_input = getUserInput()
    validateInput(user_input)

    compareAnswer(user_input)




