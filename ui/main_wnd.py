from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Detection(object):
    def setupUi(self, Detection):
        Detection.setObjectName("Detection")
        Detection.resize(805, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Detection.sizePolicy().hasHeightForWidth())
        Detection.setSizePolicy(sizePolicy)
        Detection.setMinimumSize(QtCore.QSize(805, 425))
        Detection.setMaximumSize(QtCore.QSize(805, 425))
        Detection.setSizeIncrement(QtCore.QSize(0, 0))
        Detection.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Detection)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header = QtWidgets.QLabel(Detection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QtCore.QSize(779, 180))
        self.header.setMaximumSize(QtCore.QSize(779, 180))
        self.header.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.header.setObjectName("header")
        self.verticalLayout_2.addWidget(self.header)
        self.verticalFrame = QtWidgets.QFrame(Detection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(790, 180))
        self.verticalFrame.setMaximumSize(QtCore.QSize(790, 180))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_2.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_2.setSizePolicy(sizePolicy)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(762, 60))
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(762, 60))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalFrame = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.focusText = QtWidgets.QLabel(self.horizontalFrame_2)
        self.focusText.setObjectName("focusText")
        self.horizontalFrame.addWidget(self.focusText)
        self.numberFocus = QtWidgets.QDoubleSpinBox(self.horizontalFrame_2)
        self.numberFocus.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font-size:10pt; \n"
                                       "\n"
                                       "color:#4d4d4d;")
        self.numberFocus.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.numberFocus.setProperty("value", 18.0)
        self.numberFocus.setObjectName("numberFocus")
        self.horizontalFrame.addWidget(self.numberFocus)
        self.verticalLayout.addWidget(self.horizontalFrame_2)
        self.btnLoadVideo = QtWidgets.QPushButton(self.verticalFrame)
        self.btnLoadVideo.setStyleSheet("font-size:10pt; \n"
                                        "font-weight:600; \n"
                                        "color:#4d4d4d;\n"
                                        "background-color: rgb(231, 247, 255);")
        self.btnLoadVideo.setObjectName("btnLoadVideo")
        self.verticalLayout.addWidget(self.btnLoadVideo)
        self.btnLoadSavingVideo = QtWidgets.QPushButton(self.verticalFrame)
        self.btnLoadSavingVideo.setStyleSheet("font-size:10pt; \n"
                                              "font-weight:600; \n"
                                              "color:#4d4d4d;\n"
                                              "background-color: rgb(231, 247, 255);")
        self.btnLoadSavingVideo.setObjectName("btnLoadSavingVideo")
        self.verticalLayout.addWidget(self.btnLoadSavingVideo)
        self.verticalLayout_2.addWidget(self.verticalFrame)

        self.retranslateUi(Detection)
        QtCore.QMetaObject.connectSlotsByName(Detection)

    def retranslateUi(self, Detection):
        _translate = QtCore.QCoreApplication.translate
        Detection.setWindowTitle(_translate("Detection", "Detection"))
        self.header.setText(_translate("Detection",
                                       "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#4f4f4f;\">ОПРЕДЕЛЕНИЕ РАССТОЯНИЯ МЕЖДУ ЛЮДЬМИ НА ВИДЕО</span></p></body></html>"))
        self.focusText.setText(_translate("Detection",
                                          "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#4d4d4d;\">Фокусное расстояние камеры</span></p></body></html>"))
        self.btnLoadVideo.setText(_translate("Detection", "Загрузить видео и посмотреть результат"))
        self.btnLoadSavingVideo.setText(_translate("Detection", "Посмотреть сохраненные кадры"))
