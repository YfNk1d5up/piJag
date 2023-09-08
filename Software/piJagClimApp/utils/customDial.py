
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.utils import tempDial2temp
class SimpleDisk(QtWidgets.QWidget):
    def __init__(self, parent, color={'r': 255, 'g': 255, 'b': 255, 'a': 127}):
        super(SimpleDisk, self).__init__(parent)
        self.color = color

    def paintEvent(self, event=None):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        dynPenColor = QtGui.QColor(self.color['r'],
                                   self.color['g'],
                                   self.color['b'],
                                   self.color['a']
                                   )
        painter.setBrush(QtGui.QBrush(dynPenColor))
        painter.setPen(QtGui.QColor(0,0,0,0))
        rect = QtCore.QRect(0,0,self.width(),self.height())

        painter.drawRoundedRect(rect, self.width(), self.height())

    def updateColor(self, _color):
        self.color = _color
        self.update()

class SimpleDial(QtWidgets.QDial):

    def __init__(self, parent, mode=None):
        super(SimpleDial, self).__init__(parent)
        self.color = {'r': 255, 'g': 0, 'b': 0, 'a': 127}
        self.mode = mode
        self._val = ''

        self.child = SimpleDisk(self)
        self.child.resize(60, 60)
        self.child.setVisible(False)
        self._cursorPoint = QtCore.QPoint()
        self.center = QtCore.QPoint()

        # Animation
        effect1 = QtWidgets.QGraphicsOpacityEffect(self.child)
        effect1.setOpacity(1)
        self.child.setGraphicsEffect(effect1)

        self.anim = QtCore.QPropertyAnimation(self.child, b"size")
        self.anim.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim.setStartValue(QtCore.QSize(10, 10))
        self.anim.setEndValue(QtCore.QSize(0, 0))
        self.anim.setDuration(1000)


        self.anim0 = QtCore.QPropertyAnimation(effect1, b"opacity")
        self.anim0.setStartValue(0)
        self.anim0.setEndValue(0.9)
        self.anim0.setDuration(200)


        self.anim1 = QtCore.QPropertyAnimation(self.child, b"pos")
        self.anim1.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim1.setDuration(1000)

        self.anim2 = QtCore.QPropertyAnimation(self.child, b"size")
        self.anim2.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.anim2.setStartValue(QtCore.QSize(12, 12))
        self.anim2.setEndValue(QtCore.QSize(60, 60))
        self.anim2.setDuration(1000)


        self.anim3 = QtCore.QPropertyAnimation(effect1, b"opacity")
        self.anim3.setStartValue(0.7)
        self.anim3.setEndValue(0)
        self.anim3.setDuration(200)

        self.anim_sub_group = QtCore.QParallelAnimationGroup()
        self.anim_sub_group.addAnimation(self.anim1)
        self.anim_sub_group.addAnimation(self.anim2)

        self._onAnim = False

    def paintEvent(self, event=None):
        # create a QStyleOption for the dial, and initialize it with the basic properties
        # that will be used for the configuration of the painter
        opt = QtWidgets.QStyleOptionSlider()
        self.initStyleOption(opt)

        # construct a QRectF that uses the minimum between width and height,
        # and adds some margins for better visual separation
        # this is partially taken from the fusion style helper source
        width = opt.rect.width()
        height = opt.rect.height()
        self.center = QtCore.QPoint(int((width-self.child.width())/2), int((height-self.child.height())/2))
        # Temp line
        r = min(width, height) / 2
        r -= r / 50
        d_ = r / 6
        dx = opt.rect.x() + d_ + (width - 2 * r) / 2 + 1
        dy = opt.rect.y() + d_ + (height - 2 * r) / 2 + 1
        br = QtCore.QRectF(dx + .5, dy + .5,
            int(r * 2 - 2 * d_ - 2),
            int(r * 2 - 2 * d_ - 2))

        # In line
        r_in = min(width, height) / 10
        r_in -= r_in / 50
        d_in = r_in / 6
        dx_in = opt.rect.x() + d_in + (width - 2 * r_in) / 2 + 1
        dy_in = opt.rect.y() + d_in + (height - 2 * r_in) / 2 + 1
        br_in = QtCore.QRectF(dx_in + .5, dy_in + .5,
                           int(r_in * 2 - 2 * d_in - 2),
                           int(r_in * 2 - 2 * d_in - 2))

        # Out line
        r_out = min(width, height) / 3
        r_out -= r_out / 50
        d_out = r_out / 6
        dx_out = opt.rect.x() + d_out + (width - 2 * r_out) / 2 + 1
        dy_out = opt.rect.y() + d_out + (height - 2 * r_out) / 2 + 1
        br_out = QtCore.QRectF(dx_out + .5, dy_out + .5,
                           int(r_out * 2 - 2 * d_out - 2),
                           int(r_out * 2 - 2 * d_out - 2))

        # Countain line
        r_countain = min(width, height) / 2.5
        r_countain -= r_countain / 50
        d_countain = r_countain / 6
        dx_countain = opt.rect.x() + d_countain + (width - 2 * r_countain) / 2 + 1
        dy_countain = opt.rect.y() + d_countain + (height - 2 * r_countain) / 2 + 1
        br_countain = QtCore.QRectF(dx_countain + .5, dy_countain + .5,
                               int(r_countain * 2 - 2 * d_countain - 2),
                               int(r_countain * 2 - 2 * d_countain - 2))

        qp = QtGui.QPainter(self)

        # find the "real" value ratio between minimum and maximum
        realValue = (self.value() - self.minimum()) / (self.maximum() - self.minimum())
        # compute the angle at which the dial handle should be placed, assuming
        # a range between 240° and 300° (moving clockwise)
        angle = 240 - 300 * realValue
        # create a polar line for the position of the handle; this can also
        # be done using the math module with some performance improvement
        line = QtCore.QLineF.fromPolar(r * .4, angle)
        line.translate(br.center())
        ds = r / 20
        # create the handle rect and position it at the end of the polar line
        handleRect = QtCore.QRectF(0, 0, ds, ds)
        handleRect.moveCenter(line.p2())

        self._cursorPoint = handleRect.center().toPoint()

        line_opposite = QtCore.QLineF.fromPolar(- r * .6, angle)
        line_opposite.translate(br.center())
        ds = r / 5
        # create the handle rect and position it at the end of the polar line
        handleRect_opposite = QtCore.QRectF(0, 0, ds, ds)
        handleRect_opposite.moveCenter(line_opposite.p2())

        dynPenColor = QtGui.QColor(self.color['r'],
                                self.color['g'],
                                self.color['b'],
                                self.color['a']
                                )

        dynPen = QtGui.QPen(dynPenColor, 12)
        dynPen.setCapStyle(QtCore.Qt.RoundCap)

        greyPenColor = QtGui.QColor(127,
                                127,
                                127,
                                127
                                )
        greyPen = QtGui.QPen(greyPenColor, 2)

        whitePenColor = QtGui.QColor(255,
                                     255,
                                     255,
                                     255
                                     )
        whitePen = QtGui.QPen(whitePenColor, 1)

        if self.mode == 'temp':
            gradColor0 = QtGui.QColor(255, 0, 0, 180)
            gradColor1 = QtGui.QColor(0, 0, 255, 180)
        elif self.mode == 'fan':
            gradColor0 = QtGui.QColor(220, 220, 220, 180)
            gradColor1 = QtGui.QColor(0, 0, 0, 180)
        else:
            gradColor0 = QtGui.QColor(180, 180, 180, 180)
            gradColor1 = QtGui.QColor(180, 180, 180, 180)

        qp.setRenderHints(qp.Antialiasing)
        gradient = QtGui.QConicalGradient()
        gradient.setCenter(br.center())
        gradient.setAngle(270)
        gradient.setColorAt(0, gradColor0)
        gradient.setColorAt(1, gradColor1)

        gradPenColor = QtGui.QBrush(gradient)
        gradPen = QtGui.QPen(gradPenColor, 4)
        gradPen.setCapStyle(QtCore.Qt.RoundCap)

        # Fill in and out circle

        gradColor0 = QtGui.QColor(220, 220, 220, 255)
        gradColor1 = QtGui.QColor(127, 127, 127, 127)

        mid_gradient = QtGui.QLinearGradient(handleRect.center().x(),
                                             handleRect.center().y(),
                                             handleRect_opposite.center().x(),
                                             handleRect_opposite.center().y()
                                             )
        mid_gradient.setColorAt(0, gradColor1)
        mid_gradient.setColorAt(1, gradColor0)
        gradMidColor = QtGui.QBrush(mid_gradient)

        big_gradient = QtGui.QLinearGradient(handleRect.center().x(),
                                             handleRect.center().y(),
                                             handleRect_opposite.center().x(),
                                             handleRect_opposite.center().y()
                                             )
        big_gradient.setColorAt(0, gradColor0)
        big_gradient.setColorAt(1, gradColor1)
        gradBigColor = QtGui.QBrush(big_gradient)

        circlePath = QtGui.QPainterPath()
        circlePath.moveTo(dx_countain, dy_countain)
        circlePath.arcTo(br_countain, 0.0, 360.0)

        qp.fillPath(circlePath, greyPenColor)

        circlePath = QtGui.QPainterPath()
        circlePath.moveTo(dx_out, dy_out)
        circlePath.arcTo(br_out, 0.0, 360.0)

        qp.fillPath(circlePath, gradBigColor)

        circlePath = QtGui.QPainterPath()
        circlePath.moveTo(dx_in, dy_in)
        circlePath.arcTo(br_in, 0.0, 360.0)

        qp.fillPath(circlePath, gradMidColor)



        qp.setPen(dynPen)
        qp.drawArc(br, 290 * 16, 320 * 16)

        qp.setPen(gradPen)
        qp.drawArc(br, 290*16, 320*16)

        qp.setPen(whitePen)
        #qp.drawEllipse(br_in)
        qp.setPen(QtGui.QPen(dynPenColor, 1))
        qp.drawEllipse(br_out)

        if not self._onAnim:
            qp.setPen(QtGui.QPen(dynPenColor, 6))
            qp.drawEllipse(handleRect)

        br.moveTop(r)
        try:
            if self.mode == 'temp':
                text = tempDial2temp(int(self._val))
            else:
                text = self._val
        except UnboundLocalError:
            text = ''
        except ValueError:
            text = ''
        qp.drawText(br, QtCore.Qt.AlignCenter, text)




    def changeColor(self, val):
        try:
            self.color = self.evaluateColor(self.value())
            self._onAnim = False
            self.child.setVisible(False)
            self._val = str(val)
            self.update()
        except:
            pass

    def setVal(self, val):
        self._val = str(val)
    def animateCursor(self):
        if not self._onAnim:
            self._onAnim = True
            self._val = 'Auto'
            self.child.updateColor(self.color)
            _cursorCenter = QtCore.QPoint(int(self._cursorPoint.x() - 6),
                                          int(self._cursorPoint.y() - 6)
                                          )
            self.child.setVisible(True)
            self.anim1.setStartValue(_cursorCenter)
            self.anim1.setEndValue(self.center)
            self.anim_sub_group.start()
            self.update()

    def evaluateColor(self, _valDial):
        if self.mode == 'temp':
            r = int(255* (_valDial/30))
            b = int(255* (1 - _valDial/30))
            return {'r': r, 'g': 0, 'b': b, 'a': 110}
        elif self.mode == 'fan':
            r = int(220 * ((_valDial - 1) / 11))
            g = int(220 * ((_valDial - 1) / 11))
            b = int(220 * ((_valDial - 1) / 11))
            return {'r': r, 'g': g, 'b': b, 'a': 180}
        else:
            return {'r': 150, 'g': 150, 'b': 150, 'a': 127}