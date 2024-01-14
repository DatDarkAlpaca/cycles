import os
from PySide6.QtWidgets import QApplication

from styles import set_styles
from main_window import MainWindow


def set_working_directory():
    working_dir = os.environ.get('WORKING_DIR')
    if working_dir:
        os.chdir(working_dir)
        print(f"Using {working_dir} as the application's working directory")
    else:
        print('Using default working directory')


def main():
    set_working_directory()

    app = QApplication()
    set_styles(app)

    main_window = MainWindow()
    main_window.show()

    app.exec()


if __name__ == '__main__':
    main()
