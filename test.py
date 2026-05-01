import Pencatatan
import History
import Database
space = ""
p = Database.akses()
def History(riwayat):
    for i in range(len(riwayat)):
        if (riwayat[i]["tipe"]) == "p":
            print("==========================================================================") 
            print(f"{space.ljust(20)}Transaksi {riwayat[i]["waktu"]} {space.ljust(20)}")
            print("+---+--------------+--------------+---------------+----------------------+")
            print(f"|No |     {"Nama".ljust(6)}   |    {"Produk".ljust(6)}    |     {"Harga".ljust(6)}    |       {"Pembayar".ljust(12)}   |")
            History_Peritem(mambo=i,riwayat=riwayat)       
        else:
            print("==========================================================================") 
            print(f"{space.ljust(20)}Transaksi {riwayat[i]["waktu"]} {space.ljust(20)}")
            print("+---+--------------+--------------+---------------+----------------------+")
            print(f"|No |     {"Nama".ljust(6)}   |    {"Produk".ljust(6)}    |     {"Harga".ljust(6)}    |       {"Pembayar".ljust(12)}   |")
            History_Flat(mambo=i,riwayat=riwayat)       


def History_Flat(mambo,riwayat):
    desc = Pencatatan.description(teks=riwayat[mambo]["deskripsi"])
    print("+---+--------------+--------------+---------------+----------------------+")
    historyr = riwayat[mambo]
    k = 0
    try:
        for i in range(len(historyr["part"])):
            print(f"| {i+1} | {historyr["part"][i]["nama"].ljust(12)} |", end="")
            for j in range(len(historyr["part"])):
                if j == 0 and k == 0: 
                    print(f" {historyr["produk"].ljust(12)} | {str(historyr["harga"]).ljust(13)} | {historyr["payer"].ljust(20)} |")
                    k = 1
                elif j == 0:
                    print(f" {historyr["produk"].ljust(12)} | {str(historyr["harga"]).ljust(13)} | {space.ljust(20)} |")
            if i == len(historyr["part"])-1:
                print("+---+--------------+--------------+---------------+----------------------+")
            else:
                print(f"+---+--------------+--------------+---------------+ {space.ljust(21)}|")
    except IndexError: pass

    print("Catatan:")
    for i in range(len(desc)):
        if i == 0:
            print(f"     {desc[i]}")
        else:
            print(f"  {desc[i]}")


def History_Peritem(mambo,riwayat):
    desc = Pencatatan.description(teks=riwayat[mambo]["deskripsi"])
    print("+---+--------------+--------------+---------------+----------------------+")
    no = 1
    k = 0
    historyp = riwayat[mambo]
    try:
        for i in range(len(historyp["part"])):
            print(f"| {no} | {historyp["part"][i]["nama"].ljust(12)} |", end="")
            for j in range(len(historyp["part"][i]["produk"])):
                if j == 0 and k == 0: 
                    print(f" {historyp["part"][i]["produk"][j]["item"].ljust(12)} | {str(historyp["part"][i]["produk"][j]["harga"]).ljust(13)} | {historyp["payer"].ljust(20)} |")
                    k = 1
                elif j == 0:
                    print(f" {historyp["part"][i]["produk"][j]["item"].ljust(12)} | {str(historyp["part"][i]["produk"][j]["harga"]).ljust(13)} | {space.ljust(20)} |")
                else:
                    print(f"|   |              | {historyp["part"][i]["produk"][j]["item"].ljust(12)} | {str(historyp["part"][i]["produk"][j]["harga"]).ljust(13)} | {space.ljust(20)} |")
            no += 1
            if i == len(historyp["part"])-1:
                print("+---+--------------+--------------+---------------+----------------------+")
            else:
                print(f"+---+--------------+--------------+---------------+ {space.ljust(21)}|")
    except IndexError: pass

    print("Catatan:")
    for i in range(len(desc)):
        if i == 0:
            print(f"     {desc[i]}")
        else:
            print(f"  {desc[i]}") 


#print(p[1][0])
History(p[1])