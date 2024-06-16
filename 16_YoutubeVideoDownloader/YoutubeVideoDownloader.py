import os
import pytube
import moviepy.editor as mp


def video_downloader(url):
    yt = pytube.YouTube(url)
    progressive_streams = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().all()

    video_streams = yt.streams.filter(adaptive=True, only_video=True, file_extension="mp4").order_by(
        "resolution").desc().all()
    audio_streams = yt.streams.filter(adaptive=True, only_audio=True, file_extension="mp4").all()

    print("available formats: ")
    idx = 1
    stream_dict = {}

    for stream in progressive_streams:
        print(f"{idx}. {stream.resolution} - {stream.mime_type} - progressive (can be fast)")
        stream_dict[idx] = stream
        idx += 1
    for stream in video_streams:
        print(f"{idx}. {stream.resolution} - {stream.mime_type} - Adaptive (can be slow)")
        stream_dict[idx] = stream
        idx += 1

    choice = int(input(f"Select the quality (1-{len(stream_dict)}): "))
    if 1 <= choice <= len(stream_dict):
        selected_stream = stream_dict[choice]

        if "video" in selected_stream.mime_type and selected_stream.is_progressive:
            print(f"Downloading '{yt.title}' at resolution {selected_stream.resolution}...")
            selected_stream.download()
            print("Download completed!")

        elif "video" in selected_stream.mime_type and not selected_stream.is_progressive:
            print(f"Downloading '{yt.title}' at resolution {selected_stream.resolution} (Video only)...")
            video_file = selected_stream.download(filename="video.mp4")

            print("Downloading audio...")
            best_audio = audio_streams[0]
            audio_file = best_audio.download(filename="audio.mp4")

            print("Combining video and audio...")
            video_clip = mp.VideoFileClip(video_file)
            audio_clip = mp.AudioFileClip(audio_file)
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(f"{yt.title}.mp4")

            os.remove(video_file)
            os.remove(audio_file)

            print("Download and combine completed!")

        else:
            print("Invalid selection.")


if __name__ == '__main__':
    URL = input("Enter Youtube URL: ")
    video_downloader(URL)
