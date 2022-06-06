""" 
해설 코드 
"""
class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)
    
    
class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name): # 아 여기 인자로 posts 안 넣음? -> 응 ! 
        self.name = name
        self.posts = [] 
        
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """

    def add_post(self, date, content): #이전 클라스를 사용할 수 있다. 즉, 이 두 
        new_post = Post(date, content)  #new_post 는 Post의 인스턴스다.
        self.posts.append(new_post) #추가해줌 

        # self.date = date
        # self.content = self.posts.append(content)

    def show_all_posts(self):
        for post in self.posts:
            print(post)
        # print(self.add_post())

        # 블로그 유저의 게시글은 모두 posts 리스트에 저장되어있다. 
        # 그러니까 for 문으로 리스트를 돌면서 그 안의 모든 게시글 인스턴스를 출력한다. 
        #  그러면 Post 클라스의 __str__ return "작성 날짜: {}\n내용: {}".format(self.date, self.content) 이 실행된다. 

    def __str__(self):
        return "안녕하세요 {} 입니다.\n".format(self.name)
        # 간단한 인사와 이름을 문자열로 리턴
    
    

# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()