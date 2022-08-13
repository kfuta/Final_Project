from PyQt5.QtWidgets import *
from view import Ui_MainWindow
from math import *


class Controller(QMainWindow, Ui_MainWindow):
    """
    A controller class that is used to manipulate the GUI window.
    """
    def __init__(self, *args, **kwargs):
        """
        When the user interacts with the GUI window in a specific way, the method links to other methods that
        carry out the window's response to that interaction.
        :param *args: Stores additional arguments as a tuple.
        :param **kwargs: Stores additional key - value pair arguments as a dictionary.
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.calculateButton.clicked.connect(lambda: self.calculate())

    def calculate(self) -> None:
        """
        When the user clicks the calculate button in the GUI window, it is checked that only valid inputs were entered.
        If all inputs are valid, then the composite IQ is calculated and displayed in the GUI window. If at least one
        input is invalid, then an error statement is displayed in the GUI window and a composite IQ is not calculated.
        """
        try:
            s1_score: float = float(self.s1scoreinput.toPlainText())
            s2_score: float = float(self.s2scoreinput.toPlainText())
            s3_score: float = float(self.s3scoreinput.toPlainText())
            if s1_score < 50 or s2_score < 50 or s3_score < 50:
                raise ValueError('Invalid Score(s)')
            elif s1_score > 200 or s2_score > 200 or s3_score > 200:
                raise ValueError('Invalid Score(s)')

            s1_sd: float = float(self.s1sdinput.toPlainText())
            s2_sd: float = float(self.s2sdinput.toPlainText())
            s3_sd: float = float(self.s3sdinput.toPlainText())
            if s1_sd < 1 or s2_sd < 1 or s3_sd < 1:
                raise ValueError('Invalid Standard Deviation(s)')
            if s1_sd > 50 or s2_sd > 50 or s3_sd > 50:
                raise ValueError('Invalid Standard Deviation(s)')

            r12 = float(self.r12input.toPlainText())
            r13 = float(self.r13input.toPlainText())
            r23 = float(self.r23input.toPlainText())
            if 1 < r12 or 1 < r13 or 1 < r23:
                raise ValueError('Invalid Correlation(s)')
            if 0 > r12 or 0 > r13 or 0 > r23:
                raise ValueError('Invalid Correlation(s)')

            sum_squared_sds = (s1_sd ** 2) + (s2_sd ** 2) + (s3_sd ** 2)
            sum_2rab_sda_sdb = (2 * r12 * s1_sd * s1_sd) + (2 * r13 * s1_sd * s3_sd) + (2 * r23 * s2_sd * s3_sd)
            sd_composite = sqrt(sum_squared_sds + sum_2rab_sda_sdb)
            mean_composite = 300

            score_sum = s1_score + s2_score + s3_score
            composite_score = (score_sum - mean_composite) / sd_composite * 15 + 100

            self.outputComposite.setText(f'Your composite score is {composite_score:.2f}.')

        except ValueError:
            self.outputComposite.setText('Cannot calculate. Enter scores between 50 and 200 not inclusive. Enter '
                                         'standard deviations between 1 and 50\nnot inclusive. Enter correlations '
                                         'between 0 and 1 not inclusive.')
