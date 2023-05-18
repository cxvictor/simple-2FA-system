import configparser
import random
import smtplib
import ssl

from captcha.image import ImageCaptcha

class TwoFactoresSystem:
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("__app__.ini")

        self.email = self.config.get('config', 'email')
        self.password = self.config.get('config', 'password')
        self.host = self.config.get('config', 'host')
        self.port = self.config.getint('config', 'port')
        self.context = ssl.create_default_context()
        
    
    def generate_captcha(self) -> tuple:
        c = ImageCaptcha()
        captcha_code = str(random.randint(100000, 999999))
        captcha_img = c.generate(captcha_code)

        captcha = captcha_img.getvalue()

        return captcha, captcha_code
    
    
    def verification(self, captcha = None, receiver = None) -> None:
        msg = f"Your verification code:\n {captcha}"
        with smtplib.SMTP_SSL(host=self.host, port=self.port, context=self.context) as server:
            server.login(self.email, self.password)
            server.sendmail(from_addr = self.email, to_addrs = receiver, msg = msg)
            
            
    def input_captcha(self, captcha_code = None, captcha_entered = '123456') -> bool:
        if captcha_code == captcha_entered:
            return True
        else:
            return False
        
        
