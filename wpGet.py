import os, sys, requests, re, zipfile


steamUrl = input("Paste a steam workshop link here to retrieve the wallpaper: \n")

# Settings
path = os.getcwd()
zipPath = os.path.join(path, 'tmp.zip')
fileTypes = ['.mp4', '.avi']
storagePath = os.path.join(path, 'Wallpapers')


# Parsing steam URL
wpId = re.split('=|&', steamUrl)[1]

# Get the wallpaper name from steam and store it as folder name
r = requests.get(steamUrl)
wpName = re.search(r'class="workshopItemTitle">(.*?)<',str(r.content)).group(1)
wpPath = os.path.join(storagePath, wpName)

# Check if wallpaper already exists
if os.path.isdir(wpPath):
        print('Wallpaper ' + wpName + ' already downloaded, skipping!')
        sys.exit()

# Using steamworkshop.download service to download the file
r = requests.post(url = 'http://steamworkshop.download/online/steamonline.php', data = {'item': wpId, 'app': '431960'})
downloadUrl = re.search(r'href=[\'"]?([^\'" >]+)',str(r.content)).group(1)
r = requests.get(downloadUrl)
with open(zipPath, 'wb') as s:
    s.write(r.content)

# Unzip videos from zip file and remove after extracting
with zipfile.ZipFile(zipPath, 'r') as z:
	for f in z.infolist():
		if f.filename.endswith('.mp4'):
                        f.filename = 'wp.mp4'
                        z.extract(f,wpPath)
os.remove(zipPath)
