
# Quera Webpage https://quera.org/problemset/183351/

months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]
weekDays = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]

output = []
t = int(input())

def dcalculate(m,d):
    if (m <= 5):
        days = 31
    elif (m <= 10):
        days = 30
    else:
        days = 29
    return days - d

for i in range(t):
    index = 0
    mindex = 0
    day = 0

    inpScenario = input().split(" ")
    inpWhat = input().split(" ")
    
    index = weekDays.index((inpScenario[2]))
    mindex = months.index((inpScenario[1]))
    day = int(inpScenario[0])

    targetm = months.index(inpWhat[1])
    targetd = int(inpWhat[0])

    # رسیدن به تارگت
    reversed = False
    if (mindex > targetm or (mindex == targetm and day > targetd)):
        tmp = mindex
        mindex = targetm
        targetm = tmp
        tmp = targetd
        targetd = day
        day = tmp
        reversed = True

    if (mindex != targetm): 
        days = dcalculate(mindex,day) + targetd
    else:
        days = targetd - day
    mindex += 1

    
    tmp = mindex
    for mindex in range(tmp,targetm):
        if (mindex <= 5):
            days += 31
        elif (mindex <= 10):
            days += 30
        else:
            days += 29
   

    for b in range(days):
        if (reversed):
            if (index > 0):
                index -= 1
            else:
                index = len(weekDays) - 1
        else:
            if (index < len(weekDays)-1):
                index += 1
            elif (index >= len(weekDays)-1):
                index = 0
    output.append(weekDays[index])

for o in output:
    print(o)


