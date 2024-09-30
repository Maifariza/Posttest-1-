# Masukkan nama anda
nama = (input("Masukkan nama anda: "))

# Masukkan NIM anda
NIM = (input("Masukkan NIM: "))
if NIM == "2409116032":
    print(f"Dengan pengguna NIM {NIM}")
else:
    print(f"NIM yang anda masukkan tidak valid")

# Masukkan Pin anda
Pin = (input("Masukkan Pin (6 angka): "))
if Pin == "001100":
    print(f"Selamat datang, anda telah terdaftar")
else:
    print(f"Pin yang anda masukkan tidak valid")

# Manghitung total harga barang berdasarkan harga jual
def hitung_total_harga():
    while True:
        try:
            harga_barang = float(input("Masukkan harga barang: Rp. "))
            jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")
            continue

        total_harga = harga_barang * jumlah_pembelian

        if total_harga > 250000:
            diskon = total_harga * 0.25
            total_harga = diskon
            print(f"Anda mendapatkan diskon 25%. Total harga setelah diskon: Rp. {total_harga:.2f}")
        else:
            print(f"Total harga: Rp. {total_harga:.2f}")

        pilihan = input("Apakah Anda ingin menghitung total harga lagi? (ya/tidak): ").lower()
        if pilihan != 'ya':
            break

hitung_total_harga()
