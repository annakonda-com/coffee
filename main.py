import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QWidget, QPushButton
from PyQt6 import uic

con = sqlite3.connect("coffee.sqlite")
cur = con.cursor()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(self.size())
        self.pushButton.clicked.connect(self.on_click)
        self.show_table()

    def show_table(self):
        result = cur.execute(
            "SELECT name, roasting.degree, condition.condition, taste, price, volume FROM coffee_data "
            "INNER JOIN roasting ON roasting.id = coffee_data.roasting "
            "INNER JOIN condition ON condition.id = coffee_data.condition").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                self.tableWidget.item(i, j).setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
        self.tableWidget.resizeColumnsToContents()

    def on_click(self):
        self.statistic_form = AddEditCoffeeForm()
        self.statistic_form.show()
        self.setVisible(False)

    def close(self):
        con.close()


class AddEditCoffeeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setFixedSize(self.size())

        self.no_select = QPushButton("Сбросить выделение", self)
        self.no_select.resize(128, 31)
        self.no_select.move(270, 550)
        self.no_select.setVisible(False)
        self.no_select.clicked.connect(self.no_select_func)

        self.pushButton_2.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add_value)
        self.tableWidget.itemSelectionChanged.connect(self.on_selection)

        self.show_table()

        self.clear_table = False
        self.update_value = False

    def add_value(self):
        if not self.update_value:
            values = [self.name.text(), self.roasting.text(), self.condition.text(), self.taste.text(),
                      self.price.text(),
                      self.volume.text()]
            if not all(values):
                self.warning.setText("Пожалуйста, заполните все поля!")
            elif values[1] not in ['1', '2', '3']:
                self.warning.setText("Значение обжарки должно быть 1, 2 или 3")
            elif values[2] not in ['1', '2']:
                self.warning.setText("Значение молотый/в зёрнах должно быть 1 или 2")
            else:
                try:
                    price = int(values[4])
                    volume = int(values[5])
                    cur.execute(
                        "INSERT INTO coffee_data(name, roasting, condition, taste, price, volume) VALUES(?, ?, ?, ?, ?, ?)",
                        (values[0], int(values[1]), int(values[2]), values[3], price, volume))
                    con.commit()
                    self.show_table()
                    self.warning.setText("Успешно добавлено!")
                    self.name.setText('')
                    self.roasting.setText('')
                    self.condition.setText('')
                    self.taste.setText('')
                    self.price.setText('')
                    self.volume.setText('')
                except ValueError:
                    self.warning.setText("Значения цены и объёма должны быть числами")
        else:
            self.update_values()

    def on_selection(self):
        if not self.clear_table:
            self.no_select.setVisible(True)
            self.pushButton.setText("Обновить запись")
            self.list_of_chosen = [i.row() + 1 for i in self.tableWidget.selectionModel().selectedRows()]
            if len(self.list_of_chosen) > 1:
                self.warning.setText("Пожалуйста, выберите только одну строку!")
            elif self.list_of_chosen == []:
                self.no_select_func()
            else:
                self.name.setText(self.tableWidget.item(self.list_of_chosen[0] - 1, 1).text())
                self.roasting.setText(self.tableWidget.item(self.list_of_chosen[0] - 1, 2).text())
                self.condition.setText(self.tableWidget.item(self.list_of_chosen[0] - 1, 3).text())
                self.taste.setText(self.tableWidget.item(self.list_of_chosen[0] - 1, 4).text())
                self.price.setText(self.tableWidget.item(self.list_of_chosen[0] - 1, 5).text())
                self.volume.setText(self.tableWidget.item(self.list_of_chosen[0] - 1, 6).text())
                self.warning.setText('')
                self.update_value = True

    def no_select_func(self):
        self.clear_table = True
        self.no_select.setVisible(False)
        self.pushButton.setText("Добавить запись")
        self.tableWidget.clearSelection()
        self.clear_table = False
        self.warning.setText('')
        self.name.setText('')
        self.roasting.setText('')
        self.condition.setText('')
        self.taste.setText('')
        self.price.setText('')
        self.volume.setText('')

    def show_table(self):
        result = cur.execute(
            "SELECT coffee_data.id, name, roasting.degree, condition.condition, taste, price, volume FROM coffee_data "
            "INNER JOIN roasting ON roasting.id = coffee_data.roasting "
            "INNER JOIN condition ON condition.id = coffee_data.condition").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if j == 0:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                    self.tableWidget.item(i, j).setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
                    self.tableWidget.item(i, j).setFlags(Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.resizeColumnsToContents()

    def update_values(self):
        values = [self.name.text(), self.roasting.text(), self.condition.text(), self.taste.text(),
                  self.price.text(),
                  self.volume.text()]
        if not all(values):
            self.warning.setText("Пожалуйста, заполните все поля!")
        elif values[1] not in ['1', '2', '3']:
            self.warning.setText("Значение обжарки должно быть 1, 2 или 3")
        elif values[2] not in ['1', '2']:
            self.warning.setText("Значение молотый/в зёрнах должно быть 1 или 2")
        else:
            try:
                price = int(values[4])
                volume = int(values[5])
                cur.execute(
                    "UPDATE coffee_data SET name = ?, roasting = ?, condition = ?, taste = ?, price = ?, volume = ? WHERE id == ?",
                    (values[0], int(values[1]), int(values[2]), values[3], price, volume, self.list_of_chosen[0]))
                con.commit()
                self.show_table()
                self.warning.setText("Успешно обновлено!")
                self.update_value = False
                self.name.setText('')
                self.roasting.setText('')
                self.condition.setText('')
                self.taste.setText('')
                self.price.setText('')
                self.volume.setText('')
            except ValueError:
                self.warning.setText("Значения цены и объёма должны быть числами")

    def back(self):
        ex.setVisible(True)
        self.setVisible(False)

    def close(self):
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
