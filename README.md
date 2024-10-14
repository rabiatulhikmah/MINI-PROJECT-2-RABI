# MINI-PROJECT-2 RABI
# Profil
Nama : Rabiatul Hikmah

Nim : 2409116049

Kelas : B

Tema : Pengelolaan Stok Toko Hijab
# Flowchart
![MINI PROJECK2 drawio (2)](https://github.com/user-attachments/assets/ac2e7ff9-afe5-4a01-a60a-03a1df9b4bdf)
# Menu utama

menu dimana user dapat memilih role.

![Screenshot 2024-10-14 225943](https://github.com/user-attachments/assets/5f92cad8-1aba-47ed-a055-55af1911e0bb)

# Penjelasan masing-masing role
1. akses karyawan gudang
   dapat melakukan sistem CRUD(Cread,Read,Update,Delete) pada database barang.
2. akses bersama
   dapat digunakan seluruh karyawan toko dan hanya bisa melihat stok barang yang ada
3. keluar
   maka program akan selesai atau berhenti

**jika user mennginput selain opsi diatas yaitu 1, 2 dan 3 maka otomatis akan kembali ke mode login**

seperti gambar di bawah ini :

![Screenshot 2024-10-14 232452](https://github.com/user-attachments/assets/7d6a9d9b-1e24-49d4-95ad-04032ebd285d)

# 1. Akses Karyawan Gudang 
pada role ini akan ada login yang menginput username dan juga password. 

* jika password yang dimasukkan salah maka program akan kembali ke menu role

![Screenshot 2024-10-14 233159](https://github.com/user-attachments/assets/f499a87f-8086-4682-875e-a2396d56f73a)

* jika password benar maka akses karyawan gudang akan terbuka dan mengeluarkan fitu-fitur yang ada

![Screenshot 2024-10-14 233901](https://github.com/user-attachments/assets/a83a286c-d6a5-4d93-b5a2-e56c78ff5727)

# <sub>Penjelasan Fitur Akses Karyawan Gudang<sub>

1. lihat stok
   
   untuk masuk ke fitur ini inputkan angka 1

    disini akan muncul stok barang yang ada di gudang.
   
  ![Screenshot 2024-10-14 235342](https://github.com/user-attachments/assets/f8e33c30-7b47-4c9d-a95b-2a0147dc0c56)
  
     

2. tambah barang

   untuk masuk fitur ini inputkan angka 2
   
   disini akan dilakukan penginputan nama barang lalu stok barang. setelah itu, jika berhasil      maka barang akan bertambah dalam daftar barang dan akan ditanya ingin melakukan penambahan      barang lagi atau tidak. jika menginput 'y' maka program akan mengulang namum jika selain       maka akan kembali ke menu karyawan gudang.

   ![Screenshot 2024-10-14 235657](https://github.com/user-attachments/assets/4ca93188-b4eb-40ec-a1d0-efd3e21d6319)

   **before**
   
   ![Screenshot 2024-10-15 012456](https://github.com/user-attachments/assets/0b2245af-c9ad-4d2f-871c-8a79a5454179)

   **after**

   ![Screenshot 2024-10-15 012506](https://github.com/user-attachments/assets/e8e9ab7e-8142-4e92-95aa-6d4b4756c790)


   jika barang yang diinput sudah ada dalam daftar barang maka, akan dilakukan penginputan         ulang dan harus memasukan barang yang belum ada di dalam daftar barang.

![Screenshot 2024-10-14 235952](https://github.com/user-attachments/assets/fa7f87f6-5f36-4471-9b8f-96d07f5096c8)

3. hapus barang

   untuk masuk fitur ini inputkan angka 3

   disini akan dilakukan penginputan nama barang, jika nama barang yang dimasukkan ada dalam       daftar barang maka barang tersebut akan dihapus dalam daftar. dan akan ditanya ingin            melakukan pengulangan atau tidak. jika menginput 'y' maka program akan mengulang namum jika selain y maka akan kembali ke menu karyawan gudang.

   jika nama yang dimasukkan tidak ada dalam daftar barang maka barang yang ada di dalam           daftar barang tidak akan berubah. dan akan ditanya ingin mengulang atau tidak.
   
      ![Screenshot 2024-10-15 001901](https://github.com/user-attachments/assets/f767475e-dfdd-4b7d-b6cd-3b5b9be3f8d0)

   **before**

     ![Screenshot 2024-10-15 012506](https://github.com/user-attachments/assets/3d5409c6-b722-4bfb-8cec-e865ef694a4b)

   **after**

    ![Screenshot 2024-10-15 012456](https://github.com/user-attachments/assets/87d20195-bbc2-4abb-ab93-81ac6b71538c)


4. update stok

   untuk masuk fitur ini inputkan angka 4

   disini akan dilakukan input nama barang dan stok barang baru. input nama barang harus nama yang ada di dalam daftar barang. sehingga stok barang yang ada di daftar barang akan terupdate dengan stok yang diinputkan tadi. jika berhasil tampilannya akan seperti ini dan langsung kembali ke manu karyawan gudang.

   ![Screenshot 2024-10-15 013222](https://github.com/user-attachments/assets/ef164706-1c25-44f4-bea9-bd5212a7862b)

   **before**

   ![Screenshot 2024-10-15 013239](https://github.com/user-attachments/assets/7621fbf5-d4dd-4c0e-bef9-311e88d58f53)

   **after**

   ![Screenshot 2024-10-15 013252](https://github.com/user-attachments/assets/10b06255-1407-4bcd-91cb-bfef80d7047b)

    dan jika nama barang yang diinput tidak ada, maka barang yang ada pada daftar barang tidak akan berubah dan akan langsung kembali ke menu karyawan gudang.

   ![Screenshot 2024-10-15 003246](https://github.com/user-attachments/assets/d56eb17b-6238-4d2d-a524-677ef37bff69)


 5. kembali
    
    jika menginput angka 5 maka program akan kembali ke menu utama yaitu menu memilih role

      ![Screenshot 2024-10-15 004511](https://github.com/user-attachments/assets/c55bba50-7e35-4ddd-9a29-64f206e944e7)


# 2. Akses Bersama

user akan diminta menginput nama : 

![Screenshot 2024-10-15 005921](https://github.com/user-attachments/assets/9b08614b-dd7c-4d4c-87d0-cd8b03f7283b)

# <sub>Penjelasan Fitur Akses Bersama<sub>

1. lihat stok
   
   untuk masuk fitur ini inputkan angka 1

   disini user akan melihat stok yang ada di gudang

   ![Screenshot 2024-10-15 010943](https://github.com/user-attachments/assets/6e4e9210-e2b3-42f7-abbb-85476239fecd)

2. kembali
   
   jika menginput angka 5 maka program akan kembali ke menu utama yaitu menu memilih role

   ![Screenshot 2024-10-15 011101](https://github.com/user-attachments/assets/9fdcc55a-aa55-48c8-a907-d8843aba6e4a)

# 3. Keluar

   jika memilih fitur ini maka program akan selesai atau berhenti yang ditandai dengan tulisan seperti ini :

   ![Screenshot 2024-10-15 011548](https://github.com/user-attachments/assets/b7937da0-7306-498f-8ab1-52ef172d6d84)

