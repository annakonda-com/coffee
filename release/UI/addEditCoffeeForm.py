# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Cappuccino(object):
    def setupUi(self, Cappuccino):
        Cappuccino.setObjectName("Cappuccino")
        Cappuccino.resize(620, 600)
        self.tableWidget = QtWidgets.QTableWidget(parent=Cappuccino)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 600, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(parent=Cappuccino)
        self.label.setGeometry(QtCore.QRect(10, 400, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Cappuccino)
        self.label_2.setGeometry(QtCore.QRect(120, 400, 101, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Cappuccino)
        self.textBrowser.setGeometry(QtCore.QRect(120, 460, 101, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(parent=Cappuccino)
        self.label_3.setGeometry(QtCore.QRect(230, 400, 111, 16))
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=Cappuccino)
        self.textBrowser_2.setGeometry(QtCore.QRect(230, 460, 101, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(parent=Cappuccino)
        self.label_4.setGeometry(QtCore.QRect(340, 400, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=Cappuccino)
        self.label_5.setGeometry(QtCore.QRect(450, 400, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Cappuccino)
        self.label_6.setGeometry(QtCore.QRect(10, 530, 91, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(parent=Cappuccino)
        self.pushButton.setGeometry(QtCore.QRect(140, 550, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Cappuccino)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 211, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=Cappuccino)
        self.textBrowser_3.setGeometry(QtCore.QRect(400, 510, 201, 81))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.name = QtWidgets.QLineEdit(parent=Cappuccino)
        self.name.setGeometry(QtCore.QRect(10, 420, 101, 31))
        self.name.setObjectName("name")
        self.roasting = QtWidgets.QLineEdit(parent=Cappuccino)
        self.roasting.setGeometry(QtCore.QRect(120, 420, 101, 31))
        self.roasting.setObjectName("roasting")
        self.condition = QtWidgets.QLineEdit(parent=Cappuccino)
        self.condition.setGeometry(QtCore.QRect(230, 420, 101, 31))
        self.condition.setObjectName("condition")
        self.taste = QtWidgets.QLineEdit(parent=Cappuccino)
        self.taste.setGeometry(QtCore.QRect(340, 420, 101, 31))
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QLineEdit(parent=Cappuccino)
        self.price.setGeometry(QtCore.QRect(450, 420, 101, 31))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(parent=Cappuccino)
        self.volume.setGeometry(QtCore.QRect(10, 550, 101, 31))
        self.volume.setObjectName("volume")
        self.warning = QtWidgets.QLabel(parent=Cappuccino)
        self.warning.setGeometry(QtCore.QRect(16, 370, 591, 20))
        self.warning.setText("")
        self.warning.setObjectName("warning")

        self.retranslateUi(Cappuccino)
        QtCore.QMetaObject.connectSlotsByName(Cappuccino)

    def retranslateUi(self, Cappuccino):
        _translate = QtCore.QCoreApplication.translate
        Cappuccino.setWindowTitle(_translate("Cappuccino", "Cappuccino"))
        self.label.setText(_translate("Cappuccino", "Название Сорта"))
        self.label_2.setText(_translate("Cappuccino", "Степень обжарки"))
        self.textBrowser.setHtml(_translate("Cappuccino", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 - светлая,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 - средняя,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3 - тёмная.</p></body></html>"))
        self.label_3.setText(_translate("Cappuccino", "Молотый/в зёрнах"))
        self.textBrowser_2.setHtml(_translate("Cappuccino", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 - в зёрнах,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 - молотый.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("Cappuccino", "Описание вкуса"))
        self.label_5.setText(_translate("Cappuccino", "Цена"))
        self.label_6.setText(_translate("Cappuccino", "Объём упаковки"))
        self.pushButton.setText(_translate("Cappuccino", "Добавить запись"))
        self.pushButton_2.setText(_translate("Cappuccino", "Вернуться на главный экран"))
        self.textBrowser_3.setHtml(_translate("Cappuccino", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Чтобы изменить существующую запись нажмите на номер интересующей записи  в таблице, а затем введите обновлённые данные в поля для ввода</p></body></html>"))
