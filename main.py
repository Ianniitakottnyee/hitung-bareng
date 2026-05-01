import Pencatatan
import User
import Calculation
import History
import time
import Database
suasana = time.localtime()

try:
    Database.Open()
except ValueError:
    kurawal = {}
    Database.Save(kurawal)

if suasana[3]<4 or suasana[3]>19:
    print("Selamat malam!")
elif suasana[3]<11:
    print("Selamat pagi!")
elif suasana[3]<14:
    print("Selamat siang!")
else:
    print("Selamat sore!")
try:
    while True:
        print("========  HITUNG BARENG ========")
        print("menu:")
        print("     1. Tambahkan anggota baru.")
        print("     2. Catat transaksi.")
        print("     3. Riwayat.")
        print("     4. Pembayaran.")
        print("     5. Fitur tambahan.")
        print("     6. Keluar.")

        fitur = Pencatatan.Check(pesan="Input angka untuk mengakses menu: ", eror="input tidak valid")
        if fitur == 1:
            print("==== Menu Tambahkan Anggota ====")
            User.Add_Users()
        elif fitur == 2:
            Pencatatan.Transaction()
        elif fitur == 3:
            p = Database.akses()
            while True:
                print("Riwayat:\n1. Transaksi.\n2. Hutang.")
                r = Pencatatan.Check(pesan="riwayat: ", eror="mode yang dipilih tidak valid!")            
                if r == 1:
                    try:
                        History.History(p[1])
                    except KeyError: print("Belum ada riwayat transaksi.")
                    break
                elif r == 2:
                    Calculation.Net_Debt()
                    try:
                        History.History_Hutang(p[2])
                    except KeyError: print("Belum ada riwayat hutang.")
                    break
                else:
                    print("mode tidak valid.")
        elif fitur == 4:
            ...
        elif fitur == 5:
            User.Show_Users()
            User.Delete_User()
        elif fitur == 6:
            print("=================  Terimakasih!!  =================")
            break
        else:
            print("Fiturnya cuman 4 wok\n")
except KeyboardInterrupt: 
    print(f"\n=================  Terimakasih!!  =================")
    #History.History_Peritem(participant, payer)
#save_data(users, transactions)

