import PersonClass as person

def main():

    person1 = person.Person('Gage Reynolds', '1001 Speight Ave', '(806) 401-6699')
    
    person2 = person.Customer('Dele Alli', '1882 White Hart Lane', '(123) 456-7890', 20, False)

    person1.print_person()
    print()
    person2.print_person()

main()
