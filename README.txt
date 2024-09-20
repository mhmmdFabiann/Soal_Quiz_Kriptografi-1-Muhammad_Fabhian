Tugas Kriptografi
Proyek ini merupakan implementasi dari algoritma kriptografi Vigenère, Playfair, dan Hill Cipher. Program ini memungkinkan pengguna untuk mengenkripsi dan mendekripsi pesan baik dari input langsung maupun dari file teks.

Folder proyek terdiri dari empat file:
- `main.py`: File utama yang mengelola tampilan antarmuka dan interaksi pengguna.
- `vigenere.py`: Implementasi algoritma Vigenère.
- `playfair.py`: Implementasi algoritma Playfair.
- `hill.py`: Implementasi algoritma Hill Cipher.

Cara Penggunaan
1. Persyaratan:
   - Python 3.x
   - Library numpy (untuk operasi matriks)
   Install library numpy dengan perintah:
   pip install nump

2. Menjalankan Program:
   - Jalankan file main.py untuk memulai aplikasi.
   - Pilih jenis cipher (Vigenère, Playfair, Hill) dan pilih tindakan (enkripsi atau dekripsi).
   - Masukkan pesan dan kunci sesuai yang diminta.

3. Format Kunci:
   - Kunci harus memiliki panjang minimal 12 karakter untuk algoritma Playfair dan Vigenere
   - Untuk Hill cipher, 9 karakter pertama HARUS menggunakan RRFVSVCCT untuk key nya, sisanya bisa random

4. Input:
   - Pesan dapat diinput langsung melalui keyboard atau diambil dari file teks dengan format .txt.
  
Penjelasan Algoritma
1. Vigenère Cipher
Vigenère Cipher adalah metode enkripsi sederhana yang menggunakan kunci untuk mengubah huruf dalam pesan. Setiap huruf dalam pesan digeser berdasarkan huruf dalam kunci.

2. Playfair Cipher
Playfair Cipher merupakan algoritma kriptografi yang menggunakan 5x5 matriks dari huruf-huruf. Setiap pasangan huruf dalam pesan diproses untuk menghasilkan huruf enkripsi berdasarkan posisi mereka dalam matriks.

3. Hill Cipher
Hill Cipher menggunakan operasi matriks untuk mengenkripsi dan mendekripsi pesan. Kunci diubah menjadi matriks 3x3, dan pesan diubah menjadi vektor yang kemudian diproses menggunakan matriks kunci.
