"""""""""""""""
Manage Address book
"""""""""""""""
"""
def run():
    print("Contact")

if __name__ == "__main__":
    run()
"""


class Contact:
    # We must kno
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_myContact_info(self):
        print("Name = ", self.name)
        print("phone_number = ", self.phone_number)
        print("e_mail = ", self.e_mail)
        print("addr = ", self.addr)


"""
We will receive some data from User input
"""


def set_contact_info():
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    e_mail = input("E_mail : ")
    addr = input("addr  : ")
    print(name, phone_number, e_mail, addr)


def run():
    '''
    kim_contact=Contact('김일구','010-4315-4512','kimilgu@gmail.com','Seoul')
    kim_contact.print_myContact_info()
    '''
    set_contact_info()


if __name__ == "__main__":
    run()

"""""""""""""""
Question 4-1
2015년 9월 초의 네이버 종가는 표 3.2와 같습니다. 09/07의 종가를 리스트의 첫 번째 항목으로 입력해서 naver_end_price라는 이름의 리스트를 만들어보세요.
naver_end_price = [474500, 461500, 501000, 500500, 488500]
"""""""""""""""