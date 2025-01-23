class InvalidAgeException(Exception):
    pass

number=18

try:
    input_num= int(input("enter your number "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("eligible")
        
except InvalidAgeException:
    print("exception occured: invalid age")
