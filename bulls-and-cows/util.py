from collections import namedtuple

GameResult = namedtuple("GameResult", ["strike_count", "ball_count", "out_count"])

if __name__=="__main__":
    result = GameResult(strike_count=10, ball_count=5, out_count=0)
    print(f"Strike Count:{result.strike_count}")
    print(f"Ball Count:{result.ball_count}")
    print(f"Out Count:{result.out_count}")
