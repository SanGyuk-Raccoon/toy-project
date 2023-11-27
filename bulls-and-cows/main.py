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
    game_result = None
    view.showGameScreen()

    while game_count < MAX_GAME_COUNT:
        user_input = view.inputUserAnswer()
        if user_input == 'R':
            if view.restartGame():
                game_count = 0
                break
            else:
                continue

        game_count += 1
        game_result = logic.getGameResult(true_number, user_input)
        view.printGameProgress(game_count, user_input, game_result)

        if game_result.strike_count == 3:
            break

    if game_count >= 1:
        player_score = logic.getPlayerScore(game_count, game_result)
        player_ranking = logic.rankPlayers(player_name, player_score)
        view.printFinalResult(true_number, player_score, game_count, game_result)
        view.printRank(player_ranking)