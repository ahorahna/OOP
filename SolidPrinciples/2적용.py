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

# 여기 수정됨: 키보드가 추가될때마다 이 클라스는 그대로여야 하는데 바뀐다: 즉 개방 폐쇄 원칙을 어긴다.
    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        if isinstance(self.keyboard, AppleKeyboard):
            return self.keyboard.send_keyboard_input()
        elif isinstance(self.keyboard, SamsungKeyboard):
            return self.keyboard.give_user_input()

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

samsung_keyboard = SamsungKeyboard()

keyboard_manager.connect_to_keyboad(samsung_keyboard)

samsung_keyboard.save_user_input('안녕하세요')

print(keyboard_manager.get_keyboard_input())
