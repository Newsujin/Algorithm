def is_prefix(str1, str2):
    if (len(str1) > len(str2)):
        return False
    for i in range(len(str1)):
        if (str1[i] != str2[i]):
            return False
    return True

def solution(phone_book):
    phone_book.sort();
    for i in range(len(phone_book) - 1):
        if (is_prefix(phone_book[i], phone_book[i + 1])):
            return False
    return True