from PyQt6.QtWidgets import QApplication, QWidget
import sys

def start_application():
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    app.exec()

if __name__ == "__main__":
    print("Hello world from poetry project project")
    start_application()