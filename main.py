# -*- coding: utf-8 -*-
import random
import time
import draw_table
import column
from player import Player

def printnums(nums,final=False):
    try:
        num_1, num_2, num_3, num_4, num_5 = nums[0],nums[1],nums[2],nums[3],nums[4]
        if final == False:
            print("***您的骰子现在的点数为",num_1, num_2, num_3, num_4, num_5,"***")
        else:
            print("***您的骰子最终的点数为", num_1, num_2, num_3, num_4, num_5, "***")
    except:
        pass

def round(round_player, round_num, player1,player2):
    '''该函数实现回合开始掷骰子阶段'''
    print("{}第{}回合开始".format(round_player.name, round_num))
    time.sleep(1)
    num_1 = random.randint(1, 6)
    num_2 = random.randint(1, 6)
    num_3 = random.randint(1, 6)
    num_4 = random.randint(1, 6)
    num_5 = random.randint(1, 6)
    nums = [num_1, num_2, num_3, num_4, num_5]
    printnums(nums)
    print("能够得分的得分项为:")
    possiblePoint(nums,round_player)
    for i in range(1,3):
        repeat_num(nums,i)
        printnums(nums)
        if i == 1:
            print("能够得分的得分项为:")
            possiblePoint(nums,round_player)
    printnums(nums,final=True)
    time.sleep(2.5)
    draw_table.table(player1,player2)
    print("能够得分的得分项为:")
    possiblePoint(nums,round_player)
    while True:
        id = input("请输入要选择的得分项ID(1至12):")
        if id in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
            if round_player.column[id] != "          ":
                print("该得分项已被填入，请重新输入！")
                continue
            break
        print("输入有误，请重新输入1至12的数字ID")
    whichID(round_player,id,nums)
    try:
        if int(round_player.column["award"].split("(")[1].split(")")[0]) != 35 and int(round_player.column["award"].split("(")[1].split(")")[0]) != 0:
            isAward(round_player)
    except:
        pass
    addAll(round_player)
    draw_table.table(player1, player2)
    print("{}第{}回合结束".format(round_player.name, round_num))
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("------------------------------------------------------")

def possiblePoint(nums,player):
    """该函数实现在控制台提示 确定最终骰子点数后各个得分项能获得的分数"""
    onepoint = column.numberPoint(nums, 1)
    if onepoint != 0 and player.column["1"]=="          ":
        print("★★★1-1点-"+str(onepoint)+"分")
    twopoint = column.numberPoint(nums, 2)
    if twopoint != 0 and player.column["2"]=="          ":
        print("★★★2-2点-"+str(twopoint)+"分")
    threepoint = column.numberPoint(nums, 3)
    if threepoint != 0 and player.column["3"]=="          ":
        print("★★★3-3点-"+str(threepoint)+"分")
    fourpoint = column.numberPoint(nums, 4)
    if fourpoint != 0 and player.column["4"]=="          ":
        print("★★★4-4点-"+str(fourpoint)+"分")
    fivepoint = column.numberPoint(nums, 5)
    if fivepoint != 0 and player.column["5"]=="          " :
        print("★★★5-5点-"+str(fivepoint)+"分")
    sixpoint = column.numberPoint(nums, 6)
    if sixpoint!=0 and player.column["6"]=="          ":
        print("★★★6-6点-"+str(sixpoint)+"分")
    threeaddtwo_point = column.threeAddTwo(nums)
    if threeaddtwo_point != 0 and player.column["7"]=="          ":
        print("★★★7-三带二-"+str(threeaddtwo_point)+"分")
    fouraddone_point = column.fourAddOne(nums)
    if fouraddone_point !=0 and player.column["8"]=="          ":
        print("★★★8-四带一-"+str(fouraddone_point)+"分")
    bigStraight_point = column.bigStraight(nums)
    if bigStraight_point!=0 and player.column["9"]=="          ":
        print("★★★9-大顺子-"+str(bigStraight_point)+"分")
    smallStraight_point = column.smallStraight(nums)
    if smallStraight_point!=0 and player.column["10"]=="          ":
        print("★★★10-小顺子-"+str(smallStraight_point)+"分")
    yahtzee_point = column.yahtzee(nums)
    if yahtzee_point!=0 and player.column["11"]=="          ":
        print("★★★11-快艇-"+str(yahtzee_point)+"分")
    if player.column["12"]=="          ":
        print("★★★12-总和-"+str(column.sum(nums))+"分")
def whichID(round_player,id,nums):
    """该函数实现玩家选择的得分项"""
    if id =="1":
        round_player.column["1"] = draw_table.name_lenth(str(column.numberPoint(nums, 1)))
    if id =="2":
        round_player.column["2"] = draw_table.name_lenth(str(column.numberPoint(nums, 2)))
    if id =="3":
        round_player.column["3"] = draw_table.name_lenth(str(column.numberPoint(nums, 3)))
    if id =="4":
        round_player.column["4"] = draw_table.name_lenth(str(column.numberPoint(nums, 4)))
    if id =="5":
        round_player.column["5"] = draw_table.name_lenth(str(column.numberPoint(nums, 5)))
    if id =="6":
        round_player.column["6"] = draw_table.name_lenth(str(column.numberPoint(nums, 6)))
    if id =="7":
        round_player.column["7"] = draw_table.name_lenth(str(column.threeAddTwo(nums)))
    if id =="8":
        round_player.column["8"] = draw_table.name_lenth(str(column.fourAddOne(nums)))
    if id =="9":
        round_player.column["9"] = draw_table.name_lenth(str(column.bigStraight(nums)))
    if id =="10":
        round_player.column["10"] = draw_table.name_lenth(str(column.smallStraight(nums)))
    if id =="11":
        round_player.column["11"] = draw_table.name_lenth(str(column.yahtzee(nums)))
    if id =="12":
        round_player.column["12"] = draw_table.name_lenth(str(column.sum(nums)))
def isAward(round_player):
    """该函数是判断奖励得分条件是否达成"""
    point = 0
    count = 0
    lists = [round_player.column["1"],round_player.column["2"],round_player.column["3"],round_player.column["4"],round_player.column["5"],round_player.column["6"]]
    for value in lists:
        try:
            num = int(value)
            count += 1
            point = point + num
        except:
            continue
    if count == 6:
        if point >= 63:
            round_player.column["award"] = draw_table.name_lenth("35")
        else :round_player.column["award"] = draw_table.name_lenth("0")
    elif count<6:
        if point >= 63:
            round_player.column["award"] = draw_table.name_lenth("35")
        else:
            minus = point - 63
            round_player.column["award"] = draw_table.name_lenth("(" + str(minus) + ")")
def addAll(round_player):
    """该函数用来计算总得分"""
    point = 0
    dic = round_player.column.copy()
    dic.pop("name")
    dic.pop("13")
    if dic["award"] != "    35    ":
        dic["award"] = "     0    "
    lists = list(dic.values())
    for value in lists:
        try:
            num = int(value)
            point = point + num
        except:
            continue
    round_player.column["13"] = draw_table.name_lenth(str(point))

def repeat_num(nums,count):
    '''该函数实现判断是否重置骰子阶段'''
    print("请选择第{}次要重新投掷骰子的序号（五个骰子的序号分别为1,2,3,4,5。不输入任何字符为不进行重置）".format(count))
    repeat_id = input()
    print("第{}次要重新投掷的序号为:".format(count), repeat_id)
    try:
        nums = repeat(nums, repeat_id)
        time.sleep(1)
    except:
        print("输入格式错误，请重新输入")
        repeat_num(nums,count)
    return nums
def repeat(nums, repeat_id):
    '''该函数实现重置骰子点数过程'''
    assert 0 <= len(repeat_id) < 6
    if len(repeat_id) == 0:
        pass
    else:
        for i in repeat_id:
            nums[int(i) - 1] = random.randint(1, 6)
        return nums

if __name__ == '__main__':
    plaer1name = input("请输入玩家1的名字(10字符以内)：")
    plaer2name = input("请输入玩家2的名字(10字符以内)：")
    player1= Player(plaer1name)
    player2 = Player(plaer2name)
    player1column, player2column= player1.column,player2.column

    for i in range(12):
        round(player1, i+1,player1,player2)
        time.sleep(3)
        round(player2, i+1, player1, player2)
        time.sleep(3)
    if int(player1.column["13"]) > int(player2.column["13"]):
        print("Player1:{}获胜！".format(player1.name))
    elif int(player2.column["13"]) > int(player1.column["13"]):
        print("Player2:{}获胜！".format(player2.name))
    else: print("平局！")
