import pickle
with open ("sports.dat", "wb") as F1:
    while True:
        op = int(input("Enter 1 to add data and 0 to quit = "))
        if (op == 1):
            event = input ("Enter Event Name : ")
            location = input ("Enter Location : ")
            participantNo = int (input("Enter Participant No. : "))
            pickle.dump([event,location,participantNo], F1)
        elif op == 0:
            break
F1 = open ("sports.dat","rb")
dict = {}
while True:
    try:
        l = pickle.load(F1)
        dict.update({l[0]:l[2]})

        print(dict)
    except EOFError:
        print("No Entry Found")
        break
F1.close()