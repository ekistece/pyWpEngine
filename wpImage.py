import subprocess, os

# Screen resolution
screen = '1920:1080'

#Choose wallpaper
wps = os.listdir('Wallpapers')
count = 0
for wp in wps:
    print('[' + str(count) + '] ' + wp)
    count += 1
sel = int(input("\nChoose a number: "))
wp = os.path.join(os.getcwd(), 'Wallpapers', wps[sel])

os.system('bin\\ffmpeg -i "' + wp + '\\wp.mp4" -r 1 -s ' + screen + ' -frames:v 1 "' + wp + '\\wp.jpg" -hide_banner')

