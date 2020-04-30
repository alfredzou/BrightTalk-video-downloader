import wget
import os
import urllib.parse as parse
import subprocess

def main():
    while (download() != 0):
        pass

    print('All downloads complete.')

def download():
    '''
    Example links
    source: https://www.brighttalk.com/webcast/8657/372236
    last_link = "https://cdn02.brighttalk.com/core/asset/video/372234/ios/iphone/video_1568913534-2_00012.ts"

    source: https://www.brighttalk.com/webcast/17108/397311
    last_link = "https://cdn02.brighttalk.com/core/asset/video/397303/ios/iphone/video_1586160232-2_00268.ts"
    '''

    url = parse.urlparse(input('Enter last .ts URL link: '))

    # check for valid URL
    if url.scheme not in ['http', 'https'] or url.netloc == '':
        print('Invalid URL: Syntax error.')
        return 1

    if 'brighttalk.com' not in url.netloc:
        print('Invalid URL: Expected brighttalk.com domain.')
        return 1

    if url.path[-3:] != '.ts':
        print('Invalid URL: Expected .ts file.')
        return 1

    # parse URL
    lastFilename = os.path.basename(url.path)

    try:
        length = int(lastFilename[-8:-3]) + 1
    except:
        print('Invalid URL')
        return 1
    
    # create dir if not exists
    try:
        os.mkdir('temp')
    except:
        pass

    # download all the .ts files for a brighttalk video
    for id in range(length):
        print(f'Downloading: {id}.ts')
        filename = lastFilename[:-8] + str(id).zfill(5) + lastFilename[-3:]
        link = parse.urljoin(url.geturl(), filename)
        wget.download(link, f'./temp/{id}.ts')
        print('\n')

    return 0

if __name__ == "__main__":
    main()
