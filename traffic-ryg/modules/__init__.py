import os

try:
    import cv2
    """OpenCV present"""
except ModuleNotFoundError:
    os.system("pip install opencv-python")
    """OpenCV not present, installed."""


try:
    import pywhatkit
    """pywhatkit present"""
except ModuleNotFoundError:
    os.system("pip install pywhatkit")
    """pywhatkit not present, installed."""

try:
    import twilio
    """twilio present"""
except ModuleNotFoundError:
    os.system("pip install twilio")
    """twilio not present, installed."""