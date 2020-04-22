import wget
import os

# creates directory if it doesn't exist
try:
    os.mkdir('temp')
except:
    pass

# Example links
# source: https://www.brighttalk.com/webcast/8657/372236
# last_link = "https://cdn02.brighttalk.com/core/asset/video/372234/ios/iphone/video_1568913534-2_00012.ts"

# source: https://www.brighttalk.com/webcast/17108/397311
# last_link = "https://cdn02.brighttalk.com/core/asset/video/397303/ios/iphone/video_1586160232-2_00268.ts"

# Prompts user input for the last .ts file URL link
last_link = input('Last .ts URL link: ')
length = int(last_link[-8:-3])+1

# download all the .ts files for a brighttalk video
for id in range(length):
    link = last_link[:-8] + str(id).zfill(5) + last_link[-3:]
    path = f'./temp/{id}.ts'
    print(f'Downloading: {id}.ts')
    wget.download(link, path)
    print('\n')