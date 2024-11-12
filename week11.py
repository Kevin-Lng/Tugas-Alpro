import math
import time

def tampilan():
    print("-- Pilih Bangun Datar --")
    print("1. Persegi Panjang (Hitung Panjang)")
    print("2. Persegi Panjang (Hitung Lebar)")
    print("3. Persegi")
    print("4. Lingkaran")
    return input("Pilih opsi Anda (1-4): ")

def persegi_panjang_mencari_panjang():
    lebar = int(input("Masukkan Lebar: "))
    keliling = int(input("Masukkan Keliling: "))
    luas = int(input("Masukkan Luas: "))
    start_time = time.perf_counter()  
    panjang_dari_keliling = (keliling / 2) - lebar
    panjang_dari_luas = luas / lebar
    end_time = time.perf_counter() 
    duration = end_time - start_time
    print("\nDiketahui:")
    print("Lebar:", lebar)
    print("Keliling:", keliling)
    print("Luas:", luas)
    print("Hasil Panjang (dari Keliling):", panjang_dari_keliling)
    print("Hasil Panjang (dari Luas):", panjang_dari_luas)
    print(f"Waktu Eksekusi: {duration:.10f} detik")

def persegi_panjang_mencari_lebar():
    panjang = int(input("Masukkan Panjang: "))
    keliling = int(input("Masukkan Keliling: "))
    luas = int(input("Masukkan Luas: "))
    start_time = time.perf_counter()  
    lebar_dari_keliling = (keliling / 2) - panjang
    lebar_dari_luas = luas / panjang
    end_time = time.perf_counter() 
    duration = end_time - start_time
    print("\nDiketahui:")
    print("Panjang:", panjang)
    print("Keliling:", keliling)
    print("Luas:", luas)
    print("Hasil Lebar (dari Keliling):", lebar_dari_keliling)
    print("Hasil Lebar (dari Luas):", lebar_dari_luas)
    print(f"Waktu Eksekusi: {duration:.10f} detik")

def persegi():
    luas = int(input("Masukkan Luas: "))
    keliling = int(input("Masukkan Keliling: "))
    start_time = time.perf_counter()  
    sisi_dari_luas = math.sqrt(luas)
    sisi_dari_keliling = keliling / 4
    end_time = time.perf_counter() 
    duration = end_time - start_time
    print("\nDiketahui:")
    print("Luas:", luas)
    print("Keliling:", keliling)
    print("Sisi Persegi (dari Luas):", sisi_dari_luas)
    print("Sisi Persegi (dari Keliling):", sisi_dari_keliling)
    print(f"Waktu Eksekusi: {duration:.10f} detik")

def lingkaran():
    luas = int(input("Masukkan Luas: "))
    keliling = int(input("Masukkan Keliling: "))
    start_time = time.perf_counter()  
    jari_jari_dari_luas = math.sqrt(luas / math.pi)
    jari_jari_dari_keliling = keliling / (2 * math.pi)
    end_time = time.perf_counter()
    duration = end_time - start_time
    print("\nDiketahui:")
    print("Luas:", luas)
    print("Keliling:", keliling)
    print("Jari-jari Lingkaran (dari Luas):", jari_jari_dari_luas)
    print("Jari-jari Lingkaran (dari Keliling):", jari_jari_dari_keliling)
    print(f"Waktu Eksekusi: {duration:.10f} detik")

while True:
    pilihan = tampilan()
    if pilihan == "1":
        persegi_panjang_mencari_panjang()
    elif pilihan == "2":
        persegi_panjang_mencari_lebar()
    elif pilihan == "3":
        persegi()
    elif pilihan == "4":
        lingkaran()
    else:
        print("Pilihan tidak valid, coba lagi!")
    
    lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ")
    if lanjut != "y":
        print("Terima kasih telah menggunakan program ini!")
        break