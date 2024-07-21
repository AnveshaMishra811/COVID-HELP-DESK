import csv
state=input("ENTER YOUR STATE")
def hospitals():
    global state
    f=open("zonelist.csv",'r')
    h=csv.reader(f)
    capital=state.upper()
    for row in h:
        if row[1]==state or row[1]==capital:
            print(row[0])
    f.close()

