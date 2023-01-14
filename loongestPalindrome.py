
from collections import Counter
def cal2(a:str)->int:
    z = Counter(a)
    result = 0
    flag_od = 0
    for k,v in z.items():
        if v%2==0:
            result+=v
        else:
            if flag_od == 0:
                flag_od =1    
                result = result+v
            else:    
                result = result+v-1   
    return result


