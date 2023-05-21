# PacmanTest.py
# 21-05-2023 / jjm
#
# This file is created to easily test the changed code. 
#
import subprocess

def get_score(output):
    lines = output.split('\n')
    for line in lines:
        if "Score: " in line:
            return int(line.split("Score: ")[1])
    return None

command = ["python2", "pacman.py", "-p", "MDPAgent", "-p"]
runs = 10
scores = []

for _ in range(runs):
    result = subprocess.run(command, stdout=subprocess.PIPE)
    score = get_score(result.stdout.decode('utf-8'))
    if score is not None:
        scores.append(score)

average_score = sum(scores) / len(scores) if scores else 0

print("Scores: ", scores)
print("Average Score: ", average_score)