import re

class RegularMatching:
    # Method to find Sum of numbers presnt in String
    def sum_in_string(string1):
        numbers = re.findall('[0-9]+', string1)
        sum1 = 0
        for i in range(len(numbers)):
            sum1+= int(numbers[i])
        return sum1

    # Regular Expression to validate phone number
    def phone_validation(phone):
        reg_phone = '(0|91)?[-\s]?[6-9]\d{9}'
        print(re.match(reg_phone, phone))

if __name__ == '__main__':
    pass