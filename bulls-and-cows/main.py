import logic
import view

MAX_GAME_COUNT = 10
player_data = {}
while True:
    # game scene
    is_playing = view.playTitleScene()

    if not is_playing:
        break

    player_name = view.getPlayerName()
    true_number = logic.generateNumber()
    game_count = 0
    view.initGame()

    while game_count < MAX_GAME_COUNT:
        user_input = view.inputUserAnswer()
        if user_input == 'q':
            break

        game_count += 1
        game_result = logic.getGameResult(true_number, user_input)
        view.printGameProgress(game_count, user_input, game_result)

        if game_result.strike_count == 3:
            break
    player_score = logic.getPlayerScore(game_count, game_result)
    player_ranking = logic.getRank(player_name, player_score, player_data)
    view.printRank(player_ranking)