print("VitaminD's checks")

print("This is a skillcheck, simply deflect")

support_ops = ["Thermite", "Mute","Doc", "Ace"]
for i in support_ops:
    print ("Support op to bring: ",i) 


#bank of variables for ign's, increasing k/d, all values are taken from R6 tracker as of May 1st, 2023 at 10am EST

tag_johnny = "JonnyBoy05, likely Kapkan"
    #k/d: 0.58, Bronze V
tag_le_Bleu = "andzilla07, likely Alibi :/"
    #k/d: 0.76, Gold IV
tag_Jacob = "jacoby1324, likely Hibana"
    #k/d: 0.79, Gold III
tag_danny = "DannyHany, likely Oryx"
    #k/d: 1.00, Silver II
tag_yousef = "temp-3.141592..., likely Bandit"
    #k/d: 1.01, Silver II
tag_yianni = "VitaminD, likely Thermite"
    #k/d: 1.35, PLat I
tag_kiro = "KYultimate, likely Yager "
    #k/d: 1.46, Gold I
kd_too_high = "k/d is too high, these mfs aint that good"



def kd_check (kill_death_ratio: float):
    if kill_death_ratio <= 0.60:
        return tag_johnny
    elif 0.61 <= kill_death_ratio <= 0.78:
        return tag_le_Bleu
    elif 0.79 <= kill_death_ratio <= 0.81:
        return tag_Jacob
    elif 0.82 <= kill_death_ratio <= 1.00:
        return tag_danny
    elif 1.01 <= kill_death_ratio <= 1.10:
        return tag_yousef
    elif 1.11 <= kill_death_ratio <= 1.40:
        return tag_yianni
    elif 1.41 <= kill_death_ratio <=1.60:
        return tag_kiro
    else:
        return kd_too_high

def paradia (kill_death_ratio: float):
    x = (kill_death_ratio + 0.01) - (kill_death_ratio)
    if kill_death_ratio %2 == 0:
        return "Diamagnetic"
    else:
        return "Paramagnetic"

close = ""
Done = "N" or "n"

while close != Done:

    kill_death_ratio = float(input("Enter ratio to two decimal spaces: "))
    kd_tag_identifier = kd_check(kill_death_ratio) 

    W_or_L = "L"
    if kill_death_ratio >= 1.00:
        W_or_L = "W"

    skill_check = (kd_tag_identifier, W_or_L )
    print(skill_check)
    close = input("Would you like to continue? Y/N ")