def menu_utama():
    print("\n===============================")
    print(" PROGRAM PENGELOLAAN BARANG")
    print("===============================")
    print("1. Pengolahan Data Barang")
    print("2. Lihat Data Barang")
    print("3. Kasir")
    print("4. History Transaksi")
    print("0. Keluar")

def menu_pengolahan():
    print("\n=== PENGOLAHAN DATA BARANG ===")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Edit Barang")
    print("0. Kembali")

def rupiah(angka):
    return "Rp{:,.0f}".format(angka).replace(",", ".")

def baca_barang():
    data = []
    try: #Dibantuin copilot
        file = open("barang.txt", "r")
        for line in file:
            data.append(line.strip().split(","))
        file.close()
    except:
        pass
    return data
    
def tambah_barang():
    kode = input("Kode Barang : ")
    nama = input("Nama Barang : ")
    qty = input("Quantity    : ")
    harga = input("Harga       : ")
    file = open("barang.txt", "a")
    file.write(f"{kode},{nama},{qty},{harga}\n")
    file.close()
    print("Barang berhasil ditambahkan.")
    
def hapus_barang():
    kode = input("Kode barang yang ingin dihapus : ")
    data = baca_barang()
    data_baru = []
    for d in data:
        if d[0] != kode:
            data_baru.append(d)
    simpan_barang(data_baru)
    print("Barang berhasil dihapus.")

