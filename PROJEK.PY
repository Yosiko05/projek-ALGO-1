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
    clear_terminal()
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
            keluar()
            break
        else:
            main()
        break

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
        username = input('Masukkan username: ').strip()

        while True:
            if not username:
                df=input('Username tidak boleh kosong! coba lagi? (y/n)')
                if df == 'y':
                    daftar()
                    return
                elif df == 'n':
                    main()
                    return
                else:
                    print('input tidak valid')
                    continue
            clear_terminal()    
            break
            
            
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
            password = input('Masukkan password: ').strip()
            if not password: 
                input('Password tidak boleh kosong. klik enter untuk mengulangi')
                daftar()
            konfirmasi = input('Konfirmasi password: ')

            if password != konfirmasi:
                print('Password dan konfirmasi password tidak cocok. Coba lagi!!')
            else:
                break 

        with open(file_pengguna, mode='a', newline='') as file:
            a = csv.writer(file)
            a.writerow([username, password])

        input('--Akun berhasil didaftarkan! Silakan login.--\n')
        main()
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
        login()
    
    
        

# Login sebagai Admin
def login_admin():
    if os.name == 'nt':  
        os.system('cls')

    print('===================================')
    print('LOGIN ADMIN' .center(35))
    print('===================================\n')

    if not os.path.exists(file_admin):
        with open(file_admin, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password']) 
    while True:
        username = input('Masukkan username: ')

        # Cek apakah username ada di file admin
        with open(file_admin, mode='r', newline='') as file:
            baca = csv.DictReader(file)
            if not any(row['username'] == username for row in baca):
                while True:
                    j=input('Username tidak ditemukan! apakah mau mecoba kembali? (y/n): ')
                    if j == 'y':
                        login_admin()
                        return
                    elif j == 'n':
                        login()
                        return
                    else:
                        print("pilihan tidak valid")
                        continue

        while True: 
            password = input('Masukkan password: ')

            with open(file_admin, mode='r', newline='') as file:
                baca = csv.DictReader(file)
                for row in baca:
                    if row['username'] == username and row['password'] == password:
                        menu_admin(username)
                        return 

            input('Password salah! Silakan coba lagi.')
            login_admin()

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
                while True:
                    a=input('Username salah, coba lagi?(y/n): ')
                    if a == 'y':
                        login_pengguna()
                    elif a == 'n':
                        login()
                    else:
                        print('pilihan tidak valid')
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

            input('Password salah! Silakan coba lagi.')
            login_pengguna()

file_barang = "barang.csv"
file_voucher = "voucher.csv"
file_transaksi = "transaksi.csv"

# Menu admin
def menu_admin(username):
    clear_terminal()
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
    if os.name == 'nt':  
        os.system('cls')
    while True:
        print('===================================')
        print('MANAJEMEN BARANG'.center(35))
        print('===================================\n')
        print('1. Tambah Barang')
        print('2. Lihat Barang')
        print('3. Hapus Barang')
        print('4. Kembali')
        man_barang = input('Pilih menu: ')
        if man_barang == '1':
            tambah_barang()
        elif man_barang == '2':
            lihat_barang()
        elif man_barang == '3':
            hapus_barang()
        elif man_barang == '4':
            return clear_terminal()
        else:
            print("Pilihan tidak valid, coba lagi.\n")
        break


# Fungsi Tambah Barang
def tambah_barang():
    clear_terminal()
    print('===================================')
    print('TAMBAH BARANG'.center(35))
    print('===================================\n')
    
    # Validasi nama barang tidak boleh kosong
    while True:
        nama = input('Nama barang: ').strip()
        if nama:  # Jika nama tidak kosong
            break
        else:
            print("Nama barang tidak boleh kosong. Harap masukkan nama barang.")

    while True:
        try:
            harga = int(input('Harga barang: Rp.'))
            break 
        except ValueError:
            print('Input tidak valid. Harap masukkan angka untuk harga barang.')

    while True:
        try:
            stok = int(input('Stok barang: '))
            break 
        except ValueError:
            print('Input tidak valid. Harap masukkan angka untuk stok barang.')

    # Cek apakah file barang.csv sudah ada
    file_exists = os.path.exists(file_barang)

    # Tentukan id berdasarkan data terakhir
    if file_exists:
        with open(file_barang, mode='r') as file:
            reader = csv.DictReader(file)
            id = 0
            for row in reader:
                id = int(row['id'])  # Ambil id terakhir
            id_barang = id + 1  # id berikutnya
    else:
        id_barang = 1  # Jika file belum ada, mulai dari 1

    with open(file_barang, mode='a', newline='') as file:
        tambah_b = csv.writer(file)
        if not file_exists:
            tambah_b.writerow(['id', 'nama', 'harga', 'stok'])  
        tambah_b.writerow([id_barang, nama, harga, stok])  

    print(f'\nBarang {nama} berhasil ditambahkan.\n')
    input('Tekan Enter untuk kembali ke menu manajemen...')
    clear_terminal()
    
# Fungsi Lihat Barang
def lihat_barang():
    if os.name == 'nt':  
        os.system('cls')
    print('===================================')
    print('LIHAT BARANG'.center(35))
    print('===================================\n')
    if not os.path.exists(file_barang):
        print('Belum ada barang.')
        return

    print(f"{'ID':<10} {'Nama':<30} {'Harga (Rp)':<25} {'Stok':<10}")
    print('-' * 110)

    with open(file_barang, mode='r') as file:
        baca = csv.DictReader(file)
        for row in baca:
            print(f"{row['id']:<10} {row['nama']:<30} {row['harga']:<25} {row['stok']:<10}")

    print('\n') 

    input("Tekan Enter untuk kembali ke menu manajemen...")
    clear_terminal()

def hapus_barang():
    if os.name == 'nt':  
        os.system('cls')
    print('===================================')
    print('HAPUS BARANG'.center(35))
    print('===================================\n')

    if not os.path.exists(file_barang):
        print('Belum ada barang untuk dihapus.')
        input("Tekan Enter untuk kembali")
        manajemen_barang()
        return

    # Tampilkan daftar barang
    print(f"{'ID':<10} {'Nama':<20} {'Harga (Rp)':<15} {'Stok':<10}")
    print('-' * 55)

    barang_tersedia = []
    with open(file_barang, mode='r') as file:
        baca = csv.DictReader(file)
        for row in baca:
            barang_tersedia.append(row)
            print(f"{row['id']:<10} {row['nama']:<25} {row['harga']:<15} {row['stok']:<10}")

    print('\n')

    # Input ID barang untuk dihapus
    id_hapus = input("Masukkan ID barang yang ingin dihapus: ")

    # Filter barang untuk dihapus
    barang_baru = [barang for barang in barang_tersedia if barang['id'] != id_hapus]

    if len(barang_tersedia) == len(barang_baru):
        print(f"Barang dengan ID {id_hapus} tidak ditemukan.")
    else:
        with open(file_barang, mode='w', newline='') as file:
            tulis = csv.DictWriter(file, fieldnames=['id', 'nama', 'harga', 'stok'])
            tulis.writeheader()
            tulis.writerows(barang_baru)
        print(f"Barang dengan ID {id_hapus} berhasil dihapus.")

    input("Tekan Enter untuk kembali ke menu manajemen...")
    clear_terminal()
# Fungsi manajemen voucher
def manajemen_voucher():
    if os.name == 'nt':  
        os.system('cls')
    while True:
        print('===================================')
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
            clear_terminal()
            return 
        else:
            print('Pilihan tidak valid, coba lagi.\n')
        break


# Fungsi untuk menambah voucher
def tambah_voucher():
    if os.name == 'nt':  
        os.system('cls')
    print('===================================')
    print('TAMBAH VOUCHER'.center(35))
    print('===================================\n')

    kode = input('Masukkan kode voucher: ').strip()
    if not kode:
        print('Kode voucher tidak boleh kosong.\n')
        return

    while True:
        try:
            diskon = int(input('Masukkan diskon (%): '))
            if diskon < 0 or diskon > 100:
                print('Diskon harus antara 0% hingga 100%.')
                continue
            break
        except ValueError:
            print('Diskon harus berupa angka.')

    while True:
        try:
            limit_pemakaian = int(input('Masukkan batas pemakaian voucher: '))
            if limit_pemakaian <= 0:
                print('Batas pemakaian harus lebih dari 0.')
                continue
            break
        except ValueError:
            print('Batas pemakaian harus berupa angka.')

    # Tambahkan ke file voucher
    header = ['kode', 'diskon', 'limit_pemakaian']
    if not os.path.exists(file_voucher):
        with open(file_voucher, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

    with open(file_voucher, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([kode, diskon, limit_pemakaian])

    print(f'Voucher {kode} berhasil ditambahkan dengan diskon {diskon}% dan batas {limit_pemakaian}.\n')
    input('Klik Enter untuk Lanjut')
    manajemen_voucher()

# Fungsi untuk melihat voucher
def lihat_voucher():
    if os.name == 'nt':  
        os.system('cls')
    print('===================================')
    print('DAFTAR VOUCHER'.center(35))
    print('===================================\n')

    if not os.path.exists(file_voucher):
        print('Tidak ada voucher yang tersedia.\n')
        input('Masukkan voucher terlebih dahulu')
        return clear_terminal()

    with open(file_voucher, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print('Tidak ada voucher yang tersedia.\n')
            return

        print(f"{'Kode':<15} {'Diskon (%)':<15} {'Batas Pemakaian':<20}")
        print('-' * 50)
        for row in rows:
            print(f"{row['kode']:<15} {row['diskon']:<15} {row['limit_pemakaian']:<20}")
        print('\n')
        input('Klik Enter untuk Lanjut')
        return clear_terminal()

# Fungsi untuk menghapus voucher
def hapus_voucher():
    if os.name == 'nt':  
        os.system('cls')

    # Tampilkan daftar voucher yang ada
    with open(file_voucher, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print('Tidak ada voucher yang tersedia.\n')
            return
        
        print(f"{'Kode':<15} {'Diskon (%)':<15} {'Batas Pemakaian':<20}")
        print('-' * 50)
        for row in rows:
            print(f"{row['kode']:<15} {row['diskon']:<15} {row['limit_pemakaian']:<20}")
        print('-' * 50)

    # Input kode voucher yang ingin dihapus
    kode = input('Masukkan kode voucher yang ingin dihapus: ').strip()

    if not os.path.exists(file_voucher):
        print('Data voucher tidak ditemukan.\n')
        return 

    updated_rows = []
    voucher_ditemukan = False

    with open(file_voucher, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['kode'] == kode:
                voucher_ditemukan = True
            else:
                updated_rows.append(row)

    if not voucher_ditemukan:
        print(f"Voucher tidak ditemukan.\n")
        input('Klik enter untuk kembali')
        return clear_terminal()

    with open(file_voucher, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['kode', 'diskon', 'limit_pemakaian'])
        writer.writeheader()
        writer.writerows(updated_rows)

    print(f'Voucher {kode} berhasil dihapus.\n')
    clear_terminal()

#rekap
def rekap_transaksi():
    if os.name == 'nt':  
        os.system('cls')
    print('\n--- Rekap Transaksi ---\n')

    if not os.path.exists(file_transaksi):
        print('Belum ada transaksi.')
        return

    print(f"{'ID Transaksi':<15} {'Username':<15} {'Tanggal':<20} {'Barang':<55} {'Total Pembayaran':<15}")
    print('-' * 100)

    with open(file_transaksi, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['transaksi_id']:<15} {row['username']:<15} {row['tanggal']:<20} {row['barang']:<55} Rp {row['total_pembayaran']:<15}")

    print('\n')
    input("Tekan Enter untuk kembali ke menu utama...")
    clear_terminal()

#tampilan pengguna
def tampilan_pengguna(username):
    clear_terminal()
    keranjang = muat_keranjang(username)
    while True:
        print('\n===================================')
        print((f"Selamat datang, {username}!").center(35))
        print('===================================\n')

        print('1. Belanja')
        print('2. Cek Keranjang')
        print('3. Logout\n')

        pilihan = input('Pilih menu: ')
        if pilihan == '1':
            belanja(keranjang, username)  
        elif pilihan == '2':
            cek_keranjang(keranjang, username) 
        elif pilihan == '3':
            print(f'\nTerima kasih telah berbelanja, {username}. Anda berhasil logout.')
            input('---klik enter untuk konfirmasi---')
            main()
            simpan_keranjang(username, keranjang)  
            break 
        else:
            clear_terminal()
            print('Pilihan tidak valid, coba lagi.\n')

#belanja
def belanja(keranjang, username):
    if os.name == 'nt':  
        os.system('cls')
    print('===================================')
    print('BELANJA YUK'.center(35))
    print('===================================\n')
    if not os.path.exists(file_barang):
        print('Belum ada barang tersedia.\n')
        return

    barang_tersedia = []
    with open(file_barang, mode='r') as file:
        reader = csv.DictReader(file)
        
        print(f"{'ID':<10} {'Nama Barang':<30} {'Harga (Rp)':<15} {'Stok':<10}")
        print('-' * 60)
        
        for row in reader:
            # Hanya tambahkan barang dengan stok > 0
            if int(row['stok']) > 0:
                barang_tersedia.append(row)
                print(f"{row['id']:<10} {row['nama']:<30} {row['harga']:<15} {row['stok']:<10}")
    
    if not barang_tersedia:
        print('Tidak ada barang tersedia saat ini.\n')
        return

    # Pilih barang untuk dimasukkan ke keranjang
    id_barang = input('\nMasukkan ID barang yang ingin dibeli (ketik enter untuk kembali): ')
    if not id_barang:
        return clear_terminal()

    for barang in barang_tersedia:
        if barang['id'] == id_barang:
            stok_tersedia = int(barang['stok'])
            
            while True:  # Loop untuk memastikan jumlah barang valid
                if os.name == 'nt':
                    os.system('cls') 

                print('\n--- Daftar Barang ---')
                print(f"{'ID':<10} {'Nama Barang':<30} {'Harga (Rp)':<15} {'Stok':<10}")
                print('-' * 60)
                for b in barang_tersedia:
                    print(f"{b['id']:<10} {b['nama']:<30} {b['harga']:<15} {b['stok']:<10}")
                
                print(f"\nBarang dipilih: {barang['nama']}")
                print(f"Stok tersedia: {stok_tersedia}")

                try:
                    jumlah = input(f"Masukkan jumlah {barang['nama']} yang ingin dibeli: ").strip()
                    
                    if not jumlah:  # Jika input kosong, ulangi
                        print("Jumlah tidak boleh kosong. Silakan coba lagi.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                    
                    jumlah = int(jumlah)
                    
                    if jumlah <= 0:  # Jika jumlah ≤ 0, ulangi
                        print("Jumlah barang harus lebih dari 0. Silakan coba lagi.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue

                    if jumlah > stok_tersedia:  # Jika jumlah melebihi stok, ulangi
                        print(f"Jumlah melebihi stok yang tersedia ({stok_tersedia}). Silakan coba lagi.")
                        input("Tekan Enter untuk melanjutkan...")
                        continue

                    break  # Keluar dari loop jika jumlah valid
                except ValueError:
                    print("Input jumlah tidak valid. Masukkan angka.")
                    input("Tekan Enter untuk melanjutkan...")

            # Tambahkan barang ke keranjang jika jumlah valid
            barang_ditemukan = False
            for item in keranjang:
                if item['id'] == barang['id']:
                    item['jumlah'] += jumlah  # Menambah jumlah barang yang sudah ada
                    barang_ditemukan = True
                    break

            if not barang_ditemukan:
                keranjang.append({
                    'id': barang['id'], 
                    'nama': barang['nama'], 
                    'harga': barang['harga'], 
                    'jumlah': jumlah
                })
            
            # Kurangi stok barang dalam file
            barang['stok'] = str(stok_tersedia - jumlah)
            
            with open(file_barang, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'nama', 'harga', 'stok'])
                writer.writeheader()
                writer.writerows(barang_tersedia)
            
            print(f"{barang['nama']} sebanyak {jumlah} berhasil ditambahkan ke keranjang.\n")
            simpan_keranjang(username, keranjang)
            
            lanjut_belanja = input('Apakah Anda ingin membeli barang lain? (y/n): ')
            if lanjut_belanja.lower() == 'y':
                return belanja(keranjang, username)
            else:
                print('Baik terima kasih!')
                return clear_terminal()

    print('ID barang tidak ditemukan. Coba lagi.\n')
    return belanja(keranjang, username)


def muat_keranjang(username):
    keranjang = []
    if os.path.exists("keranjang.csv"):
        with open("keranjang.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username:  # Memuat keranjang milik pengguna tertentu
                    keranjang.append({
                        'id': row['id'],
                        'nama': row['nama'],
                        'harga': row['harga'],
                        'jumlah': int(row['jumlah'])
                    })
    return keranjang


def simpan_keranjang(username, keranjang):
    data_keranjang = []
    if os.path.exists("keranjang.csv"):
        with open("keranjang.csv", mode='r') as file:
            reader = csv.DictReader(file)
            data_keranjang = list(reader)

    # Hapus data keranjang pengguna lama
    data_keranjang = [row for row in data_keranjang if row['username'] != username]

    # Tambahkan data keranjang pengguna baru
    for item in keranjang:
        data_keranjang.append({
            'username': username,
            'id': item['id'],
            'nama': item['nama'],
            'harga': item['harga'],
            'jumlah': item['jumlah']
        })

    with open("keranjang.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'id', 'nama', 'harga', 'jumlah'])
        writer.writeheader()
        writer.writerows(data_keranjang)

# Fitur Cek Keranjang
def cek_keranjang(keranjang, username):
    clear_terminal()
    print('\n===================================')
    print(('CEK KERANJANGMU').center(35))
    print('===================================\n')
    print('--- Daftar Keranjang Kamu ---')
    if not keranjang:
        print('Keranjang Anda kosong.\n')
        input("klik enter untuk kembali")
        return clear_terminal()

    total = 0
    print(f"{'ID':<10} {'Nama':<30} {'Jumlah':<20} {'Harga Satuan (Rp)':<25} {'Subtotal (Rp)':<15}")
    print('-' * 100)
    for item in keranjang:
        subtotal = int(item['harga']) * item['jumlah']
        total += subtotal
        print(f"{item['id']:<10} {item['nama']:<30} {item['jumlah']:<20} {item['harga']:<25} {subtotal:<15}")

    print('-' * 100)
    print(f"Total Belanja: Rp {total}\n")

    print('1. Checkout')
    print('2. Kembali\n')

    pilihan = input('Pilih menu: ')
    if pilihan == '1':
        checkout(keranjang, total, username) 
    elif pilihan == '2':
        return clear_terminal()
    else:
        print('Pilihan tidak valid, coba lagi.\n')

from datetime import datetime
def checkout(keranjang, total, username):
    if os.name == 'nt':  
        os.system('cls')
    print('\n===================================')
    print(('CHECKOUT').center(35))
    print('===================================\n')
    print(f"Total yang harus dibayar: Rp {total}\n")

    # Proses voucher
    pakai_voucher = input('Apakah Anda memiliki voucher? (y/n): ')
    if pakai_voucher.lower() == 'y':
        kode_voucher = input('Masukkan kode voucher: ')
        if os.path.exists(file_voucher):
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
                            diskon = int(row['diskon'])
                            total_diskon = total * diskon // 100
                            total -= total_diskon
                            print(f"\nTotal setelah diskon: Rp {total}\n")
                            if limit_pemakaian > 0:
                                rows.append({'kode': row['kode'], 'diskon': row['diskon'], 'limit_pemakaian': limit_pemakaian})
                        else:
                            print(f"Voucher {kode_voucher} sudah habis pemakaiannya.")
                    else:
                        rows.append(row)

            # Update file voucher
            with open(file_voucher, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['kode', 'diskon', 'limit_pemakaian'])
                writer.writeheader()
                writer.writerows(rows)

            if not voucher_tersedia:
                print(f"Voucher {kode_voucher} tidak ditemukan atau tidak valid.")
        else:
            print('kode voucher tidak ditemukan.')
    else:
        print("Anda tidak menggunakan voucher.")

    # Proses pembayaran
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

    # Proses pembaruan stok barang
    barang_update = []
    daftar_barang = []
    with open(file_barang, mode='r') as file:
        reader = csv.DictReader(file)
        barang_tersedia = list(reader)

    for item in keranjang:
        id_barang = item['id']
        jumlah_beli = int(item['jumlah'])
        nama_barang = item['nama']
        harga_barang = int(item['harga'])

        # Gabungkan data barang untuk laporan transaksi
        daftar_barang.append(f"{nama_barang} (x{jumlah_beli})")

        # Perbarui stok barang
        for row in barang_tersedia:
            if row['id'] == id_barang:
                stok_terbaru = int(row['stok']) - jumlah_beli
                if stok_terbaru > 0:
                    row['stok'] = str(stok_terbaru)
                    barang_update.append(row)
                # Jika stok habis atau negatif, barang tidak ditambahkan kembali
                break
            else:
                barang_update.append(row)

    # Simpan data barang dengan stok > 0 ke file
    with open(file_barang, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'nama', 'harga', 'stok'])
        writer.writeheader()
        writer.writerows(barang_update)

    # Simpan transaksi ke file transaksi
    transaksi_data = []
    if os.path.exists(file_transaksi):
        with open(file_transaksi, mode='r') as file:
            reader = csv.DictReader(file)
            transaksi_data = [row for row in reader]

    transaksi_id = len(transaksi_data) + 1
    tanggal_transaksi = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaksi_data.append({
        'transaksi_id': transaksi_id,
        'username': username,
        'tanggal': tanggal_transaksi,
        'barang': ', '.join(daftar_barang),
        'total_pembayaran': total
    })

    with open(file_transaksi, mode='w', newline='') as file:
        fieldnames = ['transaksi_id', 'username', 'tanggal', 'barang', 'total_pembayaran']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transaksi_data)

    # Bersihkan keranjang pengguna
    data_keranjang = []
    if os.path.exists("keranjang.csv"):
        with open("keranjang.csv", mode='r') as file:
            reader = csv.DictReader(file)
            data_keranjang = [row for row in reader if row['username'] != username]

    with open("keranjang.csv", mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'id', 'nama', 'harga', 'jumlah'])
        writer.writeheader()
        writer.writerows(data_keranjang)

    keranjang.clear()
    print("\nCheckout berhasil. Terima kasih sudah berbelanja!")
    input('Klik enter untuk kembali')
    clear_terminal()


def keluar():
    clear_terminal()
    print(''' _____________  ______  ______   __ _____   __________ __    _______   __  ______  ___   ____     ____  ____  ______  ___   ______
/_  __/ __/ _ \/  _/  |/  / _ | / //_/ _ | / __/  _/ // /   / __/ _ | /  |/  / _ \/ _ | /  _/ __ / / / / /  |/  / _ \/ _ | / / / /
 / / / _// , _// // /|_/ / __ |/ ,< / __ |_\ \_/ // _  /   _\ \/ __ |/ /|_/ / ___/ __ |_/ /  / // / /_/ / /|_/ / ___/ __ |/_/_/_/ 
/_/ /___/_/|_/___/_/  /_/_/ |_/_/|_/_/ |_/___/___/_//_( ) /___/_/ |_/_/  /_/_/  /_/ |_/___/  \___/\____/_/  /_/_/  /_/ |_(_|_|_)  
                                                      |/                                                             ''')


if __name__ == "__main__":
    main()
