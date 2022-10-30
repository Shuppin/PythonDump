
print("Enter student score and name sepearated by a comma (e.g. 12, Bob)")

def write_list(scores, names):
    i = 0
    while True:
        try:
            score = input("Enter student " + str(i+1) + " details: ")
            score = score.replace(" ", "")
            score = score.split(",")
            if score[0] == "x":
                break
            if len(score) == 1:
                print("Invalid value")
                continue
            scores.append(int(score[0]))
            names.append(score[1])
            i += 1
        except ValueError:
            print("Invalid value")
        print("List set")

        return scores, names


# save(append, override), search, output

while True:
    try:
        choice = int(input("> "))
        if 0 < choice < 4:
            break
        print("Invalid choice")
    except ValueError:
        print("Invalid value")

if choice == 1:
    write = input("Do you want to override then list or append to the list?")
    if write.lower().startswith("over"):
        scores, names = write_list(list(), list())
        list_made = True


if choice == 2:
    search = input("Do you want to search by name or score?")
if list_made == True:
    if choice == 3:
        for i in range(0,len(scores)):
            print(str(scores[i]) + ",", names[i])

        print("--- Extra Info ---")

        ave = sum(scores)/len(scores)
        
        print("Average score:", ave)
        print("Highest score:", names[scores.index(max(scores))].lower().capitalize() + ",", max(scores))
        print("Lowest score:", names[scores.index(min(scores))].lower().capitalize() + ",", min(scores))
else:
    print(">:(")