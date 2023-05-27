#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Mode admin mungkin error jika program tidak dijalankan menggunakan jupyter notebook
# Jangan sampai salah memasukkan input yang diminta program
# Jika salah memasukkan input, data mungkin terhapus

def write_LH():
    outfile=open('price_list.txt','w')
    
    harga=list_harga
    i=0
    while i<3:
        outfile.write(str(harga[i])+",")
        i+=1
        
    outfile.close()
    
def write_LP():
    outfile=open('lokasi_perusahaan.txt','w')
    i=int(input("Indeks berapa yang ingin anda ubah? "))
    lokasi_perusahaan[i]=input("Masukkan lokasi baru: ")
    n=int(input("Ketik 1 untuk tambah elemen: "))
    if n==1:
        tambah_1_element=True
    else:
         tambah_1_element=False
    i=len(lokasi_perusahaan)
    for x in range (0,i):
        if x==i-1 and tambah_1_element==True:
            outfile.write(lokasi_perusahaan[x]+"\n*")
        else:
            outfile.write(lokasi_perusahaan[x]+"\n")
    outfile.close()
    
def ambil_LH():
    import numpy as np
    f = np.genfromtxt('price_list.txt',delimiter=',')
    list_harga=f
    print(list_harga)

def ambil_LP():
    import numpy as np
    f = np.loadtxt('lokasi_perusahaan.txt',delimiter='\n',dtype=object)
    return f
    
def ambil_UP():
    import numpy as np
    f = np.loadtxt('admin.txt', delimiter=',', skiprows=0, dtype=str)
    return f

def choose():
    print("Apa yang ingin anda lakukan?\n1 ubah harga\n2 ubah lokasi penjualan\n3 selesai")
    return int(input())
    
def pilihan1():
    ambil_LH()
    print("Indeks berapa yang ingin anda ubah?")
    indeks=int(input())
    print("Masukkan harga baru")
    list_harga[indeks]=int(input())
    write_LH()
    ambil_LH()
        
def pilihan2():
    lokasi_perusahaan=ambil_LP()
    print(lokasi_perusahaan)
    write_LP()
    lokasi_perusahaan=ambil_LP()
    print(lokasi_perusahaan)
        
import numpy as np
f = np.genfromtxt('price_list.txt',delimiter=',')
list_harga=f
    
import numpy as np
f = np.loadtxt('lokasi_perusahaan.txt', delimiter='\n',dtype=object)
if len(f)==0:
    f=["*"]
elif len(f)==1:
    f=[f[0],'*']
lokasi_perusahaan=f

akun=0
selesai=False
while selesai==False:
    print("Ketik:\n1 jika anda admin\n2 jika anda user\n3 untuk keluar")
    akun=int(input())
    if akun==1:
        get_ipython().run_line_magic('run', 'program_login.py')
        admin_=ambil_UP()
        admin=False
        if admin_[0]=="admin_ganteng" and admin_[1]=="admin1234":
            admin=True
        if admin==True:
            print("Anda adalah admin")
            masih_admin=True
            while masih_admin==True:
                pilih=choose()
                if pilih==1:
                    while pilih==1:
                        pilihan1()
                        U=input("Apakah anda ingin mengubah harga lagi?\nYa atau Tidak\n")
                        if U=="Ya" or U=="ya":
                            pilih=1
                        if U=="Tidak" or U=="tidak":
                            pilih=0
                if pilih==2:
                    while pilih==2:
                        pilihan2()
                        U=input("Apakah anda ingin mengubah lokasi lagi?\nYa atau Tidak\n")
                        if U=="Ya"or U=="ya":
                            pilih=2
                        if U=="Tidak"or U=="tidak":
                            pilih=0
                if pilih==3:
                    masih_admin=False
                
    if akun==2:
        volume=int(input("Masukkan volume minyak jelantah yang akan dihitung (Liter): "))
        for i in range (0,3):
            print("Harga jual minyak jelantah "+str(list_harga[i]*volume)+" rupiah\nDi "+str(lokasi_perusahaan[i]))
        print("")
    if akun==3:
        selesai=True


# In[ ]:




