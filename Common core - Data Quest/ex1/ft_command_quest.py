import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    score = []

    i = 1
    while i < len(sys.argv):
        try:
            score += [int(sys.argv[i])]
        except ValueError:
            print(f"Invalid parameter: {sys.argv[i]}")

        i += 1
    if len(score) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    print(f"Scores processed: {score}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {sum(score)/len(score)}")
    print(f"High score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {max(score) - min(score)}")


ft_score_analytics()
