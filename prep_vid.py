import cv2

def video_to_frames(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    count = 0
    success, frame = cap.read()
    while success:
        cv2.imwrite(f"{output_dir}/frame_{count:04d}.jpg", frame)
        success, frame = cap.read()
        count += 1
    cap.release()

video_to_frames('YogaDog.mp4', 'dataset/val/images')
