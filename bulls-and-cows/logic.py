import random
from util import GameResult

def generateNumber():
    answer = random.sample(range(0, 10), 3)
    return answer

def validateInput(user_answer):
    if not user_answer.isdigit():
        return False

    if len(set(user_answer)) != 3:
        return False

    return True


def getGameResult(answer, user_answer):
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

    return GameResult(strike_count=strike,
                      ball_count=ball,
                      out_count=out)


def getResult(strike, ball, out, game_count):
    if strike == 3:
        if game_count==1:
            return "HOME RUN!"
        else:
            return "you win!"
    elif out == 3:
        return "strike out!"
    else:
        return f"{strike}S, {ball}B, {out}O"

def getPlayerName():
    player_name = input("enter your name: ")
    return player_name

def getPlayerScore(game_count, result, game_result:GameResult):
    GAME_SCORE = player_score = 1000
    score_multiple = 100

    if game_result.strike_count == 3:
        if result == "HOME RUN!":
            player_score += 1000
        if result == "HITS":
            player_score -= game_count * score_multiple
    elif game_result.out_count == 3:
        player_score -= game_count * score_multiple
    return player_score

def getRank(player_name, player_score):
    player_data_DICT = {}
    player_data_DICT.setdefault(player_name, player_score)
    player_ranking = sorted(player_data_DICT.items(), key=lambda x: x[1], reverse=True)
    return player_ranking

if __name__ == "__main__":
    R_B = getRank("우정훈", 1)
    print(R_B)