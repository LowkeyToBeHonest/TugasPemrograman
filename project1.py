import datetime
print("Selamat Datang Jangan Lupa Absen Ya Sayang")

def input_nama(nama_absen):
    print("Masukkan nama Anda:")
    nama = input()
    print("Masukkan NIM Anda:")
    nim = input()
    if nama in [nama['nama'] for nama in nama_absen]:
        print(f"{nama} sudah absen hari ini.")
    else:
        nama_absen.append({"nama": nama, "nim": nim, "waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        print(f"{nama} dengan NIM {nim} telah terdaftar dalam daftar absen hari ini pada {datetime.datetime.now().strftime('%H:%M:%S')}.")

def daftar_absen(nama_absen):
    print("Daftar absen hari ini:")
    for i, nama in enumerate(nama_absen, start=1):
        print(f"{i}. {nama['nama']} - NIM: {nama['nim']} - Waktu: {nama['waktu']}")

def reset_absen(nama_absen):
    nama_absen.clear()
    print("Daftar absen telah direset.")

def main():
    nama_absen = []

    while True:
        print("\nMenu Absen:")
        print("1. Input Nama dan NIM")
        print("2. Daftar Absen")
        print("3. Reset Absen")
        print("4. Keluar")
        print("Masukkan pilihan Anda:")
        pilihan = int(input())

        if pilihan == 1:
            input_nama(nama_absen)
        elif pilihan == 2:
            daftar_absen(nama_absen)
        elif pilihan == 3:
            reset_absen(nama_absen)
        elif pilihan == 4:
            print("TERIMA KASIH SUDAH ABSEN, HAVE A NICE DAY")
            print("Quotes Of The Day : Mencintai Tak Harus Memiliki")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

if __name__ == "__main__":
    main()