student = [ 
#       sid   snme cls dv
        "100 Rahul 8th 2",
        "200 Ramesh 9th 3",
        "300 suresh 10th 1",
]        
m =3
stud_pun = [
    #   no PID sid
        "1 101 200",
        "2 101 200",
        "3 201 100",
        "4 201 100",
        "5 301 300",
]
x=5
pun = [
    "101 unpolished_shoes",
    "201 Dirty_uniform",
    "301 Civil_dress",
    "401 undicipline_behaviour"
]
y=4
from collections import Counter

# map student data to object
def listOfPunishedStudents(m,x,y, student, stud_pun, punishment):
    pun = punishment
    student_obj = {} 
    for x in student:
        sid,name,clas,div = x.split(" ")
        student_obj[sid] = {'name':name}

    pun_obj = {}
    for x in pun:
        pid,desc = x.split(" ")
        pun_obj[pid]=desc

    temp = {}
    for x in stud_pun:
        no,pid,sid = x.split(" ")
        if pid not in temp:
            temp[pid] = []
        temp[pid].append(sid)

    result = []
    for k,v in temp.items():
        count_val = dict(Counter(v))
        print(k,"",v)
        #print your string here creatte it from the above tables
        for sid in count_val:
            if count_val[sid]>1:
                _s = f"{student_obj[sid]['name']}-{pun_obj[k]}"
                print(_s)
                result.append([sid,_s])

    result = sorted(result,key=lambda x:x[0])  
    result = [x[1] for x in result]             
    return "#".join(result)

def main():
    m = int(input()) 
    x = int(input())
    y = int(input())   

    student = []
    for i in range(m):
        s = input()
        student.append(s)
    stud_pun = []
    for i in range(x):
        s = input()
        stud_pun.append(s)
    punishment = []
    for i in range(y):
        s = input() 
        punishment.append(s)   
    z= listOfPunishedStudents(m,x,y, student, stud_pun, punishment)     
    print(z)
    return z

listOfPunishedStudents(m,x,y, student, stud_pun, pun)    

        