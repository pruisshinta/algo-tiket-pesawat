import os
import time
import json

#### PEMBUKA ####
print("="*41)
print("BUY YOUR TICKET HERE, HAVE A SAFE FLIGHT!")
print("="*41)
print("")

#### ATUR TANGGAL ####
def date():
    print("Departure Date")
    tanggal = int(input("Date (1-31)       : "))
    while tanggal > 31:
        print("Please input the right day")
        tanggal = int(input("Date (1-31)       : "))
    bulan = int(input ("Month (1-12)      : "))
    while bulan > 12:
        print("Please input the right month")
        bulan = int(input ("Month (1-12)      : "))
    tahun = int(input ("Year              : "))
    while tahun < 2020:
        print ("Please input the current year")
        tahun = int(input ("Year              : "))

#### PANGGIL JSON ####
def admin():
    with open('admin.json') as database:
        tmp = json.load(database)
    return tmp

#### TAMPILKAN MENU ####
def showData(base):
    if isinstance(base, list):
        os.system('cls')
        #print('') 
        print('-'*65)
        print('%-2s | %-17s | %-13s | %-10s | %-2s'%('NO','ARRIVAL','TIME','PRICE','STATUS'))
        print('-'*65)
        for idx, item in enumerate(base,1):
            print('%-2s | %-17s | %-13s | %-10s | %-2s'%(idx,item['ARRIVAL'],item['TIME'],item['PRICE'],item['STATUS']))
        print('-'*65)
    else:
        print('Tipe data tidak sesuai')
        exit()

#### ADMINISTRASI ####
def pesan():
    tiket = list()
    penumpang = int(input("Passengers        : "))
    print("-"*53)
    print("Please, input the name of passengers")
    basenama = []
    for i in range (int(penumpang)):
        nama = input("Name              : ")
        basenama.append(nama)
    time.sleep(2)
    total_tiket = penumpang*harga
    os.system('cls')
    print("LOADING...")
    time.sleep(2)
    cetak(indeks,penumpang,basenama,total_tiket)

#### BUKA JSON DATAUSER ####
json_case= 'Datauser.json'
def loaduser(json_case):
    with open(json_case, 'r') as output:
        if os.stat(json_case).st_size==0:
            return []
        else:
            _data = json.load(output)
            return _data

#### CETAK STRUK PEMBAYARAN ####
def cetak(idx,penumpang,basenama,totaltiket):
    v = ({"user" : username, 'pass' : password,'arival' : idx['ARRIVAL'],'waktu' : idx['TIME'], 'jumlah' : penumpang,'nama' : basenama, 'total' : totaltiket})
    ender.append(v)
    with open(json_case,'w') as b:
        b.write(json.dumps(ender, indent = 2))
    print('Destination\t: '+idx['ARRIVAL']+'\nTIME\t\t: '+idx['TIME'])
    print('Passengers\t: '+str(penumpang))
    print('Nama penumpang\t: '+', '.join(basenama))
    print("-"*53)
    print("Total price","Rp.",(totaltiket))
    print("-"*53)

#### PEMBATAS ####
def garis():
    print("-"*53)

#### BACA JSON AKUN ADMIN ###
def loadAkunAmin():
    with open('akunAdmin.json','r') as baseAkun:
        akun = json.load(baseAkun)
    return akun


data = admin()
dataAkunAdmin = loadAkunAmin()
#### Pilih Role ####
while True:
    ender = loaduser(json_case)
    role = [" 1.User\n","2.Admin\n","3.Exit"]
    print(" ".join(role))
    choice = int(input("Login as : "))

    #### LOGIN SEBAGAI USER ####
    if choice == 1:
        while True:
            username =  input("Username : ")
            password =  input("Password : ")
            print("Verivying your account....")
            time.sleep(2)
            os.system('cls')
            print('Welcome ',username)
            showData(data)
            indeks = data[int(input("Choose your destination : "))-1]
            harga = int(indeks['PRICE'])
            date()
            garis()
            pesan()
            peryakinan = int(input("1. Yes  2. No\n"+"Is it right? "))
            if peryakinan == 1:
                os.system('cls')
                print("You have successfully made a ticket purchase")
                print("THANKYOU")
                time.sleep(2)
                os.system('cls')
                break
            else:
                continue
        
    #### LOGIN SEBAGAI ADMIN ####
    elif choice == 2:
        while True :
            username = input("Username : ")
            password = input("password : ")
            print("Verivying your account....")
            time.sleep(2)
            os.system('cls')
            for i in dataAkunAdmin:
                if username==i['username'] and password==i['password']:
                    os.system('cls')
                    print('Welcome ',i['username'])
                    time.sleep(2.0)
                    os.system('cls')
                    menu = [' 1. Menampilkan data\n', '2. Menambah\n', '3. Edit\n', '4. Hapus\n', '5. Lihat Jumlah Pemasukkan\n', '6. Exit']
                    while True:
                        print(' '.join(menu))
                        choice = input('Pilih Menu: ')
                        os.system('cls')
                        if choice=='1':
                            showData(data)
                        elif choice=='2':
                            arrival = input('Arrival: ')
                            time = input('Time: ')
                            price = input('Price: ')
                            status = input('Status: ')
                            tmp = {'ARRIVAL': arrival, 'TIME': time, 'PRICE': price, 'STATUS': status}
                            data.append(tmp)
                            data_dump = json.dumps(data)
                            with open('admin.json','w') as output:
                                output.write(data_dump)
                        elif choice=='3':
                            showData(data)
                            idx = int(input('Pilih nomer data: ')) - 1
                            data.pop(idx)
                            arrival = input('Arrival: ')
                            time = input('Time: ')
                            price = input('Price: ')
                            status = input('Status: ')
                            tmp = {'ARRIVAL': arrival, 'TIME': time, 'PRICE': price, 'STATUS': status}
                            data.append(tmp)
                            data_dump = json.dumps(data)
                            with open('admin.json','w') as output:
                                output.write(data_dump)
                        elif choice=='4':
                            showData(data)
                            idx = int(input('Pilih nomer data: ')) - 1
                            data.pop(idx)
                            showData(data)
                            data_dump = json.dumps(data)
                            with open('admin.json','w') as output:
                                output.write(data_dump)
                        elif choice == "5" :
                            print('Lihat Laporan')
                            with open('Datauser.json','r') as dataTransaksi:
                                jual = json.load(dataTransaksi)
                            if dataTransaksi == []:
                                print('Belum ada data')
                            pemasukkan = 0
                            transaksi = 0
                            for i in jual:
                                pemasukkan += int(i['total'])
                                transaksi += int(i['jumlah'])
                            print('Jumlah pemasukkann     : ', pemasukkan)
                            print('Jumlah pembelian tiket : ', transaksi)
                            print("")
                            garis()
                            print("")
                        elif choice=='6':
                            break
                        else:
                            print("Opsi salah")
                            time.sleep(1.0)
                            break
            break       

    elif choice==3:
        break          
    else:
        print("Choose the right number, please!")