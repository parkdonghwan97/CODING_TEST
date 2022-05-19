
# 1차  역시 반복문으로 풀었음.. 
# 인덱스 및 len 조건 주기 굉장히 귀찮았다.

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for i in range(len(phone_book)-1): # 일부러 하나 덜받음 (인덱스 범위)
        if phone_book[i] < phone_book[i+1]:
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
            
    
    return answer


    # 다른 풀이  startswith  특정 문자열루 시작하는지 묻는 함수
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):   
            return False
    return True    