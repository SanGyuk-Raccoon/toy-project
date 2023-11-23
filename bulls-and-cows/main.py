import logic
import view

MAX_GAME_COUNT = 10

while True:
    # game scene
    is_playing = view.playTitleScene()

    if not is_playing:
        break

    player_name = view.getPlayerName()
    true_number = logic.generateNumber()
    game_count = 0
    view.initGame()
# todo 게임재시작창에서 y일 경우 main으로 돌아가지만, user_input이 남아 game_result를 받을 때 오류가 발생합니다. 이 부분 수정이 필요합니다.
    while game_count < MAX_GAME_COUNT:
        user_input = view.inputUserAnswer()
        if user_input == 'R':
            if view.restartGame():
                continue

        game_count += 1
        game_result = logic.getGameResult(true_number, user_input)
        view.printGameProgress(game_count, user_input, game_result)

        if game_result.strike_count == 3:
            break
# todo game_result 함수를 안 받을 때가 없도록 수정이 필요합니다.
    player_score = logic.getPlayerScore(game_count, game_result)
    player_ranking = logic.getRank(player_name, player_score)
    view.printFinalResult(true_number, player_score, game_count, game_result)
    view.printRank(player_ranking)