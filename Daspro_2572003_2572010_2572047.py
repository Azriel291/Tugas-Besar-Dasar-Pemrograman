def tambah_transaksi(data, array):

    print("--- INPUT TRANSAKSI LAUNDRY ---")
    nama = input("Masukkan Nama Pelanggan: ")
    berat = float(input("Masukkan Berat Laundry (Kg): "))
    print("Pilihan Paket: 1. Reguler (Rp 6.000) | 2. Ekspres (Rp 10.000)")
    pilihan = input("Pilih Paket (1/2): ")
    
    if pilihan == "1":
        paket = "Reguler"
        harga_per_kg = 6000
    else:
        paket = "Ekspres"
        harga_per_kg = 10000

    harga_dasar = berat * harga_per_kg    
    member = input("Punya kartu member? (ya/tidak): ")
    
    if member == "ya":
        diskon = harga_dasar * 0.10
        total_harga = harga_dasar - diskon
    else:
        total_harga = harga_dasar
    status = "Antrean"

    jumlah = array[0]
    id = array[1]
    data[jumlah][0] = id
    data[jumlah][1] = nama
    data[jumlah][2] = berat
    data[jumlah][3] = paket
    data[jumlah][4] = total_harga
    data[jumlah][5] = status
    array[0] += 1
    array[1] += 1
    print("Transaksi berhasil ditambahkan!")
    print()

def tampilkan_transaksi(data, jumlah):
    print()
    print("--- DATA SEMUA TRANSAKSI ---")
    if jumlah == 0:
        print("Belum ada data transaksi.")
        print()
        return
    
    for i in range(jumlah):
        print(f"ID: {data[i][0]} | Nama: {data[i][1]} | Berat: {data[i][2]}Kg | Paket: {data[i][3]} | Total: Rp {data[i][4]} | Status: {data[i][5]}")
    print()
    
def update_transaksi(data, jumlah):
    print()
    print("--- UPDATE STATUS TRANSAKSI ---")
    if jumlah == 0:
        print("Belum ada data transaksi yang bisa diubah.")
        print()
        return
    
    id_cari = int(input("Masukkan ID Transaksi yang ingin diupdate: "))
    found = False
    for i in range(jumlah):
        if (data[i][0]) == id_cari:
            found = True
            print(f"Data ditemukan! Status saat ini: {data[i][5]}")
            print("Pilihan Status Baru: 1. Antrean | 2. Diproses | 3. Selesai")
            pil_status = input("Pilih (1/2/3): ")

            if pil_status == "1":
                data[i][5] = "Antrean"
                print(f"Status transaksi ID {id_cari} berhasil diperbarui menjadi 'Antrean'!")
            elif pil_status == "2":
                data[i][5] = "Diproses"
                print(f"Status transaksi ID {id_cari} berhasil diperbarui menjadi 'Diproses'!")
            elif pil_status == "3":
                data[i][5] = "Selesai"
                print(f"Status transaksi ID {id_cari} berhasil diperbarui menjadi 'Selesai'!")
            else:
                print("Pilihan status tidak valid. Status tidak diubah.")

    if found == False:
        print(f"Transaksi dengan ID {id_cari} tidak ditemukan.")
    print()


def main():
    baris = 100
    kolom = 6
    data_transaksi = [[None] * kolom for i in range(baris)]
    array = [0, 1] #penjelasan(biargasalah): array[0] = sebagai jumlah transaksi | array[1] = sebagai counter(id)
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
            tambah_transaksi(data_transaksi, array)
        elif pilihan == "2":
            tampilkan_transaksi(data_transaksi, array[0])
        elif pilihan == "3":
            update_transaksi(data_transaksi, array[0])
        elif pilihan == "4":
            hitung_pendapatan(data_transaksi, array[0])
        elif pilihan == "5":
            cari_transaksi(data_transaksi, array[0])
        elif pilihan == "6":
            hapus_transaksi(data_transaksi, array)
        elif pilihan == "7":
            print("Semoga Sukses!")
            program_berjalan = False
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            print()
if __name__ == '__main__':
    main()