QUIT = -1

score = 0
scores = []

while score != QUIT:
    score = int(input("Add score. -1 to quit"))
    scores.append(score)

print(scores)