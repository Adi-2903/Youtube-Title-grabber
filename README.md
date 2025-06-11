# YT Title Grabber

YT Title Grabber is a simple Python command-line tool that allows you to fetch and list the titles of all videos in a YouTube playlist. It also provides an option to copy the entire list of titles to your clipboard for easy use.

## Features

- Fetches playlist title.
- Lists all video titles within the playlist.
- Supports colored output for better readability.
- Option to copy all titles to the clipboard.

## Prerequisites

Before you begin, ensure you have Python 3.8 or higher installed on your system.

## Installation

1.  **Clone the repository (or download the `main.py` file):**

    ```bash
    git clone https://github.com/your-username/YT-Title-Grabber.git
    cd YT-Title-Grabber
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**

    -   **Windows (Command Prompt):**

        ```bash
        .venv\Scripts\activate
        ```

    -   **Windows (PowerShell):**

        ```powershell
        .venv\Scripts\Activate.ps1
        ```

    -   **macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

4.  **Install the required libraries:**

    ```bash
    pip install yt-dlp colorama pyperclip
    ```

## Usage

1.  **Run the script:**

    Make sure your virtual environment is activated.

    ```bash
    python main.py
    ```

2.  **Enter the YouTube Playlist URL:**

    The script will prompt you to enter the URL of the YouTube playlist.

    ```
    Enter YouTube Playlist URL: [Paste your playlist URL here]
    ```

3.  **View and Copy Titles:**

    The playlist title and all video titles will be displayed. You will then be asked if you want to copy the list to your clipboard.

    ```
    Do you want to copy the list to clipboard? (Y/N): 
    ```

    Enter `Y` (or `y`) to copy, or `N` (or `n`) if you don't want to copy.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests if you have suggestions or improvements!
