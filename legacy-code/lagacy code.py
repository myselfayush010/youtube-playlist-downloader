import yt_dlp
import argparse
from pathlib import Path

def download_playlist(url, output_dir, resolution='1080'):
    Path(output_dir).mkdir(exist_ok=True)
    
    # Remove 'p' suffix if present
    resolution = str(resolution).replace('p', '')
    
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}][ext=mp4]+bestaudio[ext=m4a]/best[height<={resolution}]/best',
        'format_sort': ['res', 'ext:mp4:m4a'],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'no_cache_dir': True,
        'quiet': False,
        'progress': True,
        'ignoreerrors': True,
        'merge_output_format': 'mp4',
        'retries': 3
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading: {str(e)}")

# ...existing code...