import configparser
import random

from captcha.image import ImageCaptcha
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class TwoFactoresSystem:
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("__app__.ini")

        self.email = self.config.get('config', 'email')
        self.password = self.config.get('config', 'password')
        self.host = self.config.get('config', 'host')
        self.port = self.config.getint('config', 'port')
        
    
    def generate_captcha(self) -> tuple:
        c = ImageCaptcha()
        captcha_code = str(random.randint(100000, 999999))
        captcha_img = c.generate(captcha_code)

        captcha = captcha_img.getvalue()

        return captcha, captcha_code