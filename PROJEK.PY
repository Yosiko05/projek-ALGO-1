import pandas as pd
import os 
import csv

def clear_terminal():
    if os.name == 'nt':  
        os.system('cls')

# Nama file untuk menyimpan data pengguna dan admin
file_pengguna = "akun_pengguna.csv"
file_admin = "admin.csv"

# Menu utama
def main():
    while True:
        print("""
___  ___          _     _____           _ 
|  \/  |         (_)   |_   _|         (_)
| .  . | ___  ___ _ _ __ | | __ _ _ __  _ 
| |\/| |/ _ \/ __| | '_ \| |/ _` | '_ \| |
| |  | |  __/\__ \ | | | | | (_| | | | | |
\_|  |_/\___||___/_|_| |_\_/\__,_|_| |_|_|
""")

        print('===================================')
        print('SELAMAT DATANG DI MESINTANI'.center(35))
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
            return main()

def daftar():
    if os.name == 'nt':  
        os.system('cls')
    print('===================================')
    print('DAFTAR AKUN BARU'.center(35))
    print('===================================\n')

    if not os.path.exists(file_pengguna):
        with open(file_pengguna, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password'])

    while True:
        username = input('Masukkan username: ')
        
        # Cek apakah username sudah terdaftar
        with open(file_pengguna, mode='r', newline='') as file:
            baca = csv.DictReader(file)
            for row in baca:
                if row['username'] == username:
                    print('Username sudah terdaftar. Gunakan username lain.')
                    break
            else:
                break

    while True:
        password = input('Masukkan password: ')
        konfirmasi = input('Konfirmasi password: ')

        if password != konfirmasi:
            print('Password dan konfirmasi password tidak cocok. Coba lagi!!')
        else:
            break 

    with open(file_pengguna, mode='a', newline='') as file:
        a = csv.writer(file)
        a.writerow([username, password])


    clear_terminal()
    print('Akun berhasil didaftarkan! Silakan login.\n')
# Login
def login():
    if os.name == 'nt':  
        os.system('cls')
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
        return login()
        

# Login sebagai Admin
def login_admin():
    if os.name == 'nt':  
        os.system('cls')

    print('===================================')
    print('LOGIN ADMIN' .center(35))
    print('===================================\n')
    while True:
        username = input('Masukkan username: ')

        # Cek apakah username ada di file admin
        with open(file_admin, mode='r', newline='') as file:
            baca = csv.DictReader(file)
            if not any(row['username'] == username for row in baca):
                print('Username tidak ditemukan! Silakan masukkan username yang benar.')
                continue  # Kembali ke awal loop untuk meminta username lagi

        while True: 
            password = input('Masukkan password: ')

            with open(file_admin, mode='r', newline='') as file:
                baca = csv.DictReader(file)
                for row in baca:
                    if row['username'] == username and row['password'] == password:
                        menu_admin(username)
                        return

            print('Password salah! Silakan coba lagi.')

                    
                    

                

# Login sebagai Pengguna
def login_pengguna():
    clear_terminal()
    if not os.path.exists(file_pengguna):
        print('File akun_pengguna.csv tidak ditemukan. Silakan daftar terlebih dahulu!')
        return

    print('===================================')
    print('LOGIN PEMBELI'.center(35))
    print('===================================\n')
    while True:
        username = input('Masukkan username: ')
        
        # Cek apakah username ada di file akun_pengguna.csv
        with open(file_pengguna, mode='r', newline='') as file:
            baca = csv.DictReader(file)
            if not any(row['username'] == username for row in baca):
                print('Username tidak ditemukan! Silakan masukkan username yang benar.')
                continue 

        while True:
            password = input('Masukkan password: ')

            with open(file_pengguna, mode='r', newline='') as file:
                baca = csv.DictReader(file)
                for row in baca:
                    if row['username'] == username and row['password'] == password:
                        print(f'\nSelamat datang, {username}!')
                        tampilan_pengguna(username)
                        return 

            print('Password salah! Silakan coba lagi.')

# File untuk menyimpan data barang, voucher, dan transaksi
file_barang = "barang.csv"
file_voucher = "voucher.csv"
file_transaksi = "transaksi.csv"

# Menu admin
def menu_admin(username):
    if os.name == 'nt':  
        os.system('cls')
    while True:
        print('\n===================================')
        print('MENU ADMIN'.center(35))
        print('===================================\n')
        print(f'Selamat Datang, {username}!\n')
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
            lihat_voucher()
        elif pilihan == '3':
            hapus_voucher()
        elif pilihan == '4':
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
        writer = csv.writer(file)
        writer.writerow([kode, diskon, limit_pemakaian])

    print(f'Voucher {kode} berhasil ditambahkan dengan batas pemakaian {limit_pemakaian}.')

#lihat voucher
def lihat_voucher():
    print('===================================')
    print('LIHAT VOUCHER'.center(35))
    print('===================================\n')
    
    if not os.path.exists(file_voucher):
        print('Belum ada voucher yang terdaftar.')
        return

    print(f"{'Kode':<15} {'Diskon (%)':<15} {'Limit Pemakaian':<20}")
    print('-' * 50)

    with open(file_voucher, mode='r') as file:
        baca = csv.DictReader(file)
        for row in baca:
            print(f"{row['kode']:<15} {row['diskon']:<15} {row['limit_pemakaian']:<20}")

    print('\n') 

    while True:
        kembali = input("Apakah Anda ingin kembali? (iya/tidak): ")
        if kembali == 'iya':
            manajemen_voucher()
            break
        elif kembali == 'tidak':
            return lihat_voucher()
        else:
            print("Pilihan tidak valid, silakan jawab 'iya' atau 'tidak'.")

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
    keranjang = muat_keranjang(username)

    if os.name == 'nt':  
        os.system('cls')
    print('\n===================================')
    print('Selamat datang'.center(35))
    print('===================================\n')

    while True:
        print('1. Belanja')
        print('2. Cek Keranjang')
        print('3. Logout\n')

        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            belanja(keranjang, username)  # Pass keranjang ke fungsi belanja
        elif pilihan == '2':
            cek_keranjang(keranjang)
        elif pilihan == '3':
            print(f'\nTerima kasih telah berbelanja, {username}. Anda berhasil logout.')
            simpan_keranjang(username, keranjang)  
            break 
        else:
            print('Pilihan tidak valid, coba lagi.\n')


def belanja(keranjang, username):
    if os.name == 'nt':  
        os.system('cls')
    print('\n--- Daftar Barang ---')
    if not os.path.exists(file_barang):
        print('Belum ada barang tersedia.\n')
        return

    barang_tersedia = []
    with open(file_barang, mode='r') as file:
        reader = csv.DictReader(file)
        
        print(f"{'ID':<10} {'Nama Barang':<20} {'Harga (Rp)':<15} {'Stok':<10}")
        print('-' * 60)
        
        for row in reader:
            barang_tersedia.append(row)
            # Menampilkan setiap baris barang
            print(f"{row['id']:<10} {row['nama']:<20} {row['harga']:<15} {row['stok']:<10}")
    
    if not barang_tersedia:
        print('Tidak ada barang tersedia saat ini.\n')
        return

    # Pilih barang untuk dimasukkan ke keranjang
    id_barang = input('\nMasukkan ID barang yang ingin dibeli (atau ketik "0" untuk kembali): ')
    if id_barang == '0':
        return

    for barang in barang_tersedia:
        if barang['id'] == id_barang:
            try:
                jumlah = int(input(f"Masukkan jumlah {barang['nama']} yang ingin dibeli: "))
                if jumlah <= int(barang['stok']):
                    # Cek apakah barang sudah ada di keranjang
                    barang_ditemukan = False
                    for item in keranjang:
                        if item['id'] == barang['id']:
                            item['jumlah'] += jumlah  # Menambah jumlah barang yang sudah ada
                            barang_ditemukan = True
                            break

                    if not barang_ditemukan:
                        keranjang.append({'id': barang['id'], 'nama': barang['nama'], 'harga': barang['harga'], 'jumlah': jumlah})
                    
                    print(f"{barang['nama']} sebanyak {jumlah} berhasil ditambahkan ke keranjang.\n")
                    simpan_keranjang(username, keranjang)
                    
                    lanjut_belanja = input('Apakah Anda ingin membeli barang lain? (y/n): ')
                    if lanjut_belanja.lower() == 'y':
                        belanja(keranjang, username)  
                    else:
                        print('Baik terimakasih')
                        return  
                else:
                    print('Jumlah melebihi stok yang tersedia.\n')
            except ValueError:
                print('Input jumlah tidak valid.\n')
            return

    print('ID barang tidak ditemukan. Coba lagi.\n')


def muat_keranjang(username):
    keranjang = []
    if os.path.exists(f"keranjang_{username}.csv"):
        with open(f"keranjang_{username}.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                keranjang.append({
                    'id': row['id'],
                    'nama': row['nama'],
                    'harga': row['harga'],
                    'jumlah': int(row['jumlah'])
                })
    return keranjang

def simpan_keranjang(username, keranjang):
    with open(f"keranjang_{username}.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nama', 'harga', 'jumlah'])
        writer.writeheader()
        for item in keranjang:
            writer.writerow(item)

# Fitur Cek Keranjang
def cek_keranjang(keranjang):
    if os.name == 'nt':  
        os.system('cls')
    print('\n--- Keranjang Belanja ---')
    if not keranjang:
        print('Keranjang Anda kosong.\n')
        return

    total = 0
    print(f"{'ID':<10} {'Nama':<20} {'Jumlah':<10} {'Harga Satuan (Rp)':<20} {'Subtotal (Rp)':<15}")
    print('-' * 70)
    for item in keranjang:
        subtotal = int(item['harga']) * item['jumlah']
        total += subtotal
        print(f"{item['id']:<10} {item['nama']:<20} {item['jumlah']:<10} {item['harga']:<20} {subtotal:<15}")

    print('-' * 70)
    print(f"Total Belanja: Rp {total}\n")

    print('1. Checkout')
    print('2. Kembali\n')

    pilihan = input('Pilih menu: ')
    if pilihan == '1':
        checkout(keranjang, total)
    elif pilihan == '2':
        return
    else:
        print('Pilihan tidak valid, coba lagi.\n')

# Fitur Checkout
def checkout(keranjang, total):
    if os.name == 'nt':  
        os.system('cls')
    print('\n--- Checkout ---\n')
    print(f"Total yang harus dibayar: Rp {total}\n")

    pakai_voucher = input('Apakah Anda memiliki voucher? (y/n): ')
    if pakai_voucher.lower() == 'y':
        kode_voucher = input('Masukkan kode voucher: ')
        if gunakan_voucher(kode_voucher):
            with open(file_voucher, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['kode'] == kode_voucher:
                        diskon = int(row['diskon'])
                        total_diskon = total * diskon // 100
                        total -= total_diskon
                        print(f"\nVoucher berhasil digunakan!")
                        print(f"Diskon {diskon}% diterapkan.")
                        print(f"Total setelah diskon: Rp {total}\n")
                        break
        else:
            print('\nVoucher tidak valid atau sudah habis pemakaian.\n')

    while True:
        try:
            nominal = int(input(f"Masukkan nominal pembayaran (harus Rp {total}): \n"))
            if nominal < total:
                print(f"\nNominal kurang. Anda masih membutuhkan Rp {total - nominal} lagi.\n")
            elif nominal > total:
                print(f"\nNominal lebih. Uang kembalian Anda: Rp {nominal - total}.\n")
                break
            else:
                print("\nNominal sesuai. Pembayaran berhasil!\n")
                break
        except ValueError:
            print("\nMasukkan angka yang valid.\n")


    # Catat transaksi dan kosongkan keranjang
    with open(file_transaksi, mode='a', newline='') as file:
        transaksi_writer = csv.writer(file)
        from datetime import datetime
        transaksi_id = os.urandom(4).hex()
        tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        transaksi_writer.writerow([transaksi_id, total, tanggal])

    print('\nTransaksi berhasil dicatat. Keranjang Anda sekarang kosong.')
    keranjang.clear()

os.system('cls')
if __name__ == "__main__":
    main()

