import cv2
import os

# Function to merge images in sequence based on file names
def merge_images_in_sequence(image_directory, output_video):
    image_files = [f for f in os.listdir(image_directory) if f.endswith(".jpg")]
    image_files.sort()  # Sort images based on file names

    if not image_files:
        print("No image files (.jpg) found in the directory.")
        return

    # Read the resolution of the first image for video settings
    first_image = cv2.imread(os.path.join(image_directory, image_files[0]))
    height, width, layers = first_image.shape

    # Initialize the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # MP4 video compression format
    out = cv2.VideoWriter(output_video, fourcc, 2, (width, height))  # Frame rate: 2 frames per second

    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        frame = cv2.imread(image_path)
        out.write(frame)  # Write frames to the video

    out.release()  # Close the VideoWriter object
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_directory = r"images_directory"  # Replace with the directory where your images are stored
    output_video = "output_video.mp4"  # Name of the output video file

    merge_images_in_sequence(image_directory, output_video)
