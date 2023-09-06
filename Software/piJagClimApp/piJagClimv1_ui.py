# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piJagClimv1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from utils import SimpleDial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
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
        self.tempValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempValueLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.tempValueLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempValueLabel.setObjectName("tempValueLabel")
        self.verticalLayoutTemp.addWidget(self.tempValueLabel)
        self.tempDial = SimpleDial(self.centralwidget)
        self.tempDial.setMinimum(0)
        self.tempDial.setMaximum(30)
        self.tempDial.setSingleStep(1)
        self.tempDial.setObjectName("tempDial")
        self.verticalLayoutTemp.addWidget(self.tempDial)
        self.tempACButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempACButton.setObjectName("tempACButton")
        self.verticalLayoutTemp.addWidget(self.tempACButton)
        self.tempPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempPlusButton.setObjectName("tempPlusButton")
        self.verticalLayoutTemp.addWidget(self.tempPlusButton)
        self.tempAutoButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempAutoButton.setObjectName("tempAutoButton")
        self.verticalLayoutTemp.addWidget(self.tempAutoButton)
        self.tempMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.tempMinusButton.setObjectName("tempMinusButton")
        self.verticalLayoutTemp.addWidget(self.tempMinusButton)
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
        self.airFeetButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFeetButton.setObjectName("airFeetButton")
        self.verticalLayoutControls.addWidget(self.airFeetButton)
        self.airFaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFaceButton.setObjectName("airFaceButton")
        self.verticalLayoutControls.addWidget(self.airFaceButton)
        self.airFeetFaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFeetFaceButton.setObjectName("airFeetFaceButton")
        self.verticalLayoutControls.addWidget(self.airFeetFaceButton)
        self.airFrontDefrostButton = QtWidgets.QPushButton(self.centralwidget)
        self.airFrontDefrostButton.setObjectName("airFrontDefrostButton")
        self.verticalLayoutControls.addWidget(self.airFrontDefrostButton)
        self.airRearDefrostButton = QtWidgets.QPushButton(self.centralwidget)
        self.airRearDefrostButton.setObjectName("airRearDefrostButton")
        self.verticalLayoutControls.addWidget(self.airRearDefrostButton)
        self.airRecyclingButton = QtWidgets.QPushButton(self.centralwidget)
        self.airRecyclingButton.setObjectName("airRecyclingButton")
        self.verticalLayoutControls.addWidget(self.airRecyclingButton)
        self.horizontalLayout.addLayout(self.verticalLayoutControls)
        self.verticalLayoutFan = QtWidgets.QVBoxLayout()
        self.verticalLayoutFan.setObjectName("verticalLayoutFan")
        self.fanLabel = QtWidgets.QLabel(self.centralwidget)
        self.fanLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.fanLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fanLabel.setObjectName("fanLabel")
        self.verticalLayoutFan.addWidget(self.fanLabel)
        self.fanValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.fanValueLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.fanValueLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fanValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fanValueLabel.setObjectName("fanValueLabel")
        self.verticalLayoutFan.addWidget(self.fanValueLabel)
        self.fanDial = QtWidgets.QDial(self.centralwidget)
        self.fanDial.setMinimum(1)
        self.fanDial.setMaximum(11)
        self.fanDial.setObjectName("fanDial")
        self.verticalLayoutFan.addWidget(self.fanDial)
        self.fanPlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanPlusButton.setObjectName("fanPlusButton")
        self.verticalLayoutFan.addWidget(self.fanPlusButton)
        self.fanAutoButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanAutoButton.setObjectName("fanAutoButton")
        self.verticalLayoutFan.addWidget(self.fanAutoButton)
        self.fanMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.fanMinusButton.setObjectName("fanMinusButton")
        self.verticalLayoutFan.addWidget(self.fanMinusButton)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tempLabel.setText(_translate("MainWindow", "Temperature"))
        self.tempValueLabel.setText(_translate("MainWindow", "?°C"))
        self.tempACButton.setText(_translate("MainWindow", "A/C"))
        self.tempPlusButton.setText(_translate("MainWindow", "+"))
        self.tempAutoButton.setText(_translate("MainWindow", "Auto"))
        self.tempMinusButton.setText(_translate("MainWindow", "-"))
        self.airLabel.setText(_translate("MainWindow", "Controls"))
        self.airValueLabel.setText(_translate("MainWindow", "?"))
        self.airFeetButton.setText(_translate("MainWindow", "Feet"))
        self.airFaceButton.setText(_translate("MainWindow", "Face"))
        self.airFeetFaceButton.setText(_translate("MainWindow", "Feet n Face"))
        self.airFrontDefrostButton.setText(_translate("MainWindow", "Front Defrost"))
        self.airRearDefrostButton.setText(_translate("MainWindow", "Rear Defrost"))
        self.airRecyclingButton.setText(_translate("MainWindow", "Recycling"))
        self.fanLabel.setText(_translate("MainWindow", "Fan"))
        self.fanValueLabel.setText(_translate("MainWindow", "?"))
        self.fanPlusButton.setText(_translate("MainWindow", "+"))
        self.fanAutoButton.setText(_translate("MainWindow", "Auto"))
        self.fanMinusButton.setText(_translate("MainWindow", "-"))
