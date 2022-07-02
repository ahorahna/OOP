class AppleKeyboard:
    """apple keyboard class"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def set_keyboard_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_keyboard_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클라스"""
        self.keyboard = None 

    def connect_to_keyboad(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_keyboard_input()

class SamsungKeyboard:
    """삼성 키보드 클라스"""

    def __init__(self):
        """키보드 인풋"""
        self.user_input = ""

    def save_user_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input

    def give_user_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input


keyboard_manager = KeyboardManager()
apple_keyboard = AppleKeyboard()

apple_keyboard.set_keyboard_input('안녕하세요')
keyboard_manager.connect_to_keyboad(apple_keyboard)
print(keyboard_manager.get_keyboard_input())



""" 그런데 이건 Open-closed principle 를 어김 

Polymoorphims 다형성을 이용해서  이 문제를 해결"""
