with open("soal.txt", "r") as soal:
    for i in soal:
        j = i.split(" || ")
        print(j[0])
        jawab = input("Jawaban: ")
        if jawab.lower() == j[1].strip().lower():
            print("Jawaban Benar!")
        else:
            print("Jawaban Salah!")