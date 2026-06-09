def tambah_transaksi(data, id_cnt):
    print("--- INPUT TRANSAKSI LAUNDRY ---")
    nama = input("Masukkan Nama Pelanggan: ")
    berat = float(input("Masukkan Berat Laundry (Kg): "))
    print("Pilihan Paket: 1. Reguler (Rp 6.000) | 2. Eksprex (Rp 10.000)")
    pilihan = input("Pilih Paket (1/2): ")
    if (pilihan == "1"):
        paket = "Reguler"
        harga_per_kg = 6000
    else:
        paket = "Ekspres"
        harga_per_kg = 10000
    harga_dasar = berat * harga_per_kg
    is_member = input("Punya kartu member? (ya/tidak): ")
    if (is_member == "ya"):
        diskon = harga_dasar * 0.10
        total_harga = harga_dasar - diskon
    else:
        total_harga = harga_dasar
    status = "Antrean"
    transaksi_baru = [id_cnt, nama, berat, paket, total_harga, status]
    data = data + [transaksi_baru]
    id_cnt += 1
    print("Transaksi berhasil ditambahkan!")
    print()
    return data, id_cnt

def tampilkan_transaksi(data):
    print()
    print("--- DATA SEMUA TRANSAKSI ---")
    if (data == []):
        print("Belum ada data transaksi.")
        print()
        return
    for t in data:
        print(f"ID: {t[0]} | Nama: {t[1]} | Berat: {t[2]}Kg | Paket: {t[3]} | Total: Rp {t[4]} | Status: {t[5]}")
    print()


def main():
    data_transaksi = []
    id_counter = 1
    program_berjalan = True
    while program_berjalan == True:
        print("=== SYSTEM MANAJEMEN LAUNDRY ===")
        print("1. Input Transaksi Baru")
        print("2. Melihat Semua Transaksi")
        print("3. Update Status Transaksi")
        print("4. Total Pendapatan")
        print("5. Cari Transaksi")
        print("6. Hapus Data")
        print("7. Keluar")
        pilihan = input("Pilih Menu (1-7): ")
        if pilihan == "1":
            data_transaksi, id_counter = tambah_transaksi(data_transaksi, id_counter)
        elif pilihan == "2":
            tampilkan_transaksi(data_transaksi)
        elif pilihan == "3":
            data_transaksi = update_transaksi(data_transaksi)
        elif pilihan == "4":
            hitung_pendapatan(data_transaksi)
        elif pilihan == "5":
            cari_transaksi(data_transaksi)
        elif pilihan == "6":
            data_transaksi = hapus_transaksi(data_transaksi)
        elif pilihan == "7":
            print("Semoga Sukses!")
            program_berjalan = False
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            print()
if __name__ == '__main__':
    main()