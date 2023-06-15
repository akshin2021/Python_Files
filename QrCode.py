import pyqrcode
def qrcode():
    s="Laude ho tum "
    d=pyqrcode.create(s)
    d.png('Image.png',scale=6)
    print('Code executed properly')

if __name__=='__main__':
    qrcode()

 #QRCode generated is saved in Image.png which is created in the project in pycharm. 
 #Installed pyqrcode and pyqrpng for this 
