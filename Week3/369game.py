def how_many_three(number):
    count = 0
    
    for data in number:
        if (data == "3") or (data == "6") or (data == "9"):
            count += 1
    
    return count

def number_or_clap(number):
    clap = how_many_three(str(number))
    answer = ""
    if clap == 0:
        answer = answer + str(number)
    else:
        answer = answer + "짝" * clap
    
    return answer

list = []

num_player = int(input("Input the number of other players: "))
for i in range(1, num_player+1):
    player_name = "Player" + str(i)
    list.append(player_name)

list.append("Human")

start = 1
while True:
    for item in list:
        if item != "Human":
            print(item, ": ", number_or_clap(str(start)))
        else:
            answer = input("You: ")
            if answer != number_or_clap(str(start)):
                print("You got it wrong!")
                start = 0
                break
        start += 1
    if(start == 0):
        break

print("You Suck!")