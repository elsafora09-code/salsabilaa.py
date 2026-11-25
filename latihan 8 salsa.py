print("===== KALKULATOR SCIENTIFIC =====")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")
print("6. Akar Kuadrat")
print("7. Sin")
print("8. Cos")
print("9. Tan")
print("10. Logaritma")
print("0. Keluar")

while True:
    pilih = int(input("\nPilih operasi: "))

    if pilih == 0:
        print("Kalkulator selesai.")
        break

    elif pilih == 1:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        print("Hasil =", a + b)

    elif pilih == 2:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        print("Hasil =", a - b)

    elif pilih == 3:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        print("Hasil =", a * b)

    elif pilih == 4:
        a = float(input("Angka pertama: "))
        b = float(input("Angka kedua: "))
        if b != 0:
            print("Hasil =", a / b)
        else:
            print("Tidak bisa dibagi nol!")

    elif pilih == 5:
        a = float(input("Angka: "))
        print("Hasil =", a ** 2)

    elif pilih == 6:
        a = float(input("Angka: "))
        if a >= 0:
            print("Hasil =", math.sqrt(a))
        else:
            print("Angka tidak boleh negatif!")

    elif pilih == 7:
        a = float(input("Sudut (derajat): "))
        print("Hasil =", math.sin(math.radians(a)))

    elif pilih == 8:
        a = float(input("Sudut (derajat): "))
        print("Hasil =", math.cos(math.radians(a)))

    elif pilih == 9:
        a = float(input("Sudut (derajat): "))
        print("Hasil =", math.tan(math.radians(a)))

    elif pilih == 10:
        a = float(input("Angka: "))
        if a > 0:
            print("Hasil =", math.log10(a))
        else:
            print("Angka harus lebih dari nol!")

    else:
        print("Pilihan tidak tersedia!")