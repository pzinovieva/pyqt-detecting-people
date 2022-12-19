from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SavingVideo(object):
    def setupUi(self, centralwidjet):
        centralwidjet.setObjectName("centralwidjet")
        centralwidjet.resize(805, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(centralwidjet.sizePolicy().hasHeightForWidth())
        centralwidjet.setSizePolicy(sizePolicy)
        centralwidjet.setMinimumSize(QtCore.QSize(805, 425))
        centralwidjet.setMaximumSize(QtCore.QSize(805, 425))
        centralwidjet.setSizeIncrement(QtCore.QSize(0, 0))
        centralwidjet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(centralwidjet)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalFrame = QtWidgets.QFrame(centralwidjet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(790, 380))
        self.verticalFrame.setMaximumSize(QtCore.QSize(790, 380))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.btnBack = QtWidgets.QPushButton(self.verticalFrame)
        self.btnBack.setStyleSheet("font-size:10pt; \n"
                                   "font-weight:600; \n"
                                   "color:#4d4d4d;\n"
                                   "background-color: rgb(231, 247, 255);")
        self.btnBack.setObjectName("btnBack")
        self.verticalLayout.addWidget(self.btnBack)
        self.verticalLayout_2.addWidget(self.verticalFrame)

        self.retranslateUi(centralwidjet)
        QtCore.QMetaObject.connectSlotsByName(centralwidjet)

    def retranslateUi(self, centralwidjet):
        _translate = QtCore.QCoreApplication.translate
        centralwidjet.setWindowTitle(_translate("centralwidjet", "Detection"))
        self.btnBack.setText(_translate("centralwidjet", "Ок"))
