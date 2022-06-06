class A:
    def __init__(self, my_number, my_string, my_bool, my_list):
        self.num_value  = my_number
        self.str_value = my_string
        self.bool_value = my_bool
        self.list_value = list(my_list)
    def copy(self, other_a):
        self.num_value = other_a.num_value
        self.str_value = other_a.str_value
        self.bool_value = other_a.bool_value
        self.list_value = list(other_a.list_value)
    def append_list(self, value):
        self.list_value.append(value)

this_a = A(1,'1', True, [1])
another_a = A(2,'2',False, [2])

this_a.copy(another_a)
print(this_a) # 여기서 copy 메소드의 parameter인 other_a라는 곳에 another_a라는 argument를 넘겨주고 있습니다.