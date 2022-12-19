from PyQt5.QtWidgets import QMainWindow
from ui.main_wnd import Ui_Detection
from ui.player_wnd import Ui_PlayerWindow
from ui.save_video_wnd import Ui_SavingVideo
import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QFrame, QPushButton, QFileDialog, QLabel, QDoubleSpinBox, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap, QImage
import video.video as video
import detection.detection as detect
import sqlite3
import io
from PyQt5.QtCore import QBuffer
import base64
from PIL import Image
import binascii


class MainWindow(QWidget, Ui_Detection):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.focus_direction = self.findChild(QDoubleSpinBox, 'numberFocus')
        self.button_load = self.findChild(QPushButton, 'btnLoadVideo')
        self.button_load.clicked.connect(lambda: self.btnLoadClicked())
        self.button_load = self.findChild(QPushButton, 'btnLoadSavingVideo')
        self.button_load.clicked.connect(lambda: self.btnSavingVideoClicked())
        self.show()
        self.detection = detect.Detection()
        self.connect = sqlite3.connect("database/saving_frames.db")

    def btnLoadClicked(self):
        filename, _ = QFileDialog.getOpenFileUrl(self, filter="Видео (*.mp4)")
        if filename != QtCore.QUrl(''):
            video_obj = video.Video(filename.toString()[8:], self.detection, self.focus_direction.value())
            self.player_window = PlayerWindow(video_obj, self.connect, self)

    def btnSavingVideoClicked(self):
        self.saving_base_window = SavingVideoWindow(self.connect)

    def closeEvent(self, event):
        self.connect.close()
        if hasattr(self, 'player_window'):
            self.player_window.closePlayer()


class Player(QtCore.QObject):
    frameProcessed = QtCore.pyqtSignal(object)
    is_worked = True
    is_play = True

    def __init__(self, video_obj):
        super().__init__()
        self.video_obj = video_obj

    def stop(self):
        self.is_worked = False

    def pause(self):
        self.is_play = False

    def play(self):
        self.is_play = True

    def getPlayState(self):
        return self.is_play

    def run(self):
        while self.is_worked:
            if self.is_play:
                ret, frame = self.video_obj.getFrame()
                if ret:
                    self.frameProcessed.emit(frame)
                else:
                    break


class PlayerWindow(QWidget, Ui_PlayerWindow):
    def __init__(self, video_obj, connection_db, parent=None):
        super(PlayerWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.connection_db = connection_db
        self.cursor = self.connection_db.cursor()
        self.thread = QtCore.QThread()
        self.player_thread = Player(video_obj)
        self.player_thread.moveToThread(self.thread)
        self.player_thread.frameProcessed.connect(self.frameProcessed)
        self.thread.started.connect(self.player_thread.run)
        self.thread.start()

        self.image = None

        self.button_load = self.findChild(QPushButton, 'btnBack')
        self.button_load.clicked.connect(lambda: self.btnBackClicked())

        self.button_load = self.findChild(QPushButton, 'btnPause')
        self.button_load.clicked.connect(lambda: self.btnPauseClicked())

        self.button_load = self.findChild(QPushButton, 'btnContinue')
        self.button_load.clicked.connect(lambda: self.btnPlayClicked())

        self.button_load = self.findChild(QPushButton, 'btnSave')
        self.button_load.clicked.connect(lambda: self.btnSaveClicked())

    def btnPlayClicked(self):
        if not self.player_thread.getPlayState():
            self.player_thread.play()

    def btnPauseClicked(self):
        if self.player_thread.getPlayState():
            self.player_thread.pause()

    def btnBackClicked(self):
        self.closePlayer()
        self.close()

    def btnSaveClicked(self):
        if self.image is None:
            return
        self.btnPauseClicked()
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        self.image.save(buffer, "PNG")
        byte_image_io = io.BytesIO()
        byte_image_io.write(buffer.data())
        buffer.close()
        byte_image_io.seek(0)
        code_image = byte_image_io.read().hex()
        data = code_image.strip()
        data = data.replace(' ', '')
        data = data.replace('\n', '')
        data = binascii.a2b_hex(data)
        que = "INSERT INTO saving_frames\nVALUES (NULL, ?)"
        self.cursor.execute(que, (data,))
        self.connection_db.commit()
        self.btnPlayClicked()

    def closePlayer(self):
        self.player_thread.stop()
        self.thread.exit()
        self.thread.wait()

    @QtCore.pyqtSlot(object)
    def frameProcessed(self, frame):
        label = self.findChild(QLabel, "videoPlayer")
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        self.image = QImage(frame.data, width, height, bytesPerLine, QImage.Format_BGR888)
        label.setPixmap(QPixmap(self.image))


class SavingVideoWindow(QWidget, Ui_SavingVideo):
    def __init__(self, connection_db, parent=None):
        super(SavingVideoWindow, self).__init__(parent)
        self.setupUi(self)
        self.show()

        cursor = connection_db.cursor()
        result = cursor.execute("SELECT frame FROM saving_frames").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if j == 0:
                    self.tableWidget.setCellWidget(i, j, self.getImageValue(val))
        self.tableWidget.verticalHeader().setDefaultSectionSize(300)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(600)

        self.button_load = self.findChild(QPushButton, 'btnBack')
        self.button_load.clicked.connect(lambda: self.btnBackClicked())

    def getImageValue(self, value):
        image = QLabel(self.verticalFrame)
        image.setText("")
        image.setScaledContents(True)
        pixmap = QPixmap()
        pixmap.loadFromData(value, 'png')
        image.setPixmap(pixmap)
        return image

    def btnBackClicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
