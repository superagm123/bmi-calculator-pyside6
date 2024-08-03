import sys 
from PySide6.QtWidgets import QApplication, QMainWindow
from View.MainWindow_ui import Ui_MainWindow 
from Model.BMICalculator import BMICalculator


CONVERSION_VALUE = 100


class MainWindow(QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.height_slider.setRange(0, 200)
        self.weight_slider.setRange(1, 300)
        self.signals_connection()

    def signals_connection(self):
        self.height_slider.valueChanged.connect(self.update_height)
        self.weight_slider.valueChanged.connect(self.update_weight)
        self.calculate_button.clicked.connect(self.calculate_bmi)


    def update_height(self, value: int):
        self.height_label.setText(f"{value / CONVERSION_VALUE} M")

    def update_weight(self, value: int):
        self.weight_label.setText(f"{value} KG")

    def calculate_bmi(self):
        height = self.height_slider.value() / CONVERSION_VALUE
        weight = self.weight_slider.value()
        calculator = BMICalculator(weight, height)
        calculator.calculate_bmi()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()