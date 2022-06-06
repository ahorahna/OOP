#인스턴스 메소드를 쓰는 방법

class User: 
    def say_hello(some_user):
        print('hello, this is {}'.format(some_user.name))
            #   여기 name 이라는 instance variable 을 사용
    def login(some_user, new_email, new_pw):
        if (some_user.email == new_email and some_user.password == new_pw):
            print('login successful')
        else: 
            print('login faield')

user1 = User()

#instance variable
user1.name = 'Sooyong Lee'
user1.email = 'captin@gmail.com'
user1.password = '1234' 


#메소드 쓰기
#클래스이름.메소드이름(인스턴스:객체)  
User.say_hello(user1)  

user1.login('captin@gmail.com', '1234')
# user1.login(uswer1, 'captin@gmail.com', '1234') 
# 이건 동작 안할 것임 