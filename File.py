from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from PyQt5.QtCore import pyqtSignal
from keras.models import load_model

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

class Ui_File(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 809)
        MainWindow.setMinimumSize(QtCore.QSize(555, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.full = QtWidgets.QWidget(self.centralwidget)
        self.full.setObjectName("full")
        self.giua = QtWidgets.QWidget(self.full)
        self.giua.setGeometry(QtCore.QRect(10, 10, 951, 131))
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
        self.haui.setPixmap(QtGui.QPixmap("FEE_Logo.png"))
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
        self.haui_fee.setPixmap(QtGui.QPixmap("HAUI_Logo.png"))
        self.haui_fee.setScaledContents(True)
        self.haui_fee.setObjectName("haui_fee")
        self.horizontalLayout_2.addWidget(self.haui_fee)
        self.label_4 = QtWidgets.QLabel(self.full)
        self.label_4.setGeometry(QtCore.QRect(10, 700, 201, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.nhandien = QtWidgets.QPushButton(self.full)
        self.nhandien.setEnabled(True)
        self.nhandien.setGeometry(QtCore.QRect(30, 320, 171, 51))
        self.nhandien.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.nhandien.clicked.connect(self.detect_image)
        self.nhandien.setFont(font)
        self.nhandien.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nhandien.setMouseTracking(True)
        self.nhandien.setTabletTracking(False)
        self.nhandien.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        self.nhandien.setIcon(icon)
        self.nhandien.setIconSize(QtCore.QSize(30, 30))
        self.nhandien.setCheckable(False)
        self.nhandien.setObjectName("nhandien")
        self.selected_image_path = ""
        self.chonanh = QtWidgets.QPushButton(self.full)
        self.chonanh.setGeometry(QtCore.QRect(30, 210, 170, 51))
        self.chonanh.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.chonanh.setFont(font)
        self.chonanh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chonanh.setMouseTracking(True)
        self.chonanh.setStyleSheet("#Inputpicture\n"
                                   "{\n"
                                   "backgroud-color: #fe9f4f;\n"
                                   "}")
        icon1 = QtGui.QIcon()
        self.chonanh.setIcon(icon1)
        self.chonanh.setIconSize(QtCore.QSize(30, 30))
        self.chonanh.setObjectName("chonanh")
        self.xuatfile = QtWidgets.QPushButton(self.full)
        self.xuatfile.setGeometry(QtCore.QRect(30, 430, 170, 51))
        self.xuatfile.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.xuatfile.setFont(font)
        self.xuatfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.xuatfile.setMouseTracking(True)
        self.xuatfile.setStyleSheet("#Inputpicture\n"
                                    "{\n"
                                    "backgroud-color: #fe9f4f;\n"
                                    "}")
        self.xuatfile.setIcon(icon1)
        self.xuatfile.setIconSize(QtCore.QSize(30, 30))
        self.xuatfile.setObjectName("xuatfile")
        self.thread2 = QtWidgets.QLabel(self.full)
        self.thread2.setGeometry(QtCore.QRect(300, 160, 561, 471))
        self.thread2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                   "border-radius: 25px;")
        self.thread2.setScaledContents(True)
        self.thread2.setObjectName("thread2")
        self.kq2 = QtWidgets.QLabel(self.full)
        self.kq2.setGeometry(QtCore.QRect(300, 650, 551, 121))
        self.kq2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                               "border-radius: 25px;")
        self.kq2.setScaledContents(True)
        self.kq2.setObjectName("kq2")
        font.setPointSize(12)
        self.kq2.setFont(font)
        self.previous = QtWidgets.QPushButton(self.full)
        self.previous.setEnabled(True)
        self.previous.setGeometry(QtCore.QRect(30, 540, 171, 51))
        self.previous.setMinimumSize(QtCore.QSize(170, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.previous.setFont(font)
        self.previous.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previous.setMouseTracking(True)
        self.previous.setTabletTracking(False)
        self.previous.setAutoFillBackground(False)
        self.previous.setIcon(icon)
        self.previous.setIconSize(QtCore.QSize(30, 30))
        self.previous.setCheckable(False)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.full)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tenapp.setText(_translate("MainWindow", "ỨNG DỤNG NHẬN DIỆN LINH KIỆN ĐIỆN TỬ"))
        self.label_4.setText(_translate("MainWindow", "KẾT QUẢ"))
        self.nhandien.setText(_translate("MainWindow", "Nhận diện"))
        self.chonanh.setText(_translate("MainWindow", "Chọn ảnh  "))
        self.xuatfile.setText(_translate("MainWindow", "Xuất File"))
        self.thread2.setText(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> </span></p></body></html>"))
        self.kq2.setText(_translate("MainWindow",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> </span></p></body></html>"))
        self.previous.setText(_translate("MainWindow", "PREVIOUS"))

        # Thêm sự kiện click cho nút "Chọn ảnh"
        self.chonanh.clicked.connect(self.select_image)

        # Thêm sự kiện click cho nút "Nhận diện"
        self.nhandien.clicked.connect(self.detect_image)

        # Thêm sự kiện click cho nút "Xuất File"
        self.xuatfile.clicked.connect(self.export_file)

        # ... (code đã được giữ nguyên)

        # Khởi tạo một biến instance để lưu trữ đường dẫn của ảnh đã chọn
        self.selected_image_path = ""

    def select_image(self):
        # Hiển thị hộp thoại chọn tệp và lưu đường dẫn tệp đã chọn
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(None, "Chọn ảnh", "", "All Files (*)", options=options)

        for file_name in file_names:
            # Kiểm tra định dạng của tệp
            allowed_formats = ['.png', '.jpg']
            if not any(file_name.lower().endswith(format) for format in allowed_formats):
                # Hiển thị thông báo nếu định dạng không hợp lệ
                QMessageBox.warning(None, "Định dạng không hợp lệ", "Vui lòng chọn tệp có định dạng PNG hoặc JPG.")
                return

            # Hiển thị ảnh đã chọn trong QLabel thread2
            pixmap = QPixmap(file_name)
            self.thread2.setPixmap(pixmap)
            self.thread2.setAlignment(Qt.AlignCenter)
            # Lưu đường dẫn của ảnh đã chọn
            self.selected_image_path = file_name

    def detect_image(self):
        if self.selected_image_path:
            # Đọc ảnh từ đường dẫn đã chọn
            image = cv2.imread(self.selected_image_path)
            # Thực hiện nhận diện ảnh và hiển thị kết quả trong QLabel kq2
            class_name, confidence_score = predict_image(image)
            result_text = f"Kết quả nhận diện: {class_name[2:]} "
            self.kq2.setText(result_text)
        else:
            # Hiển thị thông báo nếu chưa chọn ảnh
            QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Vui lòng chọn ảnh trước khi nhận diện.")

    def export_file(self):
        if self.selected_image_path:
            # Đọc ảnh từ đường dẫn đã chọn
            image = cv2.imread(self.selected_image_path)

            if image is not None:
                # Thực hiện nhận diện ảnh
                class_name, confidence_score = predict_image(image)

                # Gán nhãn lên ảnh
                label_text = f"{class_name} - {confidence_score:.2%}"
                cv2.putText(image, label_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Lưu ảnh có nhãn
                file_dialog = QFileDialog()
                save_path, _ = file_dialog.getSaveFileName(None, "Lưu ảnh", "",
                                                           "Images (*.png *.xpm *.jpg *.bmp *.gif)")
                if save_path:
                    cv2.imwrite(save_path, image)
                    QtWidgets.QMessageBox.information(None, "Thông báo", "Xuất file thành công.")
                else:
                    QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Vui lòng chọn đường dẫn để lưu file.")
            else:
                QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Không thể đọc ảnh.")
        else:
            # Hiển thị thông báo nếu chưa chọn ảnh
            QtWidgets.QMessageBox.warning(None, "Cảnh báo", "Vui lòng chọn ảnh trước khi xuất file.")
def show_file_interface():
    global ui_file
    MainWindow.hide()
    ui_file = Ui_File()
    ui_file.setupUi(MainWindow)
    MainWindow.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_File()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
