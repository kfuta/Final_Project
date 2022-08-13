from controller import *


def main() -> None:
    """
    Links main.py, controller.py, and view.py.
    """
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
