from colorama import Fore, Style, init
import pyperclip
import yt_dlp

init(autoreset=True)  # Automatically reset colors after each print

def get_youtube_playlist_titles(playlist_url):
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True, # Only extract basic info, not full video data
            'force_generic_extractor': True, # Helps with some playlist issues
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=False)
            
            if 'entries' not in info_dict or not info_dict['entries']:
                print(f"{Fore.RED}❌ No videos found in the playlist or playlist is empty.")
                return

            playlist_title = info_dict.get('title', 'Unknown Playlist')
            print(f"\n{Fore.CYAN}📚 Playlist Title: {Fore.YELLOW}{playlist_title}\n")
            print(f"{Fore.MAGENTA}🎬 Videos in Playlist:\n")

            result_text = f"📚 Playlist: {playlist_title}\n\n"
            for index, video_entry in enumerate(info_dict['entries'], start=1):
                video_title = video_entry.get('title', 'Untitled Video')
                line = f"{index}. {video_title}"
                print(f"{Fore.GREEN}{line}")
                result_text += line + "\n"

        # Always ask to copy, even if no videos found
        choice = input(f"\n{Fore.BLUE}Do you want to copy the list to clipboard? (Y/N): ").strip().lower()
        if choice == 'y':
            pyperclip.copy(result_text)
            print(f"{Fore.GREEN}✅ Titles copied to clipboard!")
        else:
            print(f"{Fore.RED}❌ Not copied.")

    except yt_dlp.utils.DownloadError as e:
        print(f"{Fore.RED}❌ yt-dlp Error: {e}")
    except Exception as e:
        print(f"{Fore.RED}❌ An unexpected error occurred: {e}")

# 🔗 Run the tool
if __name__ == "__main__":
    url = input(f"{Fore.YELLOW}Enter YouTube Playlist URL: ")
    get_youtube_playlist_titles(url)
