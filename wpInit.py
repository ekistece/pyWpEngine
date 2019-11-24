import os, sys, win32gui, platform
progman = win32gui.FindWindow('Progman', None)

# Try older method if newer one fails
if win32gui.SendMessage(progman, 0x052C, 0xD, 0) and win32gui.SendMessage(progman, 0x052C, 0xD, 1):
    win32gui.SendMessage(progman, 0x052C, 0, 0)

def callback(hwnd, hwnds):
    if not win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None):
        return True
    pworker = win32gui.FindWindowEx(0, hwnd, "WorkerW", None)
    if pworker:
        print('Worker: ' + str(pworker))
        print('Progman: ' + str(progman))
        hwnds.append(pworker)
        return
    return True
hwnds = []
win32gui.EnumWindows(callback, hwnds)
worker = hwnds[0]

def writeConf(hwnd):
    with open('hwnd.conf', 'w') as s:
        s.write(str(hwnd))

#if Win7 hide worker and run mpv on progman
if (platform.release() == '7'):
    print('Detected Windows 7')
    print('MPV HWND: ' + str(progman) + '\nHIDDEN WORKER: ' + str(worker))
    win32gui.ShowWindow(worker, 0)
    writeConf(progman)
else:
    print('MPV HWND: ' + str(worker))
    writeConf(worker)
