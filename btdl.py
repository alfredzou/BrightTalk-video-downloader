import PySimpleGUI as sg
import ffmpeg
import os
import re
import requests

"""
Download BrightTalk Videos with a GUI interface
"""

sg.theme("GreenTan")

# Window
width = 100

# Columns
left_width = 12
right_width = 6
middle_width = width - left_width - right_width

# Layout
layout = [
    [
        sg.Text(".m3u8 link:", size=(left_width, 1), font=("Helvetica", 11)),
        sg.Input(size=(middle_width, 1), key="-M3U8-",),
    ],
    [
        sg.Text(".mp4 file name:", size=(left_width, 1), font=("Helvetica", 11)),
        sg.Input(size=(middle_width, 1), key="-MP4-",),
    ],
    [
        sg.Text("Download folder:", size=(left_width, 1), font=("Helvetica", 11)),
        sg.InputText(
            readonly=True,
            disabled_readonly_background_color="light grey",
            size=(middle_width, 1),
            key="-DLFOLD-",
        ),
        sg.FolderBrowse(size=(right_width, 1), font=("Helvetica", 11)),
    ],
    [
        sg.Button("Download", font=("Helvetica", 11)),
        sg.Button("Example", font=("Helvetica", 11)),
        sg.Button("Clear", font=("Helvetica", 11)),
    ],
]

# Window
window = sg.Window("BrightTalk Downloader", layout)

# Functions
def example():
    """
    Downloads a video from "https://www.brighttalk.com/webcast/8657/372236" into the current directory
    """
    window["-M3U8-"].update(
        "https://cdn02.brighttalk.com/core/asset/video/372234/ios/iphone/video_1568913534-2.m3u8"
    )
    window["-MP4-"].update("How Multi-Asset Strategies Deliver")
    window["-DLFOLD-"].update(os.getcwd())


def clear():
    """
    Clears all user input
    """
    window["-M3U8-"].update("")
    window["-MP4-"].update("")
    window["-DLFOLD-"].update("")


def clean_file_name(file_name):
    """
    Removes any characters that are illegal for windows operating system files
    """
    clean_name = re.sub(r"[/\\:*?<>|]", "", file_name)
    return clean_name


def check_m3u8_URL(m3u8_URL):
    """
    Checks if it's a .m3u8 URL
    """
    clean_m3u8_URL = m3u8_URL
    # If there is no protocol, add the protocol
    if not re.search("^https://", m3u8_URL):
        clean_m3u8_URL = "https://" + m3u8_URL

    if not re.search(".m3u8$", m3u8_URL):
        sg.popup_error("Not a .m3u8 link")
        raise TypeError("Not a .m3u8 link")

    return clean_m3u8_URL


def download():
    """
    Using the .m3u8 playlist file, ffmpeg downloads all associated stream files and concatenates them into a .mp4 file.
    
    Returns:
    .mp4 file with specified name into specified directory.
    """

    # Validate is a .m3u8 URL
    try:
        input_m3u8 = check_m3u8_URL(values["-M3U8-"])
    except TypeError:
        return

    # Validate directory has been set
    if values["-DLFOLD-"] == "":
        sg.popup_error("Specify download folder")
        return

    # Remove special characters from output file name to create output path
    # Check if OS is Windows
    if os.name == 'nt':
        output_mp4 = values["-DLFOLD-"] + "\\" + clean_file_name(values["-MP4-"]) + ".mp4"
    # Correct output path for macOS and Linux
    else:
        output_mp4 = values["-DLFOLD-"] + "/" + clean_file_name(values["-MP4-"]) + ".mp4"

    # ffmpeg downloads and concats all associated stream files into a .mp4 file
    sg.popup_auto_close("Please be patient while video file downloads")
    try:
        ffmpeg.input(input_m3u8).output(output_mp4).run(overwrite_output=True)
        sg.popup("Video downloaded")
    except:
        sg.popup_error("Error occurred")


# Event Loop
if __name__ == "__main__":
    while True:
        event, values = window.read()
        if event is None:
            break
        if event in ("Clear"):
            clear()
        if event in ("Download"):
            download()
        if event in ("Example"):
            example()

    window.close()
