# -*- coding: utf-8 -*-

def name_lenth(player_name):
    namelen = len(player_name)
    count_left = int((10 - namelen)/2)
    count_right = 10 - count_left -namelen
    name = " "*count_left + player_name + " "*count_right
    return name

def table(player1,player2):
    print("-"*34)
    print("|   |  ID  | Player_1 | Player_2 |")
    print("-" * 34)
    print("-" * 34)
    print("|   | Name |"+ name_lenth(player1.name) +"|"+ name_lenth(player2.name) +"|")
    print("-" * 34)
    print("| 1 |  1点 |"+ player1.column["1"]+"|"+ player2.column["1"]+"|\n",end='')
    print("-"*34)
    print("| 2 |  2点 |"+ player1.column["2"]+"|"+ player2.column["2"]+"|\n",end='')
    print("-"*34)
    print("| 3 |  3点 |"+ player1.column["3"]+"|"+ player2.column["3"]+"|\n",end='')
    print("-"*34)
    print("| 4 |  4点 |"+ player1.column["4"]+"|"+ player2.column["4"]+"|\n",end='')
    print("-"*34)
    print("| 5 |  5点 |"+ player1.column["5"]+"|"+ player2.column["5"]+"|\n",end='')
    print("-"*34)
    print("| 6 |  6点 |"+ player1.column["6"]+"|"+ player2.column["6"]+"|\n",end='')
    print("-"*34)
    print("| 奖| ≥63 |"+ player1.column["award"]+"|"+ player2.column["award"]+"|\n",end='')
    print("-"*34)
    print("| 7 |  3+2 |"+ player1.column["7"]+"|"+ player2.column["7"]+"|\n",end='')
    print("-"*34)
    print("| 8 |  4+1 |"+ player1.column["8"]+"|"+ player2.column["8"]+"|\n",end='')
    print("-"*34)
    print("| 9 | 大顺 |"+ player1.column["9"]+"|"+ player2.column["9"]+"|\n",end='')
    print("-"*34)
    print("| 10| 小顺 |"+ player1.column["10"]+"|"+ player2.column["10"]+"|\n",end='')
    print("-"*34)
    print("| 11| 快艇 |"+ player1.column["11"]+"|"+ player2.column["11"]+"|\n",end='')
    print("-"*34)
    print("| 12| 总和 |"+ player1.column["12"]+"|"+ player2.column["12"]+"|\n",end='')
    print("-"*34)
    print("-" * 34)
    print("|   | 总分 |"+ player1.column["13"]+"|"+ player2.column["13"]+"|\n",end='')
    print("-" * 34)

# if __name__ == '__main__':
#     draw()