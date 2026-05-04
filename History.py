import Pencatatan
import Database

space = ""

def History(riwayat):
    for i in range(len(riwayat)):
        if (riwayat[i]["tipe"]) == "p":
            print("==================================================================================") 
            print(f"{space.ljust(23)}Transaksi {riwayat[i]["waktu"]} {space.ljust(23)}")
            print("+---+--------------+----------------------+---------------+----------------------+")
            print(f"|No |     {"Nama".ljust(6)}   |        {"Produk".ljust(10)}    |     {"Harga".ljust(6)}    |       {"Pembayar".ljust(12)}   |")
            History_Peritem(mambo=i,riwayat=riwayat)       
        else:
            print("==================================================================================") 
            print(f"{space.ljust(23)}Transaksi {riwayat[i]["waktu"]} {space.ljust(23)}")
            print("+---+--------------+----------------------+---------------+----------------------+")
            print(f"|No |     {"Nama".ljust(6)}   |        {"Produk".ljust(10)}    |     {"Harga".ljust(6)}    |       {"Pembayar".ljust(12)}   |")
            History_Flat(mambo=i,riwayat=riwayat)       


def History_Flat(mambo,riwayat):
    desc = Pencatatan.description(teks=riwayat[mambo]["deskripsi"])
    print("+---+--------------+----------------------+---------------+----------------------+")
    historyr = riwayat[mambo]
    k = 0
    harga = f"{historyr["harga"]:g}"
    try:
        for i in range(len(historyr["part"])):
            print(f"| {i+1} | {historyr["part"][i]["nama"].ljust(12)} |", end="")
            for j in range(len(historyr["part"])):
                if j == 0 and k == 0: 
                    print(f" {historyr["produk"].ljust(20)} | {str(harga).ljust(13)} | {historyr["payer"].ljust(20)} |")
                    k = 1
                elif j == 0:
                    print(f" {historyr["produk"].ljust(20)} | {str(harga).ljust(13)} | {space.ljust(20)} |")
            if i == len(historyr["part"])-1:
                print("+---+--------------+----------------------+---------------+----------------------+")
            else:
                print(f"+---+--------------+----------------------+---------------+ {space.ljust(21)}|")
    except IndexError: pass

    print("Catatan:")
    for i in range(len(desc)):
        if i == 0:
            print(f"     {desc[i]}")
        else:
            print(f"  {desc[i]}")


def History_Peritem(mambo,riwayat):
    desc = Pencatatan.description(teks=riwayat[mambo]["deskripsi"])
    print("+---+--------------+----------------------+---------------+----------------------+")
    no = 1
    k = 0
    historyp = riwayat[mambo]
    try:
        for i in range(len(historyp["part"])):
            print(f"| {no} | {historyp["part"][i]["nama"].ljust(12)} |", end="")
            for j in range(len(historyp["part"][i]["produk"])):
                harga = historyp["part"][i]["produk"][j]["harga"]
                item = historyp["part"][i]["produk"][j]["item"]
                if j == 0 and k == 0: 
                    print(f" {item.ljust(20)} | {str(harga).ljust(13)} | {historyp["payer"].ljust(20)} |")
                    k = 1
                elif j == 0:
                    print(f" {item.ljust(20)} | {str(harga).ljust(13)} | {space.ljust(20)} |")
                else:
                    print(f"|   |              | {item.ljust(20)} | {str(harga).ljust(13)} | {space.ljust(20)} |")
            no += 1
            if i == len(historyp["part"])-1:
                print("+---+--------------+----------------------+---------------+----------------------+")
            else:
                print(f"+---+--------------+----------------------+---------------+ {space.ljust(21)}|")
    except IndexError: pass

    print("Catatan:")
    for i in range(len(desc)):
        if i == 0:
            print(f"     {desc[i]}")
        else:
            print(f"  {desc[i]}") 


def History_Hutang(hutang):
    print("===================================================") 
    print(f"{space.ljust(17)}Riwayat Hutang {space.ljust(17)}")
    print("+---+--------------+--------------+---------------+")
    print(f"|No |     {"Nama".ljust(6)}   |    {"Jumlah".ljust(6)}    |    {"Bayar ke".ljust(6)}   |")
    print("+---+--------------+--------------+---------------+")
    for i in range(len(hutang)):
        cetak = "%g"% hutang[i]["jumlah"]
        print( f"|{i+1}. | {hutang[i]["nama"].ljust(12)} | {str(cetak).ljust(12)} | {hutang[i]["ke"].ljust(13)} |")
        print("+---+--------------+--------------+---------------+")
        i += 1

def History_Pembayaran():
    p = Database.akses()
    pembayaran = p[3]
    print("===================================================") 
    print(f"{space.ljust(16)}Riwayat Pembayaran {space.ljust(16)}")
    print("+---+--------------+--------------+---------------+")
    print(f"|No |     {"Nama".ljust(6)}   |    {"Dibayarkan".ljust(6)}    |    {"Ke".ljust(6)}   |")
    print("+---+--------------+--------------+---------------+")
    for i in range(len(pembayaran)):
        cetak = "%g"% pembayaran[i]["jumlah"]
        print( f"|{i+1}. | {pembayaran[i]["nama"].ljust(12)} | {str(cetak).ljust(12)} | {pembayaran[i]["ke"].ljust(13)} |")
        print("+---+--------------+--------------+---------------+")
        i += 1
 
