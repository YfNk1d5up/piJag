# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piJagClimv1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from utils.customDial import SimpleDial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutTemp = QtWidgets.QVBoxLayout()
        self.verticalLayoutTemp.setObjectName("verticalLayoutTemp")
        self.tempLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.tempLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.verticalLayoutTemp.addWidget(self.tempLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutTemp.addItem(spacerItem)
        self.tempDial = SimpleDial(self.centralwidget, 'temp')
        self.tempDial.setMinimumSize(QtCore.QSize(0, 250))
        self.tempDial.setMinimum(0)
        self.tempDial.setMaximum(30)
        self.tempDial.setSingleStep(1)
        self.tempDial.setObjectName("tempDial")
        self.verticalLayoutTemp.addWidget(self.tempDial)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tempMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempMinusButton.setObjectName("tempMinusButton")
        self.horizontalLayout_5.addWidget(self.tempMinusButton)
        self.tempAutoButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempAutoButton.setObjectName("tempAutoButton")
        self.horizontalLayout_5.addWidget(self.tempAutoButton)
        self.tempPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempPlusButton.setObjectName("tempPlusButton")
        self.horizontalLayout_5.addWidget(self.tempPlusButton)
        self.verticalLayoutTemp.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutTemp.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayoutTemp)
        self.verticalLayoutControls = QtWidgets.QVBoxLayout()
        self.verticalLayoutControls.setObjectName("verticalLayoutControls")
        self.airLabel = QtWidgets.QLabel(self.centralwidget)
        self.airLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.airLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.airLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.airLabel.setObjectName("airLabel")
        self.verticalLayoutControls.addWidget(self.airLabel)
        self.airValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.airValueLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.airValueLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.airValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.airValueLabel.setObjectName("airValueLabel")
        self.verticalLayoutControls.addWidget(self.airValueLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutControls.addItem(spacerItem2)
        self.tempACButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempACButton.setMinimumSize(QtCore.QSize(0, 40))
        self.tempACButton.setObjectName("tempACButton")
        self.verticalLayoutControls.addWidget(self.tempACButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.airFaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFaceButton.setMinimumSize(QtCore.QSize(0, 40))
        self.airFaceButton.setObjectName("airFaceButton")
        self.horizontalLayout_2.addWidget(self.airFaceButton)
        self.airFeetFaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFeetFaceButton.setMinimumSize(QtCore.QSize(0, 40))
        self.airFeetFaceButton.setObjectName("airFeetFaceButton")
        self.horizontalLayout_2.addWidget(self.airFeetFaceButton)
        self.airFeetButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFeetButton.setMinimumSize(QtCore.QSize(0, 40))
        self.airFeetButton.setObjectName("airFeetButton")
        self.horizontalLayout_2.addWidget(self.airFeetButton)
        self.verticalLayoutControls.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.airFrontDefrostButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFrontDefrostButton.setMinimumSize(QtCore.QSize(0, 40))
        self.airFrontDefrostButton.setObjectName("airFrontDefrostButton")
        self.horizontalLayout_3.addWidget(self.airFrontDefrostButton)
        self.airRearDefrostButton = QtWidgets.QPushButton(self.centralwidget)
        self.airRearDefrostButton.setMinimumSize(QtCore.QSize(0, 40))
        self.airRearDefrostButton.setObjectName("airRearDefrostButton")
        self.horizontalLayout_3.addWidget(self.airRearDefrostButton)
        self.airRecyclingButton = QtWidgets.QPushButton(self.centralwidget)
        self.airRecyclingButton.setMinimumSize(QtCore.QSize(0, 40))
        self.airRecyclingButton.setObjectName("airRecyclingButton")
        self.horizontalLayout_3.addWidget(self.airRecyclingButton)
        self.verticalLayoutControls.addLayout(self.horizontalLayout_3)
        self.onoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.onoffButton.setMinimumSize(QtCore.QSize(0, 40))
        self.onoffButton.setObjectName("onoffButton")
        self.verticalLayoutControls.addWidget(self.onoffButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutControls.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayoutControls)
        self.verticalLayoutFan = QtWidgets.QVBoxLayout()
        self.verticalLayoutFan.setObjectName("verticalLayoutFan")
        self.fanLabel = QtWidgets.QLabel(self.centralwidget)
        self.fanLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.fanLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fanLabel.setObjectName("fanLabel")
        self.verticalLayoutFan.addWidget(self.fanLabel)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutFan.addItem(spacerItem4)
        self.fanDial = SimpleDial(self.centralwidget, 'fan')
        self.fanDial.setMinimumSize(QtCore.QSize(0, 250))
        self.fanDial.setMinimum(1)
        self.fanDial.setMaximum(11)
        self.fanDial.setObjectName("fanDial")
        self.verticalLayoutFan.addWidget(self.fanDial)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fanMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanMinusButton.setObjectName("fanMinusButton")
        self.horizontalLayout_6.addWidget(self.fanMinusButton)
        self.fanAutoButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanAutoButton.setObjectName("fanAutoButton")
        self.horizontalLayout_6.addWidget(self.fanAutoButton)
        self.fanPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanPlusButton.setObjectName("fanPlusButton")
        self.horizontalLayout_6.addWidget(self.fanPlusButton)
        self.verticalLayoutFan.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutFan.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayoutFan)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "piJagClimv0.1"))
        self.tempLabel.setText(_translate("MainWindow", "Temperature"))
        self.tempMinusButton.setText(_translate("MainWindow", "-"))
        self.tempAutoButton.setText(_translate("MainWindow", "Auto"))
        self.tempPlusButton.setText(_translate("MainWindow", "+"))
        self.airLabel.setText(_translate("MainWindow", "Controls"))
        self.airValueLabel.setText(_translate("MainWindow", "?"))
        self.tempACButton.setText(_translate("MainWindow", "A/C"))
        # self.airFaceButton.setText(_translate("MainWindow", "Face"))
        self.airFaceButton.setIcon(QtGui.QIcon('pictures/face.png'))
        # self.airFeetFaceButton.setText(_translate("MainWindow", "Feet n Face"))
        self.airFeetFaceButton.setIcon(QtGui.QIcon('pictures/feet_face.png'))
        self.airFeetFaceButton.setAutoFillBackground(True)
        # self.airFeetButton.setText(_translate("MainWindow", "Feet"))
        self.airFeetButton.setIcon(QtGui.QIcon('pictures/feet.png'))
        self.airFeetButton.setAutoFillBackground(True)
        # self.airFrontDefrostButton.setText(_translate("MainWindow", "Front Defrost"))
        self.airFrontDefrostButton.setIcon(QtGui.QIcon('pictures/front.png'))
        self.airFrontDefrostButton.setAutoFillBackground(True)
        # self.airRearDefrostButton.setText(_translate("MainWindow", "Rear Defrost"))
        self.airRearDefrostButton.setIcon(QtGui.QIcon('pictures/rear.png'))
        self.airRearDefrostButton.setAutoFillBackground(True)
        # self.airRecyclingButton.setText(_translate("MainWindow", "Recycling"))
        self.airRecyclingButton.setIcon(QtGui.QIcon('pictures/recycle.png'))
        self.airRecyclingButton.setAutoFillBackground(True)
        self.onoffButton.setText(_translate("MainWindow", "On"))
        self.fanLabel.setText(_translate("MainWindow", "Fan"))
        self.fanMinusButton.setText(_translate("MainWindow", "-"))
        self.fanAutoButton.setText(_translate("MainWindow", "Auto"))
        self.fanPlusButton.setText(_translate("MainWindow", "+"))
