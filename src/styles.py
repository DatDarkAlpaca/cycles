from PySide6 import QtGui
from qt_material import apply_stylesheet

from paths import *


def set_styles(app):
    apply_stylesheet(app, theme='dark_teal.xml')
    QtGui.QFontDatabase.addApplicationFont(ROBOTO_FONT_FILEPATH)

    custom_font = QtGui.QFont('Roboto-Regular')
    app.setFont(custom_font, 'QLabel')
