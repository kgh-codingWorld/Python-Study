from typing import Optional
class Rectangle:
    """
    직사각형을 표현하는 클래스
    
    Attributes:
        width (float): 가로 길이
        height (float): 세로 길이
    """
    
    def __init__(self, width:float, height:float)->None:
        """
        Rectangle 클래스의 생성자
        
        Args:
            width (float): 가로 길이
            height (float): 세로 길이
        """
        # 속성 초기화 구현
        
    def area(self)->float:
        """
        직사각형의 넓이를 계산
        
        Returns:
            float: 직사각형의 넓이
        """
        # 메서드 구현
        
    def perimeter(self):
        """
        직사각형의 둘레를 계산
        
        Returns:
            float: 직사각형의 둘레
        """
        # 메서드 구현
        
    def is_square(self)->bool:
        """
        정사각형인지 확인
        
        Returns:
            bool: 정사각형이면 True, 아니면 False
        """
        # 메서드 구현


class BankAccount:
    """
    은행 계좌를 표현하는 클래스
    
    Attributes:
        account_number (str): 계좌번호
        owner_name (str): 계좌 소유자 이름
        balance (float): 계좌 잔액
    """
    
    def __init__(self, account_number:str, owner_name:str, initial_balance:Optional[float]=0)->None:
        """
        BankAccount 클래스의 생성자
        
        Args:
            account_number (str): 계좌번호
            owner_name (str): 계좌 소유자 이름
            initial_balance (float, optional): 초기 잔액. 기본값은 0
        
        Raises:
            ValueError: 초기 잔액이 음수일 경우
        """
        # 속성 초기화 구현
        
    def deposit(self, amount:float)->float:
        """
        계좌에 돈을 입금
        
        Args:
            amount (float): 입금할 금액
            
        Returns:
            float: 입금 후 잔액
            
        Raises:
            ValueError: 입금액이 0 이하일 경우
        """
        # 메서드 구현
        
    def withdraw(self, amount:float)->float:
        """
        계좌에서 돈을 출금
        
        Args:
            amount (float): 출금할 금액
            
        Returns:
            float: 출금 후 잔액
            
        Raises:
            ValueError: 출금액이 0 이하이거나 잔액보다 클 경우
        """
        # 메서드 구현
        
    def get_balance(self)->float:
        """
        현재 잔액 조회
        
        Returns:
            float: 현재 잔액
        """
        # 메서드 구현
