# Method to find the ranked for each player in the leaderboard
def climbingLeaderboard(ranked , player):
    currentRank = len(set(ranked))
    scoreIndex = 0
    highscoreIndex = len(ranked) - 1
    while(scoreIndex != len(player)):
        while(player[scoreIndex] > ranked[highscoreIndex] and highscoreIndex > -1):
            highscoreIndex -= 1
            if(ranked[highscoreIndex] != ranked[highscoreIndex + 1]):
                currentRank -= 1
        if(player[scoreIndex] == ranked[highscoreIndex]):
            yield currentRank 
        else:
            yield currentRank + 1
        scoreIndex += 1

# Program Test
n = int(input())
ranked = list(map(int,input().split()))
m = int(input())
player = list(map(int,input().split()))

print(*climbingLeaderboard(ranked , player) , sep = "\n")