from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass
    
    @abstractmethod 
    def send(self, destination: str) -> None:  # ----- 중복되는 추상 메소드
        pass

    def __str__(self): # ----- 중복되는 일반 메소드
        return "Message 클래스의 인스턴스"

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None: 
        pass 
    
    def __str__(self): # ----- 중복되는 일반 메소드
        return "Sendable 클래스의 인스턴스"


class Email(Message, Sendable):
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email
        
    def print_message(self):
        print(f"이메일 내용입니다: \n{self.content}")
    
    def send(self, destination): # ----- 중복되는 추상 메소드
        print(f"이메일을 주소 {self.user_email}에서 {destination}로 보냅니다!")
        
email = Email("안녕? 오랜만이야 잘 지내니?", "young@codeit.kr")
email.print_message()
email.send("captain@codeit.kr")