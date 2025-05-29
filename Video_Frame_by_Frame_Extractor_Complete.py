import os
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from PIL import Image

folder = str(input("Name of folder : "))
path = str(input("Path of folder : "))
video = str(input("Video url : "))

def video_extract(folder_name, folder_path, video_url, fps=1):
    #create folder
    full_path = os.path.join(folder_path, folder_name)
    os.makedirs(full_path)
    print(f"✅ Folder created")

    #Download video from yt
    save_path = os.path.join(full_path, "downloaded_video.mp4")
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': save_path,
        }
        with YoutubeDL(ydl_opts) as ydl:
            print("⬇️ Downloading video...")
            ydl.download([video_url])
            print(f"✅ Video downloaded")
    except Exception as e:
        print(f"❌ Error downloading video")
        return

    #Extract frames
    try:
        clip = VideoFileClip(save_path)
        for i, frame in enumerate(clip.iter_frames(fps=fps)):
            frame_path = os.path.join(full_path, f"frame_{i:04d}.jpg")
            Image.fromarray(frame).save(frame_path)
            print(f"🖼️ Saved frame: {frame_path}")
        print("✅ Frame extraction complete")
    except Exception as e:
        print(f"❌ Error extracting frames")


video_extract(
    folder_name=folder,
    folder_path=path,
    video_url=video,
    fps=1
)
