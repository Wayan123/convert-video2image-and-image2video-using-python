import cv2
import os

# Fungsi untuk menggabungkan gambar-gambar dalam urutan berdasarkan nama file
def gabungkan_gambar_urutan(gambar_directory, output_video):
    gambar_files = [f for f in os.listdir(gambar_directory) if f.endswith(".jpg")]
    gambar_files.sort()  # Urutkan gambar berdasarkan nama file

    if not gambar_files:
        print("Tidak ada file gambar (.jpg) dalam direktori.")
        return

    # Baca resolusi gambar pertama untuk pengaturan video
    first_image = cv2.imread(os.path.join(gambar_directory, gambar_files[0]))
    height, width, layers = first_image.shape

    # Inisialisasi objek VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Format kompresi video MP4
    out = cv2.VideoWriter(output_video, fourcc, 2, (width, height))  # Frame rate: 2 frame per detik

    for gambar_file in gambar_files:
        gambar_path = os.path.join(gambar_directory, gambar_file)
        frame = cv2.imread(gambar_path)
        out.write(frame)  # Menulis frame ke video

    out.release()  # Menutup objek VideoWriter
    cv2.destroyAllWindows()

if __name__ == "__main__":
    gambar_directory = r"D:\COMPETITION\Sayembara RDD Berbasis AI (Publik)\VIDEO_2204011_JLN. RAYA LIMBANGAN (LIMBANGAN)_ARAHNORMAL_frames"  # Ganti dengan direktori tempat gambar-gambar Anda disimpan
    output_video = "output_video.mp4"  # Nama file untuk video keluaran

    gabungkan_gambar_urutan(gambar_directory, output_video)

