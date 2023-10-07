# convert-video2image-and-image2video
Simple python code for convert video to image and image to video

**Deskripsi 1: Mengubah Video Menjadi Gambar**

Kode ini adalah sebuah skrip Python yang digunakan untuk mengubah video menjadi serangkaian gambar dengan interval waktu tertentu. Beberapa poin utama tentang kode ini:

1. Menggunakan pustaka OpenCV untuk membaca video dan memproses frame-frame video.
2. Menggunakan frame rate yang diinginkan (dalam contoh ini, 1 frame setiap 0.5 detik) untuk menentukan interval pemotongan frame.
3. Setiap frame gambar disimpan dalam folder output yang sesuai dengan nama video tanpa ekstensi sebagai "nama_video_frames".
4. Hasil pemotongan berupa file gambar dengan format JPG yang disimpan di folder output.
5. Pada akhirnya, skrip ini akan menghasilkan serangkaian gambar yang merepresentasikan frame-frame dari video yang telah dipotong sesuai dengan interval waktu yang diinginkan.

Pastikan untuk mengganti "your_video.mp4" dengan nama file video yang ingin Anda proses.

**Deskripsi 2: Mengubah Gambar Menjadi Video**

Kode ini adalah sebuah skrip Python yang digunakan untuk mengubah serangkaian gambar dalam urutan tertentu menjadi sebuah video. Berikut adalah beberapa hal yang perlu diingat tentang kode ini:

1. Menggunakan pustaka OpenCV untuk membaca gambar-gambar dalam urutan berdasarkan nama file.
2. Urutkan gambar-gambar berdasarkan nama file.
3. Baca resolusi gambar pertama untuk pengaturan video sehingga video memiliki resolusi yang seragam.
4. Inisialisasi objek VideoWriter untuk menyimpan video.
5. Hasil video akan disimpan dengan format MP4 dan frame rate 2 frame per detik.
6. Pada akhirnya, skrip ini akan menghasilkan video dari serangkaian gambar yang diambil dalam urutan berdasarkan nama file.

Pastikan untuk mengganti "your_image_directory" dengan direktori tempat gambar-gambar Anda disimpan dan "output_video.mp4" dengan nama file video keluaran yang Anda inginkan.

**Cara menjalankan kedua kode**

**1: Mengubah Video Menjadi Gambar**

Kode ini adalah sebuah skrip Python yang digunakan untuk mengubah video menjadi serangkaian gambar dengan interval waktu tertentu. Berikut adalah beberapa poin utama tentang kode ini:

1. **Cara Menjalankan Kode:**
   - Pastikan Anda telah menginstal Python di komputer Anda.
   - Instal dependensi yang diperlukan dengan menjalankan perintah `pip install -r requirements.txt`, di mana `requirements.txt` berisi daftar dependensi termasuk OpenCV.
   - Tambahkan video yang ingin Anda proses ke dalam direktori yang sama dengan kode ini.
   - Ganti nama file video pada baris `video_file = "your_video.mp4"` dengan nama file video Anda.
   - Jalankan skrip Python dengan perintah `python nama_skrip.py`, di mana `nama_skrip.py` adalah nama file skrip Python yang Anda gunakan.
   - Hasil pemotongan gambar akan disimpan dalam folder `nama_video_frames` dalam format file JPG.

2. **Contoh Penggunaan:**
   - Anda memiliki video dengan nama "video.mp4".
   - Anda menjalankan skrip dengan perintah `python potong_video_ke_gambar.py`.
   - Gambar-gambar hasil pemotongan akan disimpan dalam folder "video_frames".

**Mengubah Gambar Menjadi Video**

Kode ini adalah sebuah skrip Python yang digunakan untuk mengubah serangkaian gambar dalam urutan tertentu menjadi sebuah video. Berikut adalah beberapa hal yang perlu diingat tentang kode ini:

1. **Cara Menjalankan Kode:**
   - Pastikan Anda telah menginstal Python di komputer Anda.
   - Instal dependensi yang diperlukan dengan menjalankan perintah `pip install -r requirements.txt`, di mana `requirements.txt` berisi daftar dependensi termasuk OpenCV.
   - Pastikan gambar-gambar yang ingin Anda gabungkan menjadi video telah ditempatkan dalam direktori yang sama dengan kode ini.
   - Ganti `"your_image_directory"` dengan direktori tempat gambar-gambar Anda disimpan.
   - Tentukan nama file video keluaran pada baris `output_video = "output_video.mp4"`.
   - Jalankan skrip Python dengan perintah `python nama_skrip.py`, di mana `nama_skrip.py` adalah nama file skrip Python yang Anda gunakan.
   - Hasil video akan disimpan dalam file "output_video.mp4".

2. **Contoh Penggunaan:**
   - Anda memiliki serangkaian gambar dengan nama "frame_1.jpg", "frame_2.jpg", dst., yang ingin Anda gabungkan menjadi video.
   - Anda menjalankan skrip dengan perintah `python gabungkan_gambar_ke_video.py`.
   - Video hasil penggabungan akan disimpan dalam file "output_video.mp4".
