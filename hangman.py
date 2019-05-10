import random

def hangman_random():
    with open("hangman_words.txt","r") as file:
        list=file.read().split("\n")
        hangman(list[random.randint(0,len(list)-1)])

def hangman(word):
    wrong=0        #プレイヤーが間違えた数
    stages=["",    #吊り絵
            "_____",
            "|",
            "|    |",
            "|    0",
            "|   /|\ ",
            "|   / \ ",
            "|",
            ]
    rletters=list(word)    #お題を文字ごとにバラバラにしたリスト
    board=["_"]*len(word)  #ヒントの文字リスト
    win=False              #プレイヤーの勝利判定
    print("welcome to ようこそハングマン")


    while True:

        print("\n".join(stages[:wrong+1]))
        print(" ".join(board))

        if wrong>=len(stages)-1:
            break

        if not "_" in board:
            win=True
            break
        
        cha=input("１文字を予想してね:")
        if cha in rletters:
            i=rletters.index(cha)
            board[i]=rletters[i]
            rletters[i]="x"
            print("正解")
        else:
            wrong+=1
            print("残念")

    if win:
        print("おめでとう。あなたの勝ち")
    else:
        print("あなたの負け")
        print("正解は{}".format(word))
