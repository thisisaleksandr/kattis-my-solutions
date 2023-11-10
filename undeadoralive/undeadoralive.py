a = input()
if ":)" in a:
    if ":(" in a:
        print("double agent")
    else:
        print("alive")
elif ":(" in a:
    print("undead")
else:
    print("machine")