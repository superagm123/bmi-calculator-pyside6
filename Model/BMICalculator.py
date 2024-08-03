from PySide6.QtWidgets import QWidget, QMessageBox


class BMICalculator(QWidget):
    def __init__(self, weight, height):
        super().__init__()
        self.weight = weight
        self.height = height

    def check_bmi(self, bmi: float):
        if bmi < 18.5:
            QMessageBox.warning(self, "Severe Thinness", f"Your bmi is: {bmi}, Try to eat more.")
        elif bmi > 18.5 and bmi <= 25:
            QMessageBox.information(self, "Normal Weight", f"Your bmi is: {bmi}, Keep it up!")
        elif bmi > 25:
            QMessageBox.warning(self, "Overweight-Obese", f"Your bmi is: {bmi}, You should get some exercise and eat less.")

    def calculate_bmi(self):
        try:
             bmi = round(self.weight / pow(self.height, 2), 2)
             self.check_bmi(bmi = bmi)
        except ZeroDivisionError:
            QMessageBox.critical(self, "Error", "You must select valid values to calculate your bmi.")