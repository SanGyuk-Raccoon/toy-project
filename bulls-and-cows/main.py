import logic

max_game_count = 10
answer = logic.generateNumber()
print(answer)

while max_game_count > 0:
    user_answer = logic.getUserInput()
    if logic.validateInput(user_answer):
        max_game_count -= 1
        strike_count, ball_count, out_count = logic.compareAnswer(answer, user_answer)
        result = logic.printResult(strike_count, ball_count, out_count)
        if strike_count == 3:
            break
