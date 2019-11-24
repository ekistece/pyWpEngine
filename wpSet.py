import subprocess, os

#Get hwnd
hwnd = None
with open('hwnd.conf', 'r') as f:
    hwnd = int(f.read())

#Choose wallpaper
wps = os.listdir('Wallpapers')
count = 0
for wp in wps:
    print('[' + str(count) + '] ' + wp)
sel = int(input("\nChoose a number: "))
wp = os.path.join(os.getcwd(), 'Wallpapers', wps[sel], 'wp.mp4')


subprocess.run(["bin\mpv","--wid",str(hwnd),"--no-audio","--loop-file",wp])
