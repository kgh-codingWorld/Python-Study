# reverse_string()의 매개변수 text는 str(문자열) 타입을 받아야 함
# 반환값 : str(문자열)
def reverse_string(text:str)->str:
    """
    문자열을 뒤집는 함수
    
    Args:
        text (str): 입력 문자열
        
    Returns:
        str: 뒤집힌 문자열
    """
    # 함수 구현
    # 문자열 뒤집기
    # 1) loop
    # ex. string = "ABCDE"
    #     reverse_str = ""
    #     for i in string:
    #         reverse_str = i + reverse_str
    # 2) slicing
    # string = "ABCDE"
    # pring(str[::-1])
    # 3) reversed
    # string = "ABCDE"
    # reverse_str = ''.join(reversed(string))
    # print(reverse_str)
    return text[::-1]
    
def count_vowels(text:str)->str:
    """
    문자열에서 모음(a, e, i, o, u)의 개수를 세는 함수
    
    Args:
        text (str): 입력 문자열
        
    Returns:
        int: 모음 개수
    """
    # 함수 구현
    cnt = 0
    for i in text:
        if i in ['a','e','i','o','u']:
            cnt = cnt+1
    return cnt
    
def is_palindrome(text:str)->str:
    """
    문자열이 앞뒤로 동일하게 읽히는지 확인하는 함수
    대소문자 구분하지 않고, 알파벳과 숫자만 고려
    
    Args:
        text (str): 입력 문자열
        
    Returns:
        bool: 회문이면 True, 아니면 False
    """
    # 함수 구현
    text = text.replace(" ", "").lower()
    return text == text[::-1]

if __name__ == "__main__":
    is_palindrome("A man a plan a canal Panama")