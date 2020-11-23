import ctypes
from config import MY_COMPANY, MY_PRODUCT, MY_SUBPRODUCT, VERSION


def MakeMyAppOfficial() -> None:
    """
    This function will tell windows not to treat application as a python script
    But rather as an independent executable
    It will be allow us to set up our custom icon in task bar
    Information about company, product and version will be available in windows services

    Original source:
    https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105
    """

    myappid = '.'.join((MY_COMPANY, MY_PRODUCT, MY_SUBPRODUCT, VERSION))
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'{}'.format(myappid))
