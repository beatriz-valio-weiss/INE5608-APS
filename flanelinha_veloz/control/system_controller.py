from flanelinha_veloz.control.client_controller import ClientController
from flanelinha_veloz.control.employees_controller import EmployeesController
from flanelinha_veloz.control.login_controller import LoginController


def shutdown():
    exit(0)


def validate_cpf(cpf: str) -> bool:
    numbers = [int(digit) for digit in cpf]

    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


def validate_email(email: str) -> bool:
    has_char_neededs = False
    sum = 0
    for letter in email:
        if letter == '@' or letter == '.':
            sum += 1
        if sum == 2:
            has_char_neededs = True

    return has_char_neededs


class SystemController:

    def __init__(self):
        self.__login_controller = LoginController(self)
        self.__client_controller = ClientController(self)
        self.__employees_controller = EmployeesController(self)

    @property
    def client_controller(self):
        return self.__client_controller

    @property
    def employees_controller(self):
        return self.__employees_controller

    def open_login_screen(self):
        self.__login_controller.open_screen()
