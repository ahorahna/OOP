"""
상위 모듈인 GameCharacter 클라스가 하위 모듈인 Sword 클라스의 구현 내용에 의존하고 있다 
"""

class Sword:
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage

    def slash(self, other_character): #다른 게임 캐릭터를 파라미터로 받아서 
        """검 사용 메소드"""
        other_character.get_damage(self.damage)


class GameCharacter:
    """게임 캐릭터 클래스"""
    def __init__(self, name, hp, sword: Sword):
        self.name = name
        self.hp = hp
        self.sword = sword

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.sword.slash(other_character)
        else:
            print(self.name + "님은 사망해서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 사망했습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        """남은 체력을 문자열로 리턴하는 메소드"""
        return self.name + "님은 hp: {}이(가) 남았습니다.".format(self.hp)

bad_sword = Sword(1)
good_sword = Sword(100)

game_character1 = GameCharacter('Bananana', 100, bad_sword)
game_character2 = GameCharacter('Grape', 1000, good_sword)

game_character1.attack(game_character2)
game_character1.attack(game_character2)
game_character1.attack(game_character2)
game_character2.attack(game_character1)

print(game_character1)
print(game_character2)
