
symbol = {
    1 : "I",
    5 : "V",
    10 : "X"
}
_keys = list(symbol.keys())
for x in range(1,20+1):
    if x in symbol:
        print(x)
    else:
        # pick off_part
        pick = ""
        for e,i in enumerate(_keys):
            if x > i and x < _keys(e+1):
                pick = i
            # else:
            #     if  

        diff = x - pick
        temp = ""
        for _item in range(diff):
            temp += symbol(pick)

import math
class Roman:
    # Python 3 program to convert integer
    # number to Roman values

    def integerToRoman(A):
        romansDict = \
            {
                1: "I",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M",
                5000: "G",
                10000: "H"
            }

        div = 1
        while A >= div:
            div *= 10

        div /= 10

        res = ""

        while A:

            # main significant digit extracted
            # into lastNum
            lastNum = int(A / div)

            if lastNum <= 3:
                res += (romansDict[div] * lastNum)
            elif lastNum == 4:
                res += (romansDict[div] +
                            romansDict[div * 5])
            elif 5 <= lastNum <= 8:
                res += (romansDict[div * 5] +
                (romansDict[div] * (lastNum - 5)))
            elif lastNum == 9:
                res += (romansDict[div] +
                            romansDict[div * 10])

            A = math.floor(A % div)
            div /= 10
            
        return res

    # Driver code
    # print("Roman value for the integer is:"
    # 				+ str(integerToRoman(3549)))

    print("Roman value for the integer is:"
                    + str(integerToRoman(4)))
