class User:
    # 인스턴스 변수 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)

    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)
        # 코드를 입력하세요

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        return len(self.following_list)
        # 코드를 입력하세요

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 유저마다 서로 관심 있는 유저를 팔로우
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

# 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())


"""
인스턴스 메소드 안에서 self는 인스턴스 자신을 가리키는 변수일 뿐입니다. 다른 인스턴스를 가리키는 것은 어떠한 이름의 변수명을 따로 받아와야 합니다. 인스턴스는 사실 다른 인스턴스와 독립적인 관계입니다. 인스턴스 간에 어떠한 변수로 연결되어 있지 않습니다. 
그러기 때문에 parameter로 another_user라는 인스턴스를 변수로 받아와서 다른 인스턴스의 인스턴스 변수를 수정할 수 있습니다.

"""
