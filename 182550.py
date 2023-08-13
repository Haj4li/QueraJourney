

# Quera Webpage https://quera.org/problemset/182550/
# Ali Nakhaee 
# https://github.com/Haj4li


# حوصلم نمیشه همشو کامنت بذارم امیدوارم متوجه بشید داره چی رخ میده
# XOXO 

# این پروژه توی کوئرا موقع امتیاز دهی واسش امتیاز صفر رد میشه 
# در حالی که تمام ورودی و خروجی ها یکسان هست 
# نمیدونم مشکل از کده یا سایت کوئرا داغونه واس اینطور موارد
# ب هر حال
# anyway
# $#^@#$@#%#$^&%^$##@$#$%#$

# فشار چیه 

troopid = 0
maxtroops = 50
totaltroops = 0

coins = 500
gitfTimer = 20
giftValue = 180
lastGift = 0


miners = []
maxMiners = 8
waitingMiners = []

prevTime = 0
newTime = 0

dragonHealth = 0


characters = {
    "miner": {
        "tspace" : 1,
        "health" : 100,
        "price": 150,
        "seconds": 10,
        "power":100,
    },
    "swordwrath": {
        "tspace" : 1,
        "health" : 120,
        "price": 125,
        "seconds": 1,
        "power":20,
    },
    "archidon": {
        "tspace" : 1,
        "health" : 80,
        "price": 300,
        "seconds": 1,
        "power":10,
    },
    "spearton": {
        "tspace" : 2,
        "health" : 250,
        "price": 500,
        "seconds": 3,
        "power":35,
    },
    "magikill": {
        "tspace" : 4,
        "health" : 80,
        "price": 1200,
        "seconds": 5,
        "power":200,
    },
    "giant": {
        "tspace" : 4,
        "health" : 1000,
        "price": 1500,
        "seconds": 4,
        "power":150,
    }
}

army = {

}
army_template = {
    "role" : "army",
    "health" : 0,
    "addtime" : 0,
    "lastact" : 0,
}

def calculate_time(timestamp):
    global prevTime
    secs = 0
    timestamp = timestamp.split(":")
    secs += int(timestamp[1])
    secs += int(timestamp[0]) * 60
    prevTime = secs

output = []
inp = input().split(' ')
dragonHealth = int(inp[1])
for i in range(int(inp[0])):
    a = input().split(' ')
    times = a[-1]
    com = a[0]
    calculate_time(times)

    # GAME LOGIC
    if (dragonHealth <= 0):
        output.append("game over")
        continue

    # + MONEY
    dif = int(prevTime / 20)
    if (dif > lastGift):
        coins += dif * giftValue
        lastGift += dif

    # + CHARACTERS
    # -- MINERS
    for m in miners:
        dif = int((prevTime - army[m]["addtime"]) / characters[army[m]["role"]]["seconds"])
        if (dif > army[m]["lastact"]):
            coins += dif * characters[army[m]["role"]]["power"]
            army[m]["lastact"] += dif
    # -- ARMY
    for i in range(1,troopid+1):
        role = army[i]["role"]
        if (role == "miner"):
            pass
        health = army[i]["health"]
        if (health > 0):
            dif = int((prevTime - army[i]["addtime"] - army[i]["lastact"]) / characters[army[i]["role"]]["seconds"])
            if (dif > army[i]["lastact"]):
                dragonHealth -= dif * characters[army[i]["role"]]["power"]
                army[i]["lastact"] += dif

    # + COMMANDS
    if (com == "money-status"):
        output.append(coins)
    elif (com == "enemy-status"):
        output.append(dragonHealth)
    elif (com == "damage"):
        tid = int(a[1])
        if (not tid in army):
            output.append("no matter")
        else:
            if (army[tid]["health"] <= 0):
                output.append("no matter")
                continue
            damage = int(a[2])
            army[tid]["health"] -= damage
            if (army[tid]["health"] <= 0):
                output.append("dead")
                if (army[tid]["role"] == "miner"):
                    if (len(miners) >= maxMiners and len(waitingMiners) > 0):
                        miners.pop(miners.index(tid))
                        miners.append(waitingMiners.pop(-1))
            else:
                output.append(army[tid]["health"])
    elif (com == "army-status"):
        troops = [0,0,0,0,0,0]
        for i in range(1,troopid+1):
            role = army[i]["role"]
            health = army[i]["health"]
            if (health > 0):
                troops[list(characters).index(role)] += 1
        os = ""
        for t in troops:
            os += str(t) + " "
        os = os[:len(os)-1]
        output.append(os)
    elif (com == "add"):
        # ADD TROOP
        if (totaltroops + characters[a[1]]["tspace"] > maxtroops ):
            output.append("too many army")
        elif (coins >= characters[a[1]]["price"]):
            coins -= characters[a[1]]["price"]
            troopid += 1
            if (a[1] == "miner"):
                if (len(miners) >= maxMiners):
                    waitingMiners.append(troopid)
                else:
                    miners.append(troopid)
            totaltroops += characters[a[1]]["tspace"]
            army[troopid] = {
                "role" : a[1],
                "health" : characters[a[1]]["health"],
                "addtime" : prevTime,
                "lastact" : 0,
            }
            output.append(troopid)
        else:
            output.append("not enough money")
    

for c in output:
    print(str(c))