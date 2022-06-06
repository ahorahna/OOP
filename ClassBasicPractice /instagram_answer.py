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
        # self.self.followers_list.append(another_user)
        # no return >>> 리턴 값을 돌려주고 함수를 즉시 종료한다.
        # 리턴하면 인스턴스에 값을 설정하지 않는다. 반환하지 않더라도 값을 저장해야 된다. 

    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)
        # 코드를 입력하세요

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        return len(self.followers_list)
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


""""
아주 비슷한 질문들: game character 만들기
"""