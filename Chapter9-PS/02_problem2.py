def game():
    # (temporary — suppose game returns score)
    score = int(input("Enter your score: "))
    return score


# play game
score = game()

# read previous high score
with open("Hi-score.txt", "r") as f:
    data = f.read()

# if file is empty
if data == "":
    high_score = 0
else:
    high_score = int(data)

# compare scores
if score > high_score:
    print("New High Score 🎉")

    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
else:
    print("Score:", score)
    print("High Score remains:", high_score)


game()