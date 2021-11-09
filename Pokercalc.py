import math
import os
full_deck = ["H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA",
             "D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA",
             "C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA",
             "S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA",]
royal_flush_arr = [["H10","HJ","HQ","HK","HA"],["D10","DJ","DQ","DK","DA"],["C10","CJ","CQ","CK","CA"],
                   ["S10","SJ","SQ","SK","SA"]]
C5_from_50 = 2118760
C2_from_47 = 1081
C1_from_46 = 46
CX_from_N = [C5_from_50, C2_from_47, C1_from_46]
def royal_flush(cards, num):
    C = None
    if(num==0):
        C = 5
    if(num==1):
        C = 2
    if(num==2):
        C = 1
    total_cards = 50-(5-C)
    n = CX_from_N[num]
    scards = set(cards)
    total_count = 0
    real_count = [0,0,0,0]
    for i in range(0,4):
        srfa = set(royal_flush_arr[i])
        equivs = len(scards.intersection(srfa))
        total_count+=equivs
        real_count[i] += equivs
    RF_hearts = 0
    RF_diamonds = 0
    RF_clubs = 0
    RF_spades = 0


    if(C-(5-real_count[0])>=0):
        cn = (5-real_count[0])
        cl = C-cn
        RF_hearts = math.factorial(total_cards-cn)/math.factorial(cl)/math.factorial(total_cards-cn-cl)/n
        
    if(C-(5-real_count[1])>=0):
        cn = (5-real_count[1])
        cl = C-cn
        RF_diamonds = math.factorial(total_cards-cn)/math.factorial(cl)/math.factorial(total_cards-cn-cl)/n
     
    if(C-(5-real_count[2])>=0):
        cn = (5-real_count[2])
        cl = C-cn
        RF_clubs = math.factorial(total_cards-cn)/math.factorial(cl)/math.factorial(total_cards-cn-cl)/n

    if(C-(5-real_count[3])>=0):
        cn = (5-real_count[3])
        cl = C-cn
        RF_spades = math.factorial(total_cards-cn)/math.factorial(cl)/math.factorial(total_cards-cn-cl)/n
 

    return (RF_hearts+RF_diamonds+RF_clubs+RF_spades)



player1 = None
player1 = input("Your 2 hole cards separated by space ex. HA S2 CK: ").split()
cards = player1
curr_deck = full_deck


i = 0
royal_flush_chance = royal_flush(cards, 0) 
print("Royal flush: "+ str(royal_flush_chance) +"\n")