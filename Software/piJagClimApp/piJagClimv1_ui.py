# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piJagClimv1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 20, 671, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tempLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.tempLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.tempLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.verticalLayout_4.addWidget(self.tempLabel)
        self.tempValueLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.tempValueLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.tempValueLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tempValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempValueLabel.setObjectName("tempValueLabel")
        self.verticalLayout_4.addWidget(self.tempValueLabel)
        self.tempACButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.tempACButton.setObjectName("tempACButton")
        self.verticalLayout_4.addWidget(self.tempACButton)
        self.tempPlusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.tempPlusButton.setObjectName("tempPlusButton")
        self.verticalLayout_4.addWidget(self.tempPlusButton)
        self.tempAutoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.tempAutoButton.setObjectName("tempAutoButton")
        self.verticalLayout_4.addWidget(self.tempAutoButton)
        self.tempMinusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.tempMinusButton.setObjectName("tempMinusButton")
        self.verticalLayout_4.addWidget(self.tempMinusButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fanLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fanLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.fanLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fanLabel.setObjectName("fanLabel")
        self.verticalLayout_5.addWidget(self.fanLabel)
        self.fanValueLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fanValueLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.fanValueLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fanValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fanValueLabel.setObjectName("fanValueLabel")
        self.verticalLayout_5.addWidget(self.fanValueLabel)
        self.fanPlusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fanPlusButton.setObjectName("fanPlusButton")
        self.verticalLayout_5.addWidget(self.fanPlusButton)
        self.fanAutoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fanAutoButton.setObjectName("fanAutoButton")
        self.verticalLayout_5.addWidget(self.fanAutoButton)
        self.fanMinusButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fanMinusButton.setObjectName("fanMinusButton")
        self.verticalLayout_5.addWidget(self.fanMinusButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.airLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.airLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.airLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.airLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.airLabel.setObjectName("airLabel")
        self.verticalLayout_7.addWidget(self.airLabel)
        self.airValueLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.airValueLabel.setMaximumSize(QtCore.QSize(100000, 50))
        self.airValueLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.airValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.airValueLabel.setObjectName("airValueLabel")
        self.verticalLayout_7.addWidget(self.airValueLabel)
        self.airFeetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.airFeetButton.setObjectName("airFeetButton")
        self.verticalLayout_7.addWidget(self.airFeetButton)
        self.airFaceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.airFaceButton.setObjectName("airFaceButton")
        self.verticalLayout_7.addWidget(self.airFaceButton)
        self.airFeetFaceButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.airFeetFaceButton.setObjectName("airFeetFaceButton")
        self.verticalLayout_7.addWidget(self.airFeetFaceButton)
        self.airFrontDefrostButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.airFrontDefrostButton.setObjectName("airFrontDefrostButton")
        self.verticalLayout_7.addWidget(self.airFrontDefrostButton)
        self.airRearDefrostButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.airRearDefrostButton.setObjectName("airRearDefrostButton")
        self.verticalLayout_7.addWidget(self.airRearDefrostButton)
        self.airRecyclingButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.airRecyclingButton.setObjectName("airRecyclingButton")
        self.verticalLayout_7.addWidget(self.airRecyclingButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
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
        self.fanLabel.setText(_translate("MainWindow", "Fan"))
        self.fanValueLabel.setText(_translate("MainWindow", "?"))
        self.fanPlusButton.setText(_translate("MainWindow", "+"))
        self.fanAutoButton.setText(_translate("MainWindow", "Auto"))
        self.fanMinusButton.setText(_translate("MainWindow", "-"))
        self.airLabel.setText(_translate("MainWindow", "Controls"))
        self.airValueLabel.setText(_translate("MainWindow", "?"))
        self.airFeetButton.setText(_translate("MainWindow", "Feet"))
        self.airFaceButton.setText(_translate("MainWindow", "Face"))
        self.airFeetFaceButton.setText(_translate("MainWindow", "Feet n Face"))
        self.airFrontDefrostButton.setText(_translate("MainWindow", "Front Defrost"))
        self.airRearDefrostButton.setText(_translate("MainWindow", "Rear Defrost"))
        self.airRecyclingButton.setText(_translate("MainWindow", "Recycling"))