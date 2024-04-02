#Perhitungan
division= 1000
num3 =0
print("=======Masukkan Watt masing-masing alat listrik dirumah========")
while True:
    sum = input("Masukkan angka (ketik 'stop' untuk berhenti): ")
    if sum.lower() == 'stop':
        break
    print("====Masukkan Penggunaan alat listrik dirumah per jam====")
    sum2 = input("Masukkan angka kedua(ketik 'stop' untuk berhenti): ")
    lenght=float(sum)+float(sum2)
    num3 +=lenght/division
    print("Total penggunaan:", num3,"Kwh")
    

    
        


