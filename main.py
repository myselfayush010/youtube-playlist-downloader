import yt_dlp
import argparse
from pathlib import Path

def download_playlist(url, output_dir, audio_only=False, resolution='best'):  # Added resolution parameter
    Path(output_dir).mkdir(exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else f'bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/best[height<={resolution}]/best',
        'format_sort': ['res:1080', 'ext:mp4:m4a', 'size'],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'no_cache_dir': True,
        'quiet': False,
        'progress': True,
        'ignoreerrors': True,
        'merge_output_format': 'mp4'
    }
    
    if audio_only:
        ydl_opts.update({
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'm4a',
                'preferredquality': '0',  # Best quality
            }],
            'format': 'bestaudio/best',
            'postprocessor_args': [
                '-ar', '48000',
                '-b:a', '320k'
            ]
        })
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    parser = argparse.ArgumentParser(description='YouTube playlist downloader')
    parser.add_argument('url', help='Playlist URL')
    parser.add_argument('-o', '--output', default='downloads', help='Output folder')
    parser.add_argument('-a', '--audio-only', action='store_true', help='Download audio only (highest quality)')
    parser.add_argument('-r', '--resolution', default='best', help='Video resolution (e.g., 1080, 720, etc.)')  # Added resolution argument
    args = parser.parse_args()
    
    download_playlist(args.url, args.output, args.audio_only, args.resolution)  # Pass resolution to download function

if __name__ == '__main__':
    main()