def solution(phone_book):
    answer = True

    phone_book.sort()
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1]:
            answer = False
            return answer
    return answer
