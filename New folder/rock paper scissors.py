play=input("do you want to play answer with 'yes' or 'no' ")
while play=="yes":
    play=input("do yoy want to play")
    player2bot=input("do you have friends to play ROCK PAPER SCISSORS WITH answer with 'yes' or 'no' : ")

    score=""
    player1=input("Player 1 goes answer with 'rock' 'paper' or 'scissors' : ")

    if player2bot=="no":    
        player2="rock"
        print("I understand")
    if player2bot=="yes":
        player2=input("Player 2 goes : ")

    print(player1,"player1")
    print(player2,"player1")
    if player1=="rock" and player2=="paper":
        score+"player1"
    if player1=="paper" and player2=="rock":
        score+"player1"
    if player1=="rock" and player2== "scissors":
        score+"player1"
    if player1=="scissors" and player2=="rock":
        score+"player2"
    if player1=="paper" and player2=="scissors":
        score+"player2"
    if player1=="rock" and player2=="paper":
        score+"player2"
print(score)