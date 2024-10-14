print('-------------------------------------------------------------------------')
print('Nama     :Rabiatul Hikmah                     ')
print('Nim      :2409116049                          ')
print('Program  :Sistem Pengelolaan Stok Toko Hijab  ')
print('-------------------------------------------------------------------------')
from prettytable import PrettyTable

# database barang
daftar_barang = {
    'pashmina ceruty': {'stok': 200},
    'pashmina silk': {'stok': 150},
    'pashmina plisket': {'stok': 200},
    'pashmina kaos': {'stok': 250},
    'segi empat': {'stok': 150},
    'jilbab sport': {'stok': 100}
}
def lihat_stok():
    table = PrettyTable()
    table.field_names = ["nama ", "stok hijab )"]
    for nama, data in daftar_barang.items():
        table.add_row([nama, data['stok']])
    print("\nstok hijab di gudang:")
    print(table)

def tambah_barang():
    while True :
        print("\ntambah hijab baru")
        nama = input("masukkan nama hijab: ")
        stok = int(input("masukkan stok hijab: "))   
        if nama in daftar_barang:
            print(f"hijab '{nama}' sudah ada dalam daftar. masukan nama yang berbeda.")            
        else :
            daftar_barang[nama] = {'stok': stok}
            print(f"hijab '{nama}' berhasil ditambahkan stok{stok} pcs.")
            lanjut = input("lanjut menambahkan barang? (y/n)")
            if lanjut == 'y':
                pass
            else :
                break
            
def hapus_barang():
    print("\nhapus barang")
    while True :
        nama = input("masukkan nama barang yang ingin dihapus: ")    
        try:
            daftar_barang.pop(nama)  # Menghapus barang dari daftar menggunakan pop
            print(f"barang '{nama}' berhasil dihapus.")
        except KeyError:
            print(f"barang '{nama}' tidak ditemukan dalam daftar.")
        lanjut = input("lanjut menambahkan barang? (y/n)")
        if lanjut == 'y':
            pass
        else :
            break  

def update_stok():
    print("\nupdate stok barang")
    nama = input("masukkan nama barang yang ingin diupdate: ")   
    if nama in daftar_barang:
        stok_baru = int(input(f"masukkan stok baru untuk barang '{nama}': "))
        daftar_barang[nama]['stok'] = stok_baru
        print(f"stok '{nama}' berhasil diupdate menjadi {stok_baru} pcs.")
    else:
        print(f"barang '{nama}' tidak ditemukan.")

# login dan akses menu khusus karyawan gudang
def akses_karyawan_gudang():
    username = "rabi"
    password = "0202"
    input_username = input("Username: ")
    input_password = input("Password: ")
    if input_username == username and input_password == password:
        print("=" * 30)
        print("       Login berhasil.      ")
        print("    Selamat Datang Rabi     ")
        print("=" * 30)

        while True:
            table = PrettyTable()
            table.field_names = ["opsi", "menu"]
            table.add_row(["1", "lihat stok"])
            table.add_row(["2", "tambah barang"])
            table.add_row(["3", "hapus barang"])
            table.add_row(["4", "update stok"])
            table.add_row(["5", "kembali"])       
            print("\nmenu karyawan gudang")
            print(table)       
            pilihan_gudang = input("pilih opsi: ")

            if pilihan_gudang == '1':
                lihat_stok()
            elif pilihan_gudang == '2':
                tambah_barang()
            elif pilihan_gudang == '3':
                hapus_barang()
            elif pilihan_gudang == '4':
                update_stok()
            elif pilihan_gudang == '5':
                break
            else:
                print("pilihan tidak valid. coba lagi.")
    else:
        print("Username atau password salah.")


# akses bersama yang bisa dilihat siapa saja
def akses_bersama():
    print("selamat datang! silahkan masukkan nama anda")
    nama_user =input("username :")
    print(f"halo {nama_user}")
    while True:
        table = PrettyTable()
        table.field_names = ["opsi", "menu"]
        table.add_row(["1", "lihat stok"])
        table.add_row(["2", "kembali"])
        print("\n--- akses bersama  ---")
        print(table)
        
        pilihan = input("pilih opsi: ")
        if pilihan == '1':
            lihat_stok()
        elif pilihan == '2':
            break
        else:
            print("pilihan tidak valid. coba lagi.")

# menu utama yaitu memilih role
def main():
    while True:
        table = PrettyTable()
        table.field_names = ["Opsi", "menu"]
        table.add_row(["1", "akses karyawan gudang"])
        table.add_row(["2", "akses bersama"])
        table.add_row(["3", "keluar"])
        print("\nsilahkan pilih role anda")
        print(table)
        pilihan = input("pilih opsi: ")       
        if pilihan == '1':
            akses_karyawan_gudang()
        elif pilihan == '2':
            akses_bersama()
        elif pilihan == '3':
            print("program berhenti!!!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == '__main__':
    main()
