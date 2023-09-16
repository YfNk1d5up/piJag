# -*- coding: utf-8 -*-
import os

# Form implementation generated from reading ui file 'piJagClimv1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from utils.customQtWidgets import SimpleDial, RoundButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, dir_folder):
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
        spacerItem = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutTemp.addItem(spacerItem)
        self.tempDial = SimpleDial(self.centralwidget, 'temp')
        self.tempDial.setMinimumSize(QtCore.QSize(400, 400))
        self.tempDial.setMinimum(0)
        self.tempDial.setMaximum(30)
        self.tempDial.setSingleStep(1)
        self.tempDial.setObjectName("tempDial")
        self.verticalLayoutTemp.addWidget(self.tempDial)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem01 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem01)
        self.tempMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempMinusButton.setObjectName("tempMinusButton")
        self.tempMinusButton.setMinimumSize(QtCore.QSize(80, 40))
        self.tempMinusButton.setStyleSheet("border:none;")
        self.horizontalLayout_5.addWidget(self.tempMinusButton)
        self.tempACButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/AC.png'))
        self.tempACButton.setMinimumSize(QtCore.QSize(60, 60))
        self.tempACButton.setAutoFillBackground(True)
        self.tempACButton.setText("")
        self.tempACButton.setObjectName("tempACButton")
        self.horizontalLayout_5.addWidget(self.tempACButton)
        self.tempPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempPlusButton.setObjectName("tempPlusButton")
        self.tempPlusButton.setMinimumSize(QtCore.QSize(80, 40))
        self.tempPlusButton.setStyleSheet("border:none;")
        self.horizontalLayout_5.addWidget(self.tempPlusButton)
        spacerItem02 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem02)
        self.verticalLayoutTemp.addLayout(self.horizontalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutTemp.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayoutTemp)
        self.verticalLayoutControls = QtWidgets.QVBoxLayout()
        self.verticalLayoutControls.setObjectName("verticalLayoutControls")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutControls.addItem(spacerItem2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.verticalLayoutControls.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.airFaceButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/face.png'))
        self.airFaceButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airFaceButton.setAutoFillBackground(True)
        self.airFaceButton.setText("")
        self.airFaceButton.setObjectName("airFaceButton")
        self.horizontalLayout_2.addWidget(self.airFaceButton)
        self.airFeetButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/feet.png'))
        self.airFeetButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airFeetButton.setAutoFillBackground(True)
        self.airFeetButton.setText("")
        self.airFeetButton.setObjectName("airFeetButton")
        self.horizontalLayout_2.addWidget(self.airFeetButton)
        self.airFeetFaceButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/feet_face.png'))
        self.airFeetFaceButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airFeetFaceButton.setAutoFillBackground(True)
        self.airFeetFaceButton.setText("")
        self.airFeetFaceButton.setObjectName("airFeetFaceButton")
        self.horizontalLayout_2.addWidget(self.airFeetFaceButton)
        self.airFeetFrontDefrostButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/feetfront.png'))
        self.airFeetFrontDefrostButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airFeetFrontDefrostButton.setAutoFillBackground(True)
        self.airFeetFrontDefrostButton.setText("")
        self.airFeetFrontDefrostButton.setObjectName("airFeetFrontDefrostButton")
        self.horizontalLayout_2.addWidget(self.airFeetFrontDefrostButton)
        self.verticalLayoutControls.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.airFrontDefrostButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/front.png'), icon_ratio=0.4)
        self.airFrontDefrostButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airFrontDefrostButton.setAutoFillBackground(True)
        self.airFrontDefrostButton.setText("")
        self.airFrontDefrostButton.setObjectName("airFrontDefrostButton")
        self.horizontalLayout_3.addWidget(self.airFrontDefrostButton)
        self.airRearDefrostButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/rear.png'), icon_ratio=0.4)
        self.airRearDefrostButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airRearDefrostButton.setAutoFillBackground(True)
        self.airRearDefrostButton.setText("")
        self.airRearDefrostButton.setObjectName("airRearDefrostButton")
        self.horizontalLayout_3.addWidget(self.airRearDefrostButton)
        self.airRecyclingButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/recycle.png'))
        self.airRecyclingButton.setMinimumSize(QtCore.QSize(60, 60))
        self.airRecyclingButton.setAutoFillBackground(True)
        self.airRecyclingButton.setText("")
        self.airRecyclingButton.setObjectName("airRecyclingButton")
        self.horizontalLayout_3.addWidget(self.airRecyclingButton)
        self.verticalLayoutControls.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.onoffButton = RoundButton(self.centralwidget, icon=os.path.join(dir_folder,'pictures/power.png'), fill=True)
        self.onoffButton.setMinimumSize(QtCore.QSize(60, 60))
        self.onoffButton.setAutoFillBackground(True)
        self.onoffButton.setText("")
        self.onoffButton.setObjectName("onoffButton")
        self.horizontalLayout_8.addWidget(self.onoffButton)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayoutControls.addLayout(self.horizontalLayout_8)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutControls.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayoutControls)
        self.verticalLayoutFan = QtWidgets.QVBoxLayout()
        self.verticalLayoutFan.setObjectName("verticalLayoutFan")
        spacerItem8 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutFan.addItem(spacerItem8)
        self.fanDial = SimpleDial(self.centralwidget, 'fan')
        self.fanDial.setMinimumSize(QtCore.QSize(400, 400))
        self.fanDial.setMinimum(1)
        self.fanDial.setMaximum(11)
        self.fanDial.setObjectName("fanDial")
        self.verticalLayoutFan.addWidget(self.fanDial)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.fanMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanMinusButton.setObjectName("fanMinusButton")
        self.fanMinusButton.setMinimumSize(QtCore.QSize(60, 40))
        self.fanMinusButton.setStyleSheet("border:none;")
        self.horizontalLayout_6.addWidget(self.fanMinusButton)
        self.fanAutoButton = RoundButton(self.centralwidget, icon = os.path.join(dir_folder,'pictures/auto.png'))
        self.fanAutoButton.setObjectName("fanAutoButton")
        self.fanAutoButton.setMinimumSize(QtCore.QSize(60, 60))
        self.fanAutoButton.setStyleSheet("border:none;")
        self.fanAutoButton.setAutoFillBackground(True)
        self.fanAutoButton.setText("")
        self.horizontalLayout_6.addWidget(self.fanAutoButton)
        self.fanPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanPlusButton.setObjectName("fanPlusButton")
        self.fanPlusButton.setMinimumSize(QtCore.QSize(60, 40))
        self.fanPlusButton.setStyleSheet("border:none;")
        self.horizontalLayout_6.addWidget(self.fanPlusButton)
        spacerItem10 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayoutFan.addLayout(self.horizontalLayout_6)
        spacerItem11 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutFan.addItem(spacerItem11)
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
        self.tempMinusButton.setText(_translate("MainWindow", "-"))
        self.tempPlusButton.setText(_translate("MainWindow", "+"))
        self.fanMinusButton.setText(_translate("MainWindow", "-"))
        self.fanPlusButton.setText(_translate("MainWindow", "+"))

        self.onoffButton.setStyleSheet("border-radius:50%;")


