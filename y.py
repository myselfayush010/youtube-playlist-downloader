import yt_dlp
import argparse
from pathlib import Path
import os

def download_content(url, output_dir, resolution='1080', audio_only=False):
    Path(output_dir).mkdir(exist_ok=True)
    
    if audio_only:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320'
            }],
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'no_cache_dir': True,
            'progress': True
        }
    else:
        resolution = str(resolution).replace('p', '')
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',  # Simplified format
            'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'no_cache_dir': True,
            'progress': True,
            'retries': 3,
            'fragment_retries': 3,
            'ignoreerrors': True
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download([url])
            if error_code != 0:
                raise Exception("Download failed")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Please ensure:")
        print("1. FFmpeg is installed: 'winget install ffmpeg'")
        print("2. yt-dlp is updated: 'pip install -U yt-dlp'")

def main():
    parser = argparse.ArgumentParser(description='YouTube downloader')
    parser.add_argument('url', help='Video URL')
    parser.add_argument('-o', '--output', default='downloads', help='Output folder')
    parser.add_argument('-r', '--resolution', default='1080', help='Video resolution')
    parser.add_argument('-a', '--audio', action='store_true', help='Download audio only (320kbps)')
    args = parser.parse_args()
    
    download_content(args.url, args.output, args.resolution, args.audio)

if __name__ == '__main__':
    main()