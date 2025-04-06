#создай тут фоторедактор Easy Editor!
import os
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
    GaussianBlur, UnsharpMask
)


app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('easi edidi')
lbmj = QLabel('Kartinka')
bwer = QPushButton('Papka')
lwf = QListWidget()

leef = QPushButton('Leva')
praa = QPushButton('Prava')
zercalo = QPushButton('Zercalo')
rezc = QPushButton('Rezcost')
Ch_b = QPushButton('CH/B')
sava = QPushButton('Save')
Resetic = QPushButton('Sbrosit filtri')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(bwer)
col1.addWidget(lwf)

col2.addWidget(lbmj)

rowowo = QHBoxLayout()
rowowo.addWidget(leef)
rowowo.addWidget(praa)
rowowo.addWidget(zercalo)
rowowo.addWidget(rezc)
rowowo.addWidget(Ch_b)
rowowo.addWidget(sava)
rowowo.addWidget(Resetic)
col2.addLayout(rowowo)

row.addLayout(col1,20)
row.addLayout(col2,80)
win.setLayout(row)

win.show()

working = ''
def filter(files,extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorking():
    global working
    working = QFileDialog.getExistingDirectory()


def showfgfgfggfg():
    extensions = ['.jpg', '.jpeg','.png', '.gif', '.bmp']
    chooseWorking()
    filenames = filter(os.listdir(working), extensions)
    lwf.clear()
    for filename in filenames:
        lwf.addItem(filename)


bwer.clicked.connect(showfgfgfggfg)

class Idfg():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def loaI(self,dir,filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)

    def ShoI(self,path):
        lbmj.hide()
        pixmapimage = QPixmap(path)
        w ,h = lbmj.width(),lbmj.height()
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        lbmj.setPixmap(pixmapimage)
        lbmj.show()

    def venom(self):
        self.image = self.image.convert('L')
        self.saveI()
        image_path = os.path.join(working,self.save_dir,self.filename)
        self.ShoI(image_path)

    def levo(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveI()
        image_path = os.path.join(working,self.save_dir,self.filename)
        self.ShoI(image_path)

    def zercloo(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveI()
        image_path = os.path.join(working,self.save_dir,self.filename)
        self.ShoI(image_path)

    def rezca(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.saveI()
        image_path = os.path.join(working,self.save_dir,self.filename)
        self.ShoI(image_path)


    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveI()
        image_path = os.path.join(working,self.save_dir,self.filename)
        self.ShoI(image_path)

    def saveI(self):
        path = os.path.join(self.dir,self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)


workimage = Idfg()

def showwwww():
    if lwf.currentRow() >= 0:
        filename = lwf.currentItem().text()
        workimage.loaI(working, filename)
        image_path = os.path.join(workimage.dir,workimage.filename)
        workimage.ShoI(image_path)

lwf.currentRowChanged.connect(showwwww)
Ch_b.clicked.connect(workimage.venom)
leef.clicked.connect(workimage.levo)
praa.clicked.connect(workimage.right)
zercalo.clicked.connect(workimage.zercloo)
rezc.clicked.connect(workimage.rezca)
Resetic.clicked.connect(showwwww)

app.exec()