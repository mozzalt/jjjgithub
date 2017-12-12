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

    # print(name, phone_number, e_mail, addr)
    # Test
    contact = Contact(name, phone_number, e_mail,addr)
    return contact

""""""
# Main Menu Construction
""""""

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")

    menu = input("메뉴선택= ")
    return int(menu)


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_myContact_info()

def delete_contact(contact_list, del_name):
    for i, contact in contact_list:
        if contact.name == del_name:
            del contact_list[i]


def save_contact_list_toFile(contact_list):
    f = open("contact_db.txt","wt","UTF-8")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

def run():
    '''
    kim_contact=Contact('김일구','010-4315-4512','kimilgu@gm ail.com','Seoul')
    kim_contact.print_myContact_info()
    '''

    '''
    set_contact_info()
    '''
    contact_list=[]
    while 1:

        menu=print_menu()

        if menu==1:
            contact = set_contact_info()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)

        elif menu ==3:
            del_name=input("Del Name : ")
            delete_contact(contact_list, del_name)

        elif menu==4:
            break





if __name__ == "__main__":
    run()

"""""""""""""""
Question 4-1
2015년 9월 초의 네이버 종가는 표 3.2와 같습니다. 09/07의 종가를 리스트의 첫 번째 항목으로 입력해서 naver_end_price라는 이름의 리스트를 만들어보세요.
naver_end_price = [474500, 461500, 501000, 500500, 488500]
"""""""""""""""