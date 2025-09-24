def calculate_love_score(name1, name2):

    sum_1 = 0
    for letter in "TRUE":
        total=0
        for letter1 in name1:
            if letter==letter1:
                total+=1
        for letter2 in name2:
            if letter==letter2:
                total+=1
        print(f"{letter} occurs {total} times.")
        sum_1+=total

    print()

    sum_2 = 0
    for letter in "LOVE":
        total=0
        for letter1 in name1:
            if letter==letter1:
                total+=1
        for letter2 in name2:
            if letter==letter2:
                total+=1
        print(f"{letter} occurs {total} times.")
        sum_2+=total

    print(f"\n{sum_1}{sum_2}")
calculate_love_score("Kanye West".upper(),"Kim Kardashian".upper())