class Engineer: 
    def __init__(self, favourite_language):
        self.favourite_language = favourite_language 

    def program(self): 
        print("{}으로 프로그래밍을 합니다.".format(self.favourite_language))


class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다.".format(self.tennis_level))


class EngineerTennisPlayer(Engineer, TennisPlayer):
    def __init__(self, favourite_language, tennis_level): 
        Engineer.__init__(self, favourite_language)
        TennisPlayer.__init__(self, tennis_level)


# 다중상속을 받는 클라스의 인스턴스 생성
minwoo = EngineerTennisPlayer('Java','beginner')

# 두 부모 클라스의 메소들을 잘 물려받았는지 확인 
minwoo.program()
minwoo.play_tennis()


""" 
자식 클라스는 부모 클라스 둘 다 로부터 변수와 메소드를 상속받는다.
그러면, favourite_language 랑 tennis_level 두 파라미터 모두 필요하니까 init 메소드가 오버라이딩이 필요하다!!!
하지만 super().은  못쓴다: 이게 다중상속의 단점이다.
"""