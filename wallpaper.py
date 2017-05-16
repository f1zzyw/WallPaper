# -*- coding; utf-8 -*-


import os
import win32api, win32gui, win32con
from PIL import Image
import getpass
import time


def readWallfile(path):
    files_list = os.listdir(path)
    files = [i for i in files_list if os.path.getsize(path + '\\' + i) > 200000]
    files.sort(key=lambda f: os.path.getmtime(path + '\\' + f))
    file_path = os.path.join(path, files[-1])
    return file_path


def setWallpaper(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "1")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, win32con.SPIF_SENDWININICHANGE)


if __name__ == '__main__':
    path = readWallfile(
        'C:\\Users\\%s\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets' % getpass.getuser())
    f = Image.open(path)
    filename = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    if not os.path.exists('E:\\wallpaper'):
        os.makedirs('E:\\wallpaper')
    f.save('E:\\wallpaper\\' + filename + '.bmp')
    npath = 'E:\\wallpaper\\' + filename + '.bmp'
    setWallpaper(npath)
