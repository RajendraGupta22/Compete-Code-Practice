"""
At space statsion ,stff is communication about a movie 'love and janice'
but they are smart and texting in encrypted way
where all small letters are replace with theier reverse index of letter
special chars and uppercase are ignored

"""

import string
def solution(x):
    # Your code here
    result = ""
    az = string.ascii_lowercase
    za = az[::-1]
    for s in x:
         val = s
         if s in za:
             idx = za.index(s)
             val = az[idx]
         result += val
    return result


print( solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?") )
print( solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!") )
