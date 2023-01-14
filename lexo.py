from audioop import reverse
from typing import final


s="3294"
def reverse(z):
    return z[::-1]

def solution(s):
    x_high = ""
    y_low = ""
    for e,x in enumerate(s):
        y=x
        if e==0:
            x_high = y_low = x
        else:
            pre_x = f"{x}{x_high}"
            pos_x = f"{x_high}{x}"
            final_x = pre_x if int( pre_x)>int(pos_x) else pos_x
            pre_y = f"{y}{y_low}"
            pos_y = f"{y_low}{y}"
            final_y = pre_y if int(pre_y)<int(pos_y) else pos_y
            x_high=final_x
            y_low=final_y
    return x_high+reverse(y_low), x_high, y_low   

# Case, 3294
# x="",y=""
# x=3,y=3
# x=32,y=23
# x=932, y=239
# 

        