import random
from util import GameResult

PLAYER_DATA_DICT = {}

def generateNumber():
    answer = random.sample(range(0, 10), 3)
    return answer

def validateAnswer(user_answer):
    if not user_answer.isdigit():
        return False

    if len(set(user_answer)) != 3:
        return False

    return True


def validatePlayerName(player_name):
    if not player_name.isalpha():
        return False

    if len(player_name) != 3:
        return False

    return True

def getGameResult(answer, user_answer):
    if user_answer != "R": #'R' = 재시작 기능, 재시작 기능으로 인한 오류 발생으로 인한 예외 필요
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



def getPlayerScore(game_count, game_result: GameResult):
    player_score = 1000
    score_multiple = 100

    if game_result.strike_count == 3 and game_count == 1:
        player_score += 1000
    else:
        player_score -= game_count * score_multiple

    return player_score


def rankPlayers(player_name, player_score):
    original_name = player_name
    dupe_count = 1

    while player_name in PLAYER_DATA_DICT:
        player_name = f"{original_name}_{dupe_count}"
        dupe_count += 1

    PLAYER_DATA_DICT.setdefault(player_name, player_score)
    player_ranking = sorted(PLAYER_DATA_DICT.items(), key=lambda x: x[1], reverse=True)
    return player_ranking