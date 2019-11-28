import os, sys, requests, re, zipfile

def downloadFile(url,path):
    response = requests.get(url, stream=True)
    with open(path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:  # filter out keep-alive new chunks
                print('.', end='')
                f.write(chunk)
    return

def getWorkshopId(url):
    return re.split('=|&', url)[1]

def main():
    steamUrl = input("Paste a steam workshop link here to retrieve the wallpaper: \n")

    # Settings
    screen = '1920:1080'
    path = os.getcwd()
    zipPath = os.path.join(path, 'tmp.zip')
    fileTypes = ['.mp4', '.avi']
    storagePath = os.path.join(path, 'Wallpapers')
    wpId = getWorkshopId(steamUrl)
    # Get the wallpaper name from steam and store it as folder name
    r = requests.get(steamUrl)
    wpName = str(re.search(r'class="workshopItemTitle">(.*?)<',r.content.decode()).group(1))
    wpPath = os.path.join(storagePath, wpName)
    print('Downloading ' + wpName)

    # Check if wallpaper already exists
    if os.path.isdir(wpPath):
        print('Wallpaper ' + wpName + ' already downloaded, skipping!')
        sys.exit()

    # Using steamworkshop.download service to download the file
    r = requests.post(url = 'http://steamworkshop.download/online/steamonline.php', data = {'item': wpId, 'app': '431960'})
    downloadUrl = re.search(r'href=[\'"]?([^\'" >]+)',str(r.content)).group(1)
    downloadFile(downloadUrl,zipPath)

    # Unzip videos from zip file and remove after extracting
    with zipfile.ZipFile(zipPath, 'r') as z:
	    for f in z.infolist():
		    if f.filename.endswith('.mp4'):
                        f.filename = 'wp.mp4'
                        z.extract(f,wpPath)
    os.remove(zipPath)

    # Extract first frame to set as wallpaper with wpSet.py
    os.system('bin\\ffmpeg -i "' + wpPath + '\\wp.mp4" -r 1 -s ' + screen + ' -frames:v 1 "' + wpPath + '\\wp.jpg" -hide_banner')

if __name__ == "__main__":
    main()