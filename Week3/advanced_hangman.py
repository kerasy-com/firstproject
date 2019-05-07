import random

# 행맨 모습 출력
hangmanpic = ["""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ HELP
|   |   
|   | 
|  | 
|  | 
|
--------
""",
""""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""
 ]

def hangman():
    
    print("[행맨게임을 시작합니다]")
    
    #txt file에서 불러오기
    # inFile = open('hangmanwords.txt', 'r')
    # words=[]
    # for text in inFile:
    #     words.append(text.strip())
    # print(words)
    # inFile.close()

    # word = random.choice(words).upper()

    # 하드코딩으로 랜덤하게 단어 선택하기
    words = ["hangman", "chairs", "python"]
    word = random.choice(words).upper()
    
    # 그냥 정해진 단어
    # word = "likelion".upper()
    
    now = len(word)*"_"
    wrong_cnt = 0 # 행맨 목숨 만들기

    while wrong_cnt < 9:
        print("======================")
        print("======================")
        print('현재 상태: ' + now)
        print("======================")
        print(hangmanpic[wrong_cnt]) #행맨 그림 출력하기
        print("행맨의 목숨이 {}개 남았습니다".format(9-wrong_cnt))
        guess = str(input("알파벳을 적어주세요: ")).upper()
       
       # 단어 전체 적어서 정답 맞추기
        if guess == word:
            print("벌써 정답을 맞추셨군요. 맞습니다 정답은 {} !!!!".format(guess))
            break

        #글자가 정답에 있을 경우
        if guess in word:
            now = hangman_answer(guess, word, now) #새로운 now!!
            #다 맞췄을 경우
            if now == word:
                print("다 맞췄다!!! 정답은 {}입니다.".format(word))
                break

        #글자가 정답에 없을 경우
        else:
            print("없는 글자입니다")
            wrong_cnt += 1 
            
            #행맨 목숨이 다 없어졌을 경우
            if wrong_cnt == 9:
                print(hangmanpic[wrong_cnt])
                print("GAME OVER 행맨이 죽었어요. 정답은 {}였습니다.".format(word))
                break

#글자랑 정답이랑 맞춰보는 함수
def hangman_answer(guess, word, now):
    result = ''
    for i in range(len(word)):
        #글자가 정답의 i번째 글자와 맞을 때
        if word[i] == guess: 
            result += guess
        #글자가 정답의 i번째 글자와 다를 때
        else:
            if now[i] == '_': #글자가 맞춰져 있지 않을 때
                result += '_'
            else: #글자가 이미 맞춰져 있을 때
                result += now[i]
    return result

hangman()