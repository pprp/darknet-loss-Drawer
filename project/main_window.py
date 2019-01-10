
import sys
import qdarkstyle
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import QTimer
from Ui_Main import *
import os
from extract_log import *
from visualization_loss import *
from PyQt5.QtGui import QPixmap

class window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.slot_btn_chooseFile)
        self.cwd = os.getcwd()
        #self.ui.setWindowTitle("Loss Drawer")
        self.newName = 'eg'
        self.ignore = 0
        self.end = 0
        self.start = 100
        self.lines = 1000
        self.step = 30
        self.filePath = ''
        self.picName = 'tmp'
        
        self.ui.pushButton_2.clicked.connect(self.slot_change)
        self.ui.lineEdit.textChanged.connect(self.slot_line)
        self.ui.lineEdit_2.textChanged.connect(self.slot_step)
        self.ui.lineEdit_3.textChanged.connect(self.slot_start)
        self.ui.lineEdit_4.textChanged.connect(self.slot_end)
        self.ui.lineEdit_7.textChanged.connect(self.slot_newName)
        self.ui.lineEdit_5.textChanged.connect(self.slot_ignore)
        self.ui.lineEdit_8.textChanged.connect(self.slot_picName)
        
        
    
    def slot_picName(self):
        if self.ui.lineEdit_8.text()!='':
            self.picName = self.ui.lineEdit_8.text()
    def slot_line(self):
        if self.ui.lineEdit.text() != '':
            self.lines = int(self.ui.lineEdit.text())
    
    def slot_step(self):
        if self.ui.lineEdit_2.text() != '':
            self.step = int(self.ui.lineEdit_2.text())
    
    def slot_start(self):
        if self.ui.lineEdit_3.text() != '':
            self.start = int(self.ui.lineEdit_3.text())
    
    def slot_end(self):
        if self.ui.lineEdit_4.text() != '':
            self.end = int(self.ui.lineEdit_4.text())
    
    def slot_ignore(self):
        if self.ui.lineEdit_5.text() != '':
            self.ignore = int(self.ui.lineEdit_5.text())
    
    def slot_newName(self):
        self.newName = self.ui.lineEdit_7.text() + ".txt"
        
    def slot_btn_chooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    self.cwd, # 起始路径 
                                    "All Files (*);;Text Files (*.log)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件为:")
        print(fileName_choose)
        print("文件筛选器类型: ",filetype)
        self.ui.lineEdit_6.setText(fileName_choose)
        
        self.filePath = fileName_choose
        print(self.filePath)
    
    def slot_change(self):
        extract_log(self.filePath, self.newName, 'images')
        print("Extract Done")
        # def __init__(self, lines, step, start, end, ignore, data_path):
        l = loss(self.lines, self.step, self.start, self.end, self.ignore, self.cwd+'/'+'test.txt', self.picName)
        l.process()
        #v = visual(self.line, self.step, self.start, self.end, self.ignore, self.filePath)
        self.ui.label.setPixmap(QPixmap("./"+self.picName+".png"))
        self.ui.label.setScaledContents (True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    #app.setStyleSheet("QPushButton { margin: 1ex;font-size: 15pt; }")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    # create and show mainWindow
    mainWindow = window()
    mainWindow.show()
    sys.exit(app.exec_())
    
    
    
    
    
