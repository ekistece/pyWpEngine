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
wpOpt = wp + '_Optimized'
os.mkdir(wpOpt)

os.system('bin\\ffmpeg.exe -i "' + wp + '\\wp.mp4" -vf scale=' + screen + ',setsar=1:1 "' + wpOpt + '\\wp.mp4" -hide_banner')



