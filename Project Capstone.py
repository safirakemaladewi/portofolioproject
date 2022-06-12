listProduk = [
    {
        'kode produk' : 'RM-VA-01',
        'nama' : 'Vanilla',
        'produsen' : 'Darjeeling',
        'stock' : 20,
        'netto' : 100,
        'harga' : 150000
    },
    {
        'kode produk' : 'RM-PA-01',
        'nama' : 'Patchouli',
        'produsen' : 'Darjeeling',
        'stock' : 30,
        'netto' : 150,
        'harga' : 200000
    },
    {
        'kode produk' : 'RM-JA-01',
        'nama' : 'Jasmine',
        'produsen' : 'Bali Garden',
        'stock' : 25,
        'netto' : 100,
        'harga' : 145000
        
    },
    {
        'kode produk' : 'RM-TB-01',
        'nama' : 'Tuberose',
        'produsen' : 'Bali Garden',
        'stock' : 15,
        'netto' : 200,
        'harga' : 250000
        
    }
]


def reportSeluruhData(): #read
    print ('Daftar Bahan Baku - Produk Essential Oil\n')
    print ('Kode Produk \t| Nama Produk \t\t| Produsen \t| Stock (pcs)   | Netto(ml)     | Harga (Satuan)')
    for i in range (len(listProduk)):
        print('{} \t| {} \t\t| {} \t| {}\t\t| {}\t\t| {}' .format(listProduk[i]['kode produk'], listProduk[i]['nama'], listProduk[i]['produsen'], listProduk[i]['stock'], listProduk[i]['netto'], listProduk[i]['harga']))
        
        
def reportDataTertentu(): #read
    inputKode = input('Masukkan Kode Produk : ')
    index = 0
    for i in range (len(listProduk)):
        if (inputKode == listProduk[i]['kode produk']):
            break
            
        index += 1
        
    if (index  == len(listProduk)):
        print('******Tidak Ada Data Produk******')
        opsiMenuRead()
    else:
        print ('Data dengan Kode Produk : {} \n' .format(inputKode))
        print ('Kode Produk \t| Nama Produk \t\t| Produsen \t| Stock(pcs) | Netto(ml) | Harga (Satuan)')
        print('{} \t| {} \t\t| {} \t| {} \t\t| {} \t\t| {}' .format(listProduk[i]['kode produk'], listProduk[i]['nama'], listProduk[i]['produsen'], listProduk[i]['stock'], listProduk[i]['netto'], listProduk[i]['harga']))
            
            
def menampilkanDaftarProduk(): #read
    while(True):
        pilihanSubMenu = input('''
=======================================Menampilkan Laporan Data Stock=========================================

List Sub Menu Read Data:

1. Report Seluruh Data
2. Report Data Tertentu
3. Kembali ke Menu Utama

Silahkan Pilih Sub-Menu Utama [1-3] : ''')
        if (pilihanSubMenu == '1'):
            reportSeluruhData()
        elif (pilihanSubMenu == '2'):
            reportDataTertentu()
        elif (pilihanSubMenu == '3'):
            Menu_Utama() 
        else:
            continue

def opsiMenuRead(): 
    while(True):
        pilihanOpsi = input('''
==============================================================================================================

1. Kembali Mengakses Sub Menu
2. Kembali ke Menu Utama

Silahkan Pilih Opsi Menu [1-2] : ''')
        if (pilihanOpsi == '1'):
            menampilkanDaftarProduk()
        elif (pilihanOpsi == '2'):
            Menu_Utama()
        else:
            print('Pilihan yang Anda Masukkan Salah')
            
          
        
def tambahDataProduk(): #create
    kodeProduk = str(input('Masukkan kode produk : '))
    index = 0
    for i in range (len(listProduk)):
        if (kodeProduk == listProduk[i]['kode produk']):
            break
            
        index += 1
    
    if (index  == len(listProduk)):
        namaProduk = str(input('Masukkan nama produk : '))
        prodProduk = str(input('Masukkan produsen produk : '))
        stockProduk = int(input('Masukkan stock produk : '))
        nettProduk = int(input('Masukkan netto produk : '))
        hrgProduk = int(input('Masukkan harga produk : '))
        while(True):
            checker = input('Apakah Data Produk akan disimpan? (Y/N) = ')
            if (checker == 'Y' or checker == 'y'):
                listProduk.append({
                    'kode produk' : kodeProduk,
                    'nama' : namaProduk,
                    'produsen' : prodProduk,
                    'stock' : stockProduk,
                    'netto' : nettProduk,
                    'harga' : hrgProduk
                })
                print('Data Tersimpan')
                opsiMenuCreate()    
            elif (checker == 'N' or checker == 'n'):
                opsiMenuCreate() 
            else:
                continue
    else:
        print ('******Data sudah ada******')
        opsiMenuCreate()
        
    
            
def menambahDataProduk(): #create
     while(True):
        pilihanSubMenu = input('''
=======================================Menambah Data Produk=========================================

List Sub Menu Create Data:

1. Tambah Data Produk
2. Kembali ke Menu Utama

Silahkan Pilih Sub-Menu Utama [1-2] : ''')
        if (pilihanSubMenu == '1'):
            tambahDataProduk()
        elif (pilihanSubMenu == '2'):
            Menu_Utama() 
        else:
            continue
            
def opsiMenuCreate(): 
    while(True):
        pilihanOpsi = input('''
==============================================================================================================

1. Kembali Mengakses Sub Menu
2. Kembali ke Menu Utama

Silahkan Pilih Opsi Menu [1-2] : ''')
        if (pilihanOpsi == '1'):
            menambahDataProduk()
        elif (pilihanOpsi == '2'):
            Menu_Utama()
        else:
            print('Pilihan yang Anda Masukkan Salah')
            

def ubahDataProduk():
    reportSeluruhData()
    kodeProduk = str(input('Masukkan kode produk : '))
    index = 0
    for i in range (len(listProduk)):
        if (kodeProduk == listProduk[i]['kode produk']):
            break
            
        index += 1
        
    if (index  == len(listProduk)):
        print('******Data yang Anda cari tidak ada******')
        mengubahDataProduk()
    else:
        print ('Kode Produk \t| Nama Produk \t\t| Produsen \t| Stock(pcs) | Netto(ml) | Harga (Satuan)')
        print('{} \t| {} \t\t| {} \t| {} \t\t| {} \t\t| {}' .format(listProduk[i]['kode produk'], listProduk[i]['nama'], listProduk[i]['produsen'], listProduk[i]['stock'], listProduk[i]['netto'], listProduk[i]['harga']))
        while(True):
            checker = input('Lanjut update? (Y/N) = ')
            if (checker == 'Y' or checker == 'y'):
                inputKey = input('''
Catatan: 
Input keterangan kolom yang sudah ada sesuai dengan yang di bawah ini! Input kolom menggunakan huruf kecil.
1. kode produk untuk Kode Produk
2. nama untuk Nama Produk
3. produsen untuk Produsen
4. stock untuk Stock
5. netto untuk Netto
6. harga untuk Harga

Masukkan Kolom yang akan di-update : ''')
                
                inputVal = input('Masukkan {} Baru : ' .format(inputKey))
                while(True):
                    checker2 = input('Apakah data akan di-update? (Y/N) = ')
                    if (checker2 == 'Y' or checker2 == 'y'):
                        listProduk[i][inputKey] = inputVal
                        print('Data Updated')
                        opsiMenuUpdate()    
                    elif (checker2 == 'N' or checker2 == 'n'):
                        opsiMenuUpdate()
                    else:
                        continue     
            elif (checker == 'N' or checker == 'n'):
                opsiMenuUpdate()
            else:
                continue
                
            
def mengubahDataProduk(): #update
     while(True):
        pilihanSubMenu = input('''
=======================================Mengubah Data Produk=========================================

List Sub Menu Update Data:

1. Ubah Data Produk
2. Kembali ke Menu Utama

Silahkan Pilih Sub-Menu Utama [1-2] : ''')
        if (pilihanSubMenu == '1'):
            ubahDataProduk()
        elif (pilihanSubMenu == '2'):
            Menu_Utama() 
        else:
            continue

            
def opsiMenuUpdate(): 
    while(True):
        pilihanOpsi = input('''
==============================================================================================================

1. Kembali Mengakses Sub Menu
2. Kembali ke Menu Utama

Silahkan Pilih Opsi Menu [1-2] : ''')
        if (pilihanOpsi == '1'):
            mengubahDataProduk()
        elif (pilihanOpsi == '2'):
            Menu_Utama()
        else:
            print('Pilihan yang Anda Masukkan Salah')
            
            
def hapusDataProduk():
    reportSeluruhData()
    kodeProduk = str(input('Masukkan kode produk : '))
    index = 0
    for i in range (len(listProduk)):
        if (kodeProduk == listProduk[i]['kode produk']):
            break
            
        index += 1
        
    if (index  == len(listProduk)):
        print('******Data yang Anda cari tidak ada******')
        menghapusDataProduk()
    else:
        while(True):
            checker = input('Apakah Anda Yakin untuk menghapus data ini? (Y/N)')
            if (checker == 'Y' or checker == 'y'):
                del listProduk[i]
                print('Data dengan kode produk {} sudah dihapus' .format(kodeProduk))
                menghapusDataProduk()
            elif (checker == 'N' or checker == 'n'):
                menghapusDataProduk()
            else:
                continue
                
    
def menghapusDataProduk(): #delete
    while(True):
        pilihanSubMenu = input('''
=======================================Menghapus Data Produk=========================================

List Sub Menu Delete Data:

1. Hapus Data Produk
2. Kembali ke Menu Utama

Silahkan Pilih Sub-Menu Utama [1-2] : ''')
        if (pilihanSubMenu == '1'):
            hapusDataProduk()
        elif (pilihanSubMenu == '2'):
            Menu_Utama() 
        else:
            continue

def opsiMenuDelete(): 
    while(True):
        pilihanOpsi = input('''
==============================================================================================================

1. Kembali Mengakses Sub Menu
2. Kembali ke Menu Utama

Silahkan Pilih Opsi Menu [1-2] : ''')
        if (pilihanOpsi == '1'):
            menghapusDataProduk()
        elif (pilihanOpsi == '2'):
            Menu_Utama()
        else:
            print('Pilihan yang Anda Masukkan Salah')
            
              
def Menu_Utama():       
    while(True):
        pilihanMenu = input('''
=========Laporan Data Stock Bahan Baku - Produk Essential Oil========

List Menu Utama:

1. Menampilkan Laporan Data Stock
2. Menambah Data Produk
3. Mengubah Data Produk
4. Menghapus Data Produk
5. Exit Program

Silahkan Pilih Menu Utama [1-5] : ''')
        if (pilihanMenu == '1'): #read data
            menampilkanDaftarProduk()
        
        elif (pilihanMenu == '2'): #crate data
            menambahDataProduk()
            
        elif (pilihanMenu == '3'): #delete data
            mengubahDataProduk()
        
        elif (pilihanMenu == '4'):
            menghapusDataProduk()
            
        elif (pilihanMenu == '5'):
            break #exit program
        
        else:
            print('Pilihan yang Anda Masukkan Salah')

            
Menu_Utama()
