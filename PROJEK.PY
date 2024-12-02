import pandas as pd
import os 
import csv


print("""
___  ___          _     _____           _ 
|  \/  |         (_)   |_   _|         (_)
| .  . | ___  ___ _ _ __ | | __ _ _ __  _ 
| |\/| |/ _ \/ __| | '_ \| |/ _` | '_ \| |
| |  | |  __/\__ \ | | | | | (_| | | | | |
\_|  |_/\___||___/_|_| |_\_/\__,_|_| |_|_|
""")


# Nama file untuk menyimpan data pengguna dan admin
file_pengguna = "akun_pengguna.csv"
file_admin = "admin.csv"

# Menu utama
def main():
    while True:
        print('===================================')
        print('MESINTANI'.center(35))
        print('===================================\n')

        print('1. Daftar akun dulu yuk')
        print('2. Login')
        print('3. Keluar\n')
        pilihan = input('tentukkan pilihan: ')
        if pilihan == '1':
            daftar()
        elif pilihan == '2':
            login()
        elif pilihan == '3':
            print('\nKeluar dari MesinTani, Terimakasih!')
            break
        else:
            print('Pilihan tidak valid, coba lagi.\n')

# Daftar akun pengguna baru
def daftar():
    print('===================================')
    print('DAFTAR AKUN BARU'.center(35))
    print('===================================\n')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    konfirmasi = input('Konfirmasi password: ')

    if password != konfirmasi:
        print('Password dan konfirmasi password tidak cocok. Coba lagi!!')
        return

    with open(file_pengguna, mode='r', newline='') as file:
        baca = csv.DictReader(file)
        for row in baca:
            if row['username'] == username:
                print('Username sudah terdaftar. Gunakan username lain.')
                return

    with open(file_pengguna, mode='a', newline='') as file:
        a = csv.writer(file)
        a.writerow([username, password])

    print('Akun berhasil didaftarkan! Silakan login.\n')

# Login
def login():
    print('===================================')
    print('LOGIN'.center(35))
    print('===================================\n')
    print('1. Login sebagai Admin')
    print('2. Login sebagai Pengguna')
    print('3. kembali')

    pilihan = input('Pilih jenis login: ')
    if pilihan == '1':
        login_admin()
    elif pilihan == '2':
        login_pengguna()
    elif pilihan == '3':
        main()
    else:
        print('Pilihan tidak valid, coba lagi.\n')

# Login sebagai Admin
def login_admin():
    if not os.path.exists(file_admin):
        print('File admin.csv tidak ditemukan. Pastikan file tersedia!')
        return

    print('===================================')
    print('LOGIN ADMIN'.center(35))
    print('===================================\n')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    with open(file_admin, mode='r', newline='') as file:
        baca = csv.DictReader(file)
        for row in baca:
            if row['username'] == username and row['password'] == password:
                print(f'\nSelamat datang, Admin {username}!')
                menu_admin(username)
                return

            else: 
                print('Username atau password admin salah.\n')
                return login_admin()

# Login sebagai Pengguna
def login_pengguna():
    if not os.path.exists(file_pengguna):
        print('File akun_pengguna.csv tidak ditemukan. Silakan daftar terlebih dahulu!')
        return

    print('===================================')
    print('LOGIN PEMBELI'.center(35))
    print('===================================\n')
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')

    with open(file_pengguna, mode='r', newline='') as file:
        baca = csv.DictReader(file)
        for row in baca:
            if row['username'] == username and row['password'] == password:
                print(f'\nSelamat datang, {username}!')
                tampilan_pengguna(username)
                return
            
            else:
                print('Username atau password pengguna salah.\n')
                return login_pengguna()



# File untuk menyimpan data barang, voucher, dan transaksi
file_barang = "barang.csv"
file_voucher = "voucher.csv"
file_transaksi = "transaksi.csv"

# Menu admin
def menu_admin(username):
    while True:
        print('\n===================================')
        print('MENU ADMIN'.center(35))
        print('===================================\n')

        print('1. Manajemen Barang')
        print('2. Manajemen Voucher')
        print('3. Rekap Transaksi')
        print('4. Logout\n')

        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            manajemen_barang()
        elif pilihan == '2':
            manajemen_voucher()
        elif pilihan == '3':
            rekap_transaksi()
        elif pilihan == '4':
            print(f'\nTerima kasih, Admin {username}. Anda berhasil logout.')
            return main()
        else:
            print('Pilihan tidak valid, coba lagi.\n')

# Fitur manajemen barang
def manajemen_barang():
    print('===================================')
    print('MANAJEMEN BARANG'.center(35))
    print('===================================\n')
    print('1. Tambah Barang')
    print('2. Lihat Barang')
    print('3. kembali')
    man_barang = input('Pilih menu: ')
    if man_barang == '1':
        tambah_barang()
    elif man_barang == '2':
        lihat_barang()
    elif man_barang == '3':
        menu_admin()

#tambah barang
def tambah_barang():
    print('===================================')
    print('TAMBAH BARANG'.center(35))
    print('===================================\n')
    nama = input('Nama barang: ')
    
    while True:
        try:
            harga = float(input('Harga barang: Rp.'))
            break 
        except ValueError:
            print('Input tidak valid. Harap masukkan angka untuk harga barang.')

    while True:
        try:
            stok = int(input('Stok barang: '))
            break 
        except ValueError:
            print('Input tidak valid. Harap masukkan angka untuk stok barang.')

    with open(file_barang, mode='a', newline='') as file:
        tambah_b = csv.writer(file)
        tambah_b.writerow([os.urandom(4).hex(), nama, harga, stok])

    print(f'Barang {nama} berhasil ditambahkan.\n')
    manajemen_barang()

#lihat barang
def lihat_barang():
    print('===================================')
    print('LIHAT BARANG'.center(35))
    print('===================================\n')
    if not os.path.exists(file_barang):
        print('Belum ada barang.')
        return

    print(f"{'ID':<10} {'Nama':<20} {'Harga (Rp)':<15} {'Stok':<10}")
    print('-' * 55)

    with open(file_barang, mode='r') as file:
        baca = csv.DictReader(file)
        for row in baca:
            print(f"{row['id']:<10} {row['nama']:<20} {row['harga']:<15} {row['stok']:<10}")

    print('\n') 

    while True:
        kembali = input("Apakah Anda ingin kembali? (iya/tidak): ")
        if kembali == 'iya':
            manajemen_barang()
            break
        elif kembali == 'tidak':
            return lihat_barang()
        else:
            print("Pilihan tidak valid, silakan jawab 'iya' atau 'tidak'.")



# Fitur manajemen voucher
def manajemen_voucher():
        print('\n===================================')
        print('MANAJEMEN VOUCHER'.center(35))
        print('===================================\n')

        print('1. Tambah Voucher')
        print('2. Lihat Voucher')
        print('3. Hapus Voucher')
        print('4. Kembali\n')

        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            tambah_voucher()
        elif pilihan == '2':
            hapus_voucher()
        elif pilihan == '3':
            menu_admin()  
        else:
            print('Pilihan tidak valid, coba lagi.\n')

#tambah voucher
def tambah_voucher():
    print('\n===================================')
    print('TAMBAH VOUCHER'.center(35))
    print('===================================\n')
    kode = input('Kode voucher: ')
    diskon = input('Diskon (%): ')
    limit_pemakaian = input('Batas pemakaian voucher: ')

    with open(file_voucher, mode='a', newline='') as file:
        voucher = csv.writer(file)
        voucher.writerow([kode, diskon, limit_pemakaian])

    print(f'Voucher {kode} berhasil ditambahkan dengan batas pemakaian {limit_pemakaian}.')

def hapus_voucher():
    print('\n--- Hapus Voucher ---')
    lihat_voucher()
    kode_voucher = input('Masukkan kode voucher yang ingin dihapus: ')

    if not os.path.exists(file_voucher):
        print('Data voucher tidak ditemukan.')
        return

    rows = []
    with open(file_voucher, mode='r') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row['kode'] != kode_voucher]

    with open(file_voucher, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['kode', 'diskon', 'limit_pemakaian'])
        writer.writerows(rows)

    print('Voucher berhasil dihapus.')


def gunakan_voucher(kode_voucher):
    """
    Fitur untuk mengurangi limit pemakaian voucher saat digunakan.
    """
    if not os.path.exists(file_voucher):
        print('Data voucher tidak ditemukan.')
        return False

    voucher_tersedia = False
    rows = []

    with open(file_voucher, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['kode'] == kode_voucher:
                voucher_tersedia = True
                limit_pemakaian = int(row['limit_pemakaian'])
                if limit_pemakaian > 0:
                    limit_pemakaian -= 1
                    print(f"Voucher {kode_voucher} berhasil digunakan! Sisa pemakaian: {limit_pemakaian}.")
                    if limit_pemakaian > 0:
                        rows.append({'kode': row['kode'], 'diskon': row['diskon'], 'limit_pemakaian': limit_pemakaian})
                else:
                    print(f"Voucher {kode_voucher} sudah habis pemakaiannya.")
            else:
                rows.append(row)

    if not voucher_tersedia:
        print(f"Voucher {kode_voucher} tidak ditemukan.")
        return False

    # Tulis ulang data voucher
    with open(file_voucher, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['kode', 'diskon', 'limit_pemakaian'])
        writer.writeheader()
        writer.writerows(rows)

    return True

#rekap transaksi
def rekap_transaksi(username):
    while True:
        print('\n===================================')
        print('REKAP TRANSAKSI'.center(35))
        print('===================================\n')

        if not os.path.exists(file_transaksi):
            print('Belum ada transaksi.\n')
            break

        # Memastikan file akun pengguna tersedia
        if not os.path.exists(file_pengguna):
            print('Data akun pengguna tidak ditemukan. Pastikan file akun_pengguna.csv tersedia.\n')
            break

        # Membaca data pengguna
        pengguna_data = {}
        with open(file_pengguna, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pengguna_data[row['username']] = True  # Mengelola daftar pengguna terdaftar

        total_semua_transaksi = 0
        transaksi_list = []

        # Membaca data transaksi
        with open(file_transaksi, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['user'] in pengguna_data:  
                    transaksi_list.append(row)
                    total_semua_transaksi += int(row['total'])

        # Menampilkan data transaksi
        if transaksi_list:
            print(f"{'ID':<10} {'User':<15} {'Total (Rp)':<15} {'Tanggal':<15}")
            print('-' * 50)
            for row in transaksi_list:
                print(f"{row['id']:<10} {row['user']:<15} {row['total']:<15} {row['tanggal']:<15}")

            print(f"\nTotal Semua Transaksi: Rp {total_semua_transaksi}\n")
        else:
            print('Tidak ada transaksi dari akun pengguna yang terdaftar.\n')

        print("1. Kembali")
        pilihan = input("\nMasukkan pilihan: ")
        if pilihan == '1':
            menu_admin(username)  
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")

#tampilan pengguna
def tampilan_pengguna(username):
    print('\n===================================')
    print((f"\nSelamat datang, {username}!\n").center(35))
    print('===================================\n')


if __name__ == "__main__":
    main()

