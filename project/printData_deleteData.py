import os


def printData():
#     nama_file = input("Masukkan nama file (.txt) :")
    try:
        infile = open(nama_file, "r")
        print(infile.read())
        infile.close()
    except FileNotFoundError:
        print("Nama File", nama_file , "Tidak ada")



def deleteDaata():
#     nama_file = input("Masukkan nama file (.txt) : ")
    try:
        os.remove(nama_file)
        print("NOTIFIKASI : File", nama_file, "Berhasil Dihapus \n")
    except FileNotFoundError:
        print("Nama File", nama_file , "Tidak ditemukan")
