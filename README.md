# convert-video2image-and-image2video
Simple python code for convert video to image and image to video

Kode ini adalah sebuah skrip Python yang digunakan untuk memotong sebuah video menjadi frame-frame gambar dengan interval waktu tertentu, kemudian menyimpannya sebagai file gambar. Beberapa poin utama tentang kode ini:

1. Menggunakan pustaka OpenCV untuk membaca video dan memproses frame-frame video.
2. Menggunakan frame rate yang diinginkan (dalam contoh ini, 1 frame setiap 0.5 detik) untuk menentukan interval pemotongan frame.
3. Setiap frame gambar disimpan dalam folder output yang sesuai dengan nama video tanpa ekstensi sebagai "nama_video_frames".
4. Hasil pemotongan berupa file gambar dengan format JPG yang disimpan di folder output.
5. Pada akhirnya, skrip ini akan menghasilkan serangkaian gambar yang merepresentasikan frame-frame dari video yang telah dipotong sesuai dengan interval waktu yang diinginkan.

Pastikan untuk mengganti "your_video.mp4" dengan nama video yang ingin Anda proses.
