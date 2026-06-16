def tambah_transaksi(data, array):

    print("--- INPUT TRANSAKSI LAUNDRY ---")
    nama = input("Masukkan Nama Pelanggan: ")
    berat = float(input("Masukkan Berat Laundry (Kg): "))
    print("Pilihan Paket: 1. Reguler (Rp 6.000) | 2. Ekspres (Rp 10.000)")


    input_valid = False
    while input_valid == False:
        pilihan = input("Pilih Paket (1/2): ")
        
        if pilihan == "1":
            paket = "Reguler"
            harga_per_kg = 6000
            input_valid = True
            
        elif pilihan == "2":
            paket = "Ekspres"
            harga_per_kg = 10000
            input_valid = True
            
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1 atau 2.")
            print()
        

    harga_dasar = berat * harga_per_kg    
    
    member_valid = False
    while member_valid == False:
        member = input("Punya kartu member? (ya/tidak): ")
        
        if member == "ya":
            diskon = harga_dasar * 0.10
            total_harga = harga_dasar - diskon
            member_valid = True
            
        elif member == "tidak":
            total_harga = harga_dasar
            member_valid = True
            
        else:
            
            print("Pilihan tidak valid! Silakan masukkan 'ya' atau 'tidak'.")
            print()
            
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


def hitung_pendapatan(data, jumlah):
    print()
    print("--- TOTAL PENDAPATAN ---")
    if jumlah == 0:
        print("Belum ada data transaksi.")
        print()
        return
    
    total = 0
    for i in range(jumlah):
        total += data[i][4]
    print(f"Total Pendapatan: Rp {total}")
    print()

def cari_transaksi(data, jumlah):
    print()
    print("--- FITUR CARI & URUTKAN TRANSAKSI ---")
    if jumlah == 0:
        print("Belum ada data transaksi.")
        print()
        return
    
    print("Pilih Operasi: 1. Pencarian (Search) | 2. Pengurutan (Sort)")
    operasi = input("Pilih (1/2): ")
    
    if operasi == "1":
        print()
        print("Pencarian Berdasarkan:")
        print("1. ID Transaksi")
        print("2. Nama Pelanggan")
        print("3. Jenis Paket")
        print("4. Status Laundry")
        pilihan_cari = input("Pilih (1-4): ")
        
        found = False
        
        if pilihan_cari == "1":
            id_cari = int(input("Masukkan ID Transaksi: "))
            for i in range(jumlah):
                if data[i][0] == id_cari:
                    found = True
                    print(f"ID: {data[i][0]} | Nama: {data[i][1]} | Berat: {data[i][2]}Kg | Paket: {data[i][3]} | Total: Rp {data[i][4]} | Status: {data[i][5]}")
                    
        elif pilihan_cari == "2":
            nama_cari = input("Masukkan Nama Pelanggan: ")
            for i in range(jumlah):
                if data[i][1] == nama_cari:
                    found = True
                    print(f"ID: {data[i][0]} | Nama: {data[i][1]} | Berat: {data[i][2]}Kg | Paket: {data[i][3]} | Total: Rp {data[i][4]} | Status: {data[i][5]}")
                    
        elif pilihan_cari == "3":
            paket_cari = input("Masukkan Jenis Paket (Reguler/Ekspres): ")
            for i in range(jumlah):
                if data[i][3] == paket_cari:
                    found = True
                    print(f"ID: {data[i][0]} | Nama: {data[i][1]} | Berat: {data[i][2]}Kg | Paket: {data[i][3]} | Total: Rp {data[i][4]} | Status: {data[i][5]}")
                    
        elif pilihan_cari == "4":
            status_cari = input("Masukkan Status (Antrean/Diproses/Selesai): ")
            for i in range(jumlah):
                if data[i][5] == status_cari:
                    found = True
                    print(f"ID: {data[i][0]} | Nama: {data[i][1]} | Berat: {data[i][2]}Kg | Paket: {data[i][3]} | Total: Rp {data[i][4]} | Status: {data[i][5]}")
        else:
            print("Pilihan menu pencarian tidak valid.")
            return

        if found == False:
            print("Data yang Anda cari tidak ditemukan.")
            
    elif operasi == "2":
        print()
        print("Pengurutan Berdasarkan:")
        print("1. Harga Terbesar ke Terkecil")
        print("2. Harga Terkecil ke Terbesar")
        print("3. Berat Terberat ke Teringan")
        print("4. Berat Teringan ke Terberat")
        pilihan_sort = input("Pilih (1-4): ")
        
        if pilihan_sort != "1" and pilihan_sort != "2" and pilihan_sort != "3" and pilihan_sort != "4":
            print("Pilihan menu pengurutan tidak valid.")
            return
        
        data_copy = [[None] * kolom for p in range(jumlah)]
        for i in range(jumlah):
            for j in range(kolom):
                data_copy[i][j] = data[i][j]
        
        for p in range(1, jumlah, 1):
            tem = data_copy[p]
            i = p - 1
            
            while (pilihan_sort == "1" and i >= 0 and tem[4] > data_copy[i][4]) or (pilihan_sort == "2" and i >= 0 and tem[4] < data_copy[i][4]) or (pilihan_sort == "3" and i >= 0 and tem[2] > data_copy[i][2]) or (pilihan_sort == "4" and i >= 0 and tem[2] < data_copy[i][2]):
                
                data_copy[i + 1] = data_copy[i]
                i = i - 1 
                
            data_copy[i + 1] = tem
                
        print()
        print("--- HASIL PENGURUTAN DATA ---")
        for i in range(jumlah):
            print(f"ID: {data_copy[i][0]} | Nama: {data_copy[i][1]} | Berat: {data_copy[i][2]}Kg | Paket: {data_copy[i][3]} | Total: Rp {data_copy[i][4]} | Status: {data_copy[i][5]}")
            
    else:
        print("Pilihan operasi tidak valid.")
    print()

# Kamus Data
# data: array 2 dimensi untuk menyimpan data transaksi
# array: array penunjuk (array[0] = jumlah transaksi, array[1] = ID berikutnya)
# id_cari: ID transaksi yang akan dihapus(int)
# found: penanda apakah data ditemukan(boolean)
# i: indeks utk pencarian data(int)
# j: indeks utk menggeser data(int)
# k: indeks kolom array 2 dimensi(int)
def hapus_transaksi(data, array):
    print()
    print("--- HAPUS DATA TRANSAKSI ---")
    if (array[0] == 0):
        print("Belum ada data transaksi yang bisa dihapus.")
        print()
        return
    
    id_cari = int(input("Masukkan ID Transaksi yang ingin dihapus: "))
    
    found = False
    for i in range(array[0]):
        if (data[i][0] == id_cari and found == False):
            found = True
            
            for j in range(i, array[0] - 1):
                for k in range(kolom):
                    data[j][k] = data[j + 1][k]
                    
            for k in range(kolom):
                data[array[0] - 1][k] = [None]
            array[0] -= 1
            print("Data transaksi berhasil dihapus!")
    if (found == False):
        print("ID transaksi tidak ditemukan.")
    print()

def main():
    baris = 100
    
    data_transaksi = [[None] * kolom for i in range(baris)]
    array = [0, 1] 
    program_berjalan = True
    while program_berjalan == True:
        print("=== SYSTEM MANAJEMEN LAUNDRY ===")
        print("1. Input Transaksi Baru")
        print("2. Melihat Semua Transaksi")
        print("3. Update Status Transaksi")
        print("4. Total Pendapatan")
        print("5. Cari atau Urutkan Transaksi")
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
    kolom = 6
    main()