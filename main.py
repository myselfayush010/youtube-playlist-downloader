import yt_dlp
import argparse
from pathlib import Path

def download_playlist(url, output_dir):
    Path(output_dir).mkdir(exist_ok=True)
    
    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]/best',
        'format_sort': ['res:1080', 'ext:mp4:m4a', 'size'],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'no_cache_dir': True,
        'quiet': False,
        'progress': True,
        'ignoreerrors': True,
        'merge_output_format': 'mp4'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    parser = argparse.ArgumentParser(description='YouTube playlist downloader')
    parser.add_argument('url', help='Playlist URL')
    parser.add_argument('-o', '--output', default='downloads', help='Output folder')
    args = parser.parse_args()
    
    download_playlist(args.url, args.output)

if __name__ == '__main__':
    main()