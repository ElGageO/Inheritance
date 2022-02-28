class Person:

    def __init__(self, name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__phone = telephone_number

    def print_person(self):
        print('\nThis person is', self.__name)
        print('They live at', self.__address)
        print('Their phone number is', self.__phone)


class Customer(Person):

    def __init__(self, name, address, telephone_number, customer_number, mailing_list):
        Person.__init__(self, name, address, telephone_number)
        
        self.__cn = customer_number
        self.__mailing = mailing_list

    def print_person(self):
        Person.print_person(self)
        
        print('They are customer number', self.__cn)
        
        if self.__mailing:
            print('They would like to be on the mailing list.')
        else:
            print('They would not like to be on the mailing list.')

