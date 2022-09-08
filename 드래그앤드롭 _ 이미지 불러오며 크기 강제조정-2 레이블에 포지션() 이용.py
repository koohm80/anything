import sys, os
from tkinter import Scale
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

global counter
counter = 0

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n 여기 드랍 \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')
        self.setAcceptDrops(True)


    def setPixmap(self, image):
        super().setPixmap(image)

    

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(500, 660)
        self.setWindowTitle('드래그앤드롭 이미지')
        self.setAcceptDrops(True)

        mainLayout = QVBoxLayout()
        
        self.photoViewer = ImageLabel()
        self.photoViewer.move(200, 200)  
        mainLayout.addWidget(self.photoViewer)

        self.photoViewer2 = ImageLabel()   
        self.photoViewer.move(200, 200)     
        mainLayout.addWidget(self.photoViewer2)

        ############################################################        
        self.setLayout(mainLayout)

        # widget = QWidget()
        # widget.setLayout(mainLayout)
        #                                     #### 레이블 위에서는 실시간 좌표 안 됨
        # self.setCentralWidget(widget)
        # self.setCentralWidget(mainLayout)
        ############################################################

        # self.statusbar = self.statusBar()
        

        print(self.hasMouseTracking())
        self.setMouseTracking(True)   # True 면, mouse button 안눌러도 , mouse move event 추적함.
        print(self.hasMouseTracking())

        self.show()

    def mouseMoveEvent(self, event):
        print('(%d %d)' % (event.x(), event.y()))

        # txt = "Mouse 위치 ; x={0},y={1}, global={2},{3}".format(event.x(), event.y(), event.globalX(), event.globalY())
        # self.statusbar.showMessage(txt)
        # global counter
        # if 12 <= event.x() <= 486 and 12 <= event.y() <= 312:
        #     counter = 0
        #     print(counter)
        # elif 12 <= event.x() <= 486 and 323 <= event.y() <= 626:
        #     counter = 1
        #     print(counter)

        # print(event.globalX())

    def mouseReleaseEvent(self, event):  # event : QMouseEvent
        print('BUTTON RELEASE')
        print('(%d %d) 릴리즈 위치' % (event.x(), event.y()))



    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        global counter
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            
            position = event.pos()          ##### 드롭 이벤트때 포지션으로 위치 지정 가능 하네 굿!
            print(position)

            if 12 <= position.x() <= 486 and 12 <= position.y() <= 312:
                counter = 0
                print(counter)
            elif 12 <= position.x() <= 486 and 323 <= position.y() <= 626:
                counter = 1
                print(counter)
                
            if counter == 0:
                self.photoViewer.setPixmap(QPixmap(file_path).scaled(500,330,Qt.IgnoreAspectRatio))
            elif counter == 1:
                self.photoViewer2.setPixmap(QPixmap(file_path).scaled(500,330,Qt.IgnoreAspectRatio))
    
                # self.set_image(file_path)
            
            
            event.accept()
        else:
            event.ignore()

    # def set_image(self, file_path):
    #     print(file_path, '상')    ###
    #     self.photoViewer.setPixmap(QPixmap(file_path).scaled(500,330,Qt.IgnoreAspectRatio))

    # def set_image2(self, file_path):
    #     print(file_path, '하')    ###
    #     self.photoViewer2.setPixmap(QPixmap(file_path).scaled(500,330,Qt.IgnoreAspectRatio))

        '''
        QPixmap QPixmap::scaled(int width, int height, Qt::AspectRatioMode aspectRatioMode = Qt::IgnoreAspectRatio, Qt::TransformationMode transformMode = Qt::FastTransformation) const
        https://doc.qt.io/qt-6/qpixmap.html#scaled
        '''

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())