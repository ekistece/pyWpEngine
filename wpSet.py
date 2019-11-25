import subprocess, os

#Choose wallpaper
wps = os.listdir('Wallpapers')
count = 0
for wp in wps:
    print('[' + str(count) + '] ' + wp)
    count += 1
sel = int(input("\nChoose a number: "))
wp = os.path.join(os.getcwd(), 'Wallpapers', wps[sel], 'wp.mp4')

with open('wp.conf','wb') as f:
    f.write(wp.encode('utf-8'))

#subprocess.run(["bin\mpv","--wid",str(hwnd),"--no-audio","--loop-file",wp])
#os.system('bin\mpv --wid ' + str(hwnd) + ' --no-audio --loop-file ' + wp)
