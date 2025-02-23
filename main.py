import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt6 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setFixedSize(self.size())
        self.con = sqlite3.connect("coffee.sqlite")
        self.show_table()

    def show_table(self):
        cur = self.con.cursor()
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

    def close(self):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
