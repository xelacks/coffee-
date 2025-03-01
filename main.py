import sys
from PyQt6 import QtWidgets, uic
import sqlite3


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.conn = sqlite3.connect("coffee.sqlite")
        self.cursor = self.conn.cursor()

        self.display_coffee_data()

    def display_coffee_data(self):
        query = "SELECT * FROM coffee"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        self.coffeeTable.setRowCount(0)

        for row_number, row_data in enumerate(rows):
            self.coffeeTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.coffeeTable.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data))
                )

    def closeEvent(self, event):
        self.conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())