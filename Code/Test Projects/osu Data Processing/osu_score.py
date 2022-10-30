TH = 384   # Three Hundreds
OH = 22   # One Hundreds
FT = 3   # FifTies
MS = 0     # MisseS

acc = (TH*300+OH*100+FT*50+MS*0)/((TH+OH+FT+MS)*300)
acc_neat = str(round((TH*300+OH*100+FT*50+MS*0)/((TH+OH+FT+MS)*300), 4)*100) + "%"

print(acc_neat, acc)

# Lower Bound

for x in range((TH+OH+FT)-MS):
    hit = 50 + (50*((x*2*1)/25))
        
        