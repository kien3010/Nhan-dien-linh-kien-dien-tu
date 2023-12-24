from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from keras.models import load_model
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from File import Ui_File



# Load the model
model = load_model("keras_Model.h5", compile=False)

class_names = [line.strip() for line in open("labels.txt")]



def predict_image(image):
    resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image_array = np.asarray(resized_image, dtype=np.float32).reshape(1, 224, 224, 3)
    normalized_image = (image_array / 127.5) - 1

    prediction = model.predict(normalized_image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score

class Ui_Camera(object):
    def update_display(self):
        ret, frame = self.camera.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.thread1.setPixmap(pixmap)

            # Gọi hàm dự đoán
            class_name, confidence = predict_image(frame)

            # Hiển thị kết quả trong kq1
            result_text = f"Class: {class_name[2:]} - Confidence: {confidence:.2f}"
            self.kq1.setText(result_text)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 809)
        MainWindow.setMinimumSize(QtCore.QSize(555, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.full = QtWidgets.QWidget(self.centralwidget)
        self.full.setObjectName("full")
        self.thread1 = QtWidgets.QLabel(self.full)
        self.thread1.setGeometry(QtCore.QRect(220, 150, 601, 481))
        self.thread1.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                   "border-radius: 25px;")
        self.thread1.setScaledContents(True)
        self.thread1.setObjectName("thread1")
        self.giua = QtWidgets.QWidget(self.full)
        self.giua.setGeometry(QtCore.QRect(10, 10, 851, 131))
        self.giua.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                " border-radius: 15px;")
        self.giua.setObjectName("giua")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.giua)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.haui = QtWidgets.QLabel(self.giua)
        self.haui.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.haui.setFont(font)
        self.haui.setFocusPolicy(QtCore.Qt.NoFocus)
        self.haui.setAcceptDrops(False)
        self.haui.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.haui.setStyleSheet("\n"
                                "image: url(:/newPrefix/HAUI_Logo.png);")
        self.haui.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.haui.setFrameShadow(QtWidgets.QFrame.Plain)
        self.haui.setLineWidth(1)
        self.haui.setText("")
        self.haui.setPixmap(QtGui.QPixmap("HAUI_Logo.png"))
        self.haui.setScaledContents(True)
        self.haui.setAlignment(QtCore.Qt.AlignCenter)
        self.haui.setOpenExternalLinks(False)
        self.haui.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.haui.setObjectName("haui")
        self.horizontalLayout_2.addWidget(self.haui)
        self.tenapp = QtWidgets.QLabel(self.giua)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tenapp.setFont(font)
        self.tenapp.setStyleSheet("color: rgb(255, 0, 0);\n"
                                  "")
        self.tenapp.setAlignment(QtCore.Qt.AlignCenter)
        self.tenapp.setObjectName("tenapp")
        self.horizontalLayout_2.addWidget(self.tenapp)
        self.haui_fee = QtWidgets.QLabel(self.giua)
        self.haui_fee.setMaximumSize(QtCore.QSize(110, 16777215))
        self.haui_fee.setMouseTracking(False)
        self.haui_fee.setAutoFillBackground(False)
        self.haui_fee.setStyleSheet("image: url(:/newPrefix/FEE_Logo.png);")
        self.haui_fee.setText("")
        self.haui_fee.setPixmap(QtGui.QPixmap("FEE_Logo.png"))
        self.haui_fee.setScaledContents(True)
        self.haui_fee.setObjectName("haui_fee")
        self.horizontalLayout_2.addWidget(self.haui_fee)
        self.kq1 = QtWidgets.QLabel(self.full)
        self.kq1.setGeometry(QtCore.QRect(220, 650, 591, 121))
        self.kq1.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                               "border-radius: 25px;")
        self.kq1.setScaledContents(True)
        self.kq1.setObjectName("kq1")
        self.label_4 = QtWidgets.QLabel(self.full)
        self.label_4.setGeometry(QtCore.QRect(0, 690, 201, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.full)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 201, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.next = QtWidgets.QPushButton(self.full)
        self.next.setEnabled(True)
        self.next.setGeometry(QtCore.QRect(30, 270, 170, 40))
        self.next.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kq1.setFont(font)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.next.setFont(font)
        self.next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next.setMouseTracking(True)
        self.next.setTabletTracking(False)
        self.next.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        self.next.setIcon(icon)
        self.next.setIconSize(QtCore.QSize(30, 30))
        self.next.setCheckable(False)
        self.next.setObjectName("next")
        self.giua.raise_()
        self.thread1.raise_()
        self.kq1.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.next.raise_()
        self.horizontalLayout.addWidget(self.full)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add an attribute for OpenCV camera capture
        self.camera = cv2.VideoCapture(0)

        # Create a QTimer for updating the camera feed
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.update_display)
        self.timer.start(10)  # Set the update interval in milliseconds

    def update_display(self):
        ret, frame = self.camera.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.thread1.setPixmap(pixmap)

            # Gọi hàm dự đoán
            class_name, confidence = predict_image(frame)

            # Hiển thị kết quả trong kq1
            result_text = f" {class_name[2:]} - Confidence: {confidence:.2f}"
            self.kq1.setText(result_text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.thread1.setText(_translate("MainWindow",
                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> </span></p></body></html>"))
        self.tenapp.setText(_translate("MainWindow", "ỨNG DỤNG NHẬN DIỆN LINH KIỆN ĐIỆN TỬ"))
        self.kq1.setText(_translate("MainWindow",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "KẾT QUẢ"))
        self.label_5.setText(_translate("MainWindow", "CAMERA"))
        self.next.setText(_translate("MainWindow", "NEXT"))

    def closeEvent(self, event):
        # Release the camera when the application is closed
        self.camera.release()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Camera()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
