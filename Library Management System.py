class Library:
    def __init__(self, listOfBooks):
        # 도서관에 있는 책 목록을 초기화합니다.
        self.books = listOfBooks

    def display_available_books(self):
        # 도서관에 현재 보유 중인 책 목록을 출력합니다.
        print("Books present in this library are: ")
        for book in self.books:
            print("- " + book)

    def borrow_books(self, bookName):
        # 사용자가 요청한 책을 대출 처리합니다.
        if bookName in self.books:
            # 요청한 책이 도서관에 있는 경우 대출을 승인하고 목록에서 제거합니다.
            self.books.remove(bookName)
            print(f"\nYou have been issued {bookName}. Keep it safe & Return in 30 Days.")
            return True
        else:
            # 요청한 책이 이미 대출된 경우 사용자에게 알립니다.
            print("\nSorry! This book is already issued. Wait until the book is returned.")
            return False

    def return_book(self, bookName):
        # 사용자가 반납한 책을 도서관 목록에 추가합니다.
        self.books.append(bookName)
        print("\nThanks for returning the book on time! Hope you enjoyed reading. Have a nice day!")

    def search_book(self, keyword):
        # 키워드가 포함된 책을 검색합니다.
        found_books = [book for book in self.books if keyword.lower() in book.lower()]
        if found_books:
            # 검색 결과가 있는 경우 출력합니다.
            print("\nBooks found:")
            for book in found_books:
                print("- " + book)
        else:
            # 검색 결과가 없는 경우 메시지를 출력합니다.
            print("\nNo books found with that keyword.")


class Student:
    def __init__(self):
        # 대출한 책 목록을 초기화합니다.
        self.borrowed_books = []

    def request_book(self):
        # 사용자가 대출을 요청할 책의 이름을 입력받습니다.
        self.book = input("\nEnter the book you want to issue: ")
        return self.book

    def return_book(self):
        # 사용자가 반납할 책의 이름을 입력받습니다.
        self.book = input("\nEnter the book you want to return: ")
        return self.book

    def display_borrowed_books(self):
        # 대출 중인 책 목록을 출력합니다.
        if self.borrowed_books:
            print("\nBooks you have borrowed:")
            for book in self.borrowed_books:
                print("- " + book)
        else:
            print("\nYou have not borrowed any books yet.")

    def borrow_book(self, book_name):
        # 대출한 책 목록에 책을 추가합니다.
        self.borrowed_books.append(book_name)

    def return_book_from_list(self, book_name):
        # 대출한 책 목록에서 책을 제거합니다.
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
        else:
            print("\nYou have not borrowed this book.")


if __name__ == "__main__":
    # 도서관 객체를 생성하고 초기 도서 목록을 설정합니다.
    TheGreatLibrary = Library(
        [
            "Think and Grow Rich",
            "Can't Hurt Me",
            "Atomic Habits",
            "48 Laws Of Power",
            "Growth Mindset",
            "The Power of Habit",
            "Rich Habits"
        ]
    )

    # 학생 객체를 생성합니다.
    student = Student()

    while True:
        
        welcomemsg = """
        ╔══════════════════════════════════════════════════╗
        ║            Welcome To Hanbat's Library           ║
        ║  The place where you can get your desired book   ║
        ╚══════════════════════════════════════════════════╝

        Please Choose an Option:

        1. List of all the books.
        2. Request a book.
        3. Return a book.
        4. View borrowed books.
        5. Search for a book.
        6. Exit.
        """
        # 사용자에게 선택할 메뉴를 출력합니다.
        print(welcomemsg)

        # 사용자 입력을 처리하기 위해 try 문을 사용합니다.
        try:
            # 사용자가 입력한 옵션 번호를 정수로 변환합니다.
            a = int(input("Enter the option number: "))
            
            # 입력 값이 메뉴 범위에 포함되지 않은 경우 경고 메시지를 출력합니다.
            if a not in [1, 2, 3, 4, 5, 6]:
                print("Invalid option! Please choose a number between 1 and 6.")
                continue
        except ValueError:
            # 사용자가 정수가 아닌 값을 입력했을 경우 경고 메시지를 출력합니다.
            print("Invalid input! Please enter a valid number.")
            continue

        if a == 1:
            # 도서관에 현재 있는 책 목록을 표시합니다.
            TheGreatLibrary.display_available_books()
            print("----------------------------------------------------")

        elif a == 2:
            # 사용자가 요청한 책을 대출 처리합니다.
            book_name = student.request_book()
            if TheGreatLibrary.borrow_books(book_name):
                # 책 대출 성공 시 학생의 대출 목록에 추가시킵니다.
                student.borrow_book(book_name)  
            print("----------------------------------------------------")

        elif a == 3:
            # 사용자가 반납한 책을 도서관에 추가합니다.
            book_name = student.return_book()
            # 사용자가 반납하려는 책이 대출 목록에 있는지 확인합니다.
            if book_name in student.borrowed_books:
                # 도서관에 반납하는 코드입니다.
                TheGreatLibrary.return_book(book_name)  
                # 학생의 빌린 책 목록에서 제거시킵니다.
                student.return_book_from_list(book_name)  
            else:
                # 대출 목록에 반납하려는 책이 없을 시 아래와 같은 경고 문구를 출력시킵니다.
                print("\nYou cannot return this book as it is not in your borrowed list.")  
            print("----------------------------------------------------")

        elif a == 4:
            # 사용자가 현재 대출 중인 책 목록을 표시합니다.
            student.display_borrowed_books()
            print("----------------------------------------------------")

        elif a == 5:
            # 사용자가 특정 책을 검색할 수 있는 기능을 실행합니다.
            bookName = input("Enter the name or keyword of the book you want to search: ")
            TheGreatLibrary.search_book(bookName)
            print("----------------------------------------------------")

        elif a == 6:
            # 프로그램을 종료하며 사용자에게 작별 메시지를 출력합니다.
            print("Thanks for using Hanbat Library! Have a great day!")
            break
