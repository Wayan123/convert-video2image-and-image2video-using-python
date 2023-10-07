import cv2
import os

# Fungsi untuk memotong gambar dari video hingga mencapai jumlah frame yang diinginkan
def potong_gambar(video_file):
    cap = cv2.VideoCapture(video_file)
    
    frame_rate = 2  # Frame rate yang diinginkan (1 frame setiap 0.5 detik)
    frame_count = 0
    
    # Ambil nama file video tanpa ekstensi
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    
    # Buat folder output dengan nama yang sesuai dengan video
    output_directory = f"{video_name}_frames"
    os.makedirs(output_directory, exist_ok=True)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_count += 1
        
        # Hanya potong gambar pada frame yang sesuai dengan frame rate yang diinginkan
        if frame_count % int(cap.get(5) / frame_rate) == 0:
            output_file = f"{output_directory}/frame_{frame_count}.jpg"
            cv2.imwrite(output_file, frame)
            print(f"Frame ke-{frame_count} telah dipotong dan disimpan sebagai {output_file}")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_file = r"your_video.mp4"  # Ganti dengan nama video Anda
    
    potong_gambar(video_file)
