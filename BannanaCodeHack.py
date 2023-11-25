
# Problem : 
# Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in H hours.

# Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile.

# If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards come back.

# Return the minimum integer K such that she can eat all the bananas within H hours.
# speed <= 1000, for test used 100

# Input: piles = [30,11,23,4,20], H = 6
# output : 23


# Input: piles = [3,6,7,11], H = 8
# Output: 4




from copy import deepcopy
def solution(piles, h):
    p = deepcopy(piles)
    start_speed = 1
    min_speed = 0
    for speed in range( start_speed, 100):
        time_to_eat = 0
        print("##############################")
        for bannana in p:
            total_bannana = bannana
            while total_bannana > 0:
                total_bannana = total_bannana - speed
                time_to_eat+=1
            print(speed," : time_to_eat : ",time_to_eat) # since time took is more increase speed
            if time_to_eat >= h: # for loop break for bannana
                break
        if bannana == p[-1] and time_to_eat<=h : # last banna is consumed
            min_speed += speed
            break
    print("result is : ", min_speed)
    return min_speed    
   

# piles = [30,11,23,4,22]
# h = 6


piles = [30,11,23,4,20]
h = 6

# piles = [3,6,7,11]
# h = 8

solution( piles, h)          

"""
Author : Rajendra Gupta
Date : 25 Nov 2023
desc : came across at code-gladiator practice/fun/study

analysis : applied brute-force approach to compute the result speed

overcome-challenge : Yes
solution : 1. took some understanding to debug and analyze the resource
           2. rather than iteration the whole array/list
           3. iterated in chunks
           4. resolved the issue and worked effectively

FEEDBACK : higly appreciated share on my github, would try my best to revert !

"""

