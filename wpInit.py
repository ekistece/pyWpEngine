import os, win32gui, platform, subprocess

def setWallpaper(p):
    win32gui.SystemParametersInfo(20, p, 0)

def spawnWorkerW():
    progman = win32gui.FindWindow('Progman', None)
    if win32gui.SendMessage(progman, 0x052C, 0xD, 0) or win32gui.SendMessage(progman, 0x052C, 0xD, 1):
        win32gui.SendMessage(progman, 0x052C, 0, 0)
    def callback(hwnd, enum):
        workerw = win32gui.FindWindowEx(0, hwnd, "WorkerW", None)
        if win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None) and workerw:
            enum.append(workerw)
            return
        return True
    enum = []
    win32gui.EnumWindows(callback, enum)
    if (platform.release() == '7'):
        win32gui.ShowWindow(enum[0], 0)
        return progman
    return enum[0]

def readConf(f):
    with open(f,'rb') as f:
        return f.read().decode('utf-8')

def main():
    wpPath = readConf('wp.conf')
    workerId = spawnWorkerW()
    setWallpaper(wpPath.replace('.mp4','.jpg'))
    os.system('taskkill /f /im mpv.exe')
    subprocess.Popen('bin\mpv --wid ' + str(workerId) + ' --hwdec=dxva2-copy --fps=30 --no-audio --loop-file "' + wpPath + '"')
    return

if __name__ == "__main__":
    main()
