class Vehicle:
    """
    운송 수단을 표현하는 기본 클래스
    
    Attributes:
        make (str): 제조사
        model (str): 모델명
        year (int): 제조년도
        fuel_capacity (float): 연료 용량
        fuel_level (float): 현재 연료량
    """
    
    def __init__(self, make:str, model:str, year:int, fuel_capacity:float)->None:
        """
        Vehicle 클래스의 생성자
        
        Args:
            make (str): 제조사
            model (str): 모델명
            year (int): 제조년도
            fuel_capacity (float): 연료 용량
        """
        # 속성 초기화 구현
        
    def fuel_up(self)->float:
        """
        연료를 가득 채움
        
        Returns:
            float: 주유한 연료량
        """
        # 메서드 구현
        
    def drive(self, distance:float)->float:
        """
        주행하여 연료 소모
        
        Args:
            distance (float): 주행 거리
            
        Returns:
            float: 남은 연료량
            
        Raises:
            ValueError: 연료가 부족할 경우
        """
        # 메서드 구현


class Car(Vehicle):
    """
    자동차를 표현하는 클래스
    
    Attributes:
        num_doors (int): 문의 개수
        fuel_efficiency (float): 연비 (km/L)
    """
    
    def __init__(self, make:str, model:str, year:int, fuel_capacity:float, num_doors:int, fuel_efficiency:float)->None:
        """
        Car 클래스의 생성자
        
        Args:
            make (str): 제조사
            model (str): 모델명
            year (int): 제조년도
            fuel_capacity (float): 연료 용량
            num_doors (int): 문의 개수
            fuel_efficiency (float): 연비 (km/L)
        """
        # 부모 클래스 생성자 호출 및 추가 속성 초기화
        
    def drive(self, distance:float)->float:
        """
        주행하여 연료 소모 (연비 기반)
        
        Args:
            distance (float): 주행 거리
            
        Returns:
            float: 남은 연료량
            
        Raises:
            ValueError: 연료가 부족할 경우
        """
        # 메서드 구현 (부모 클래스 메서드 오버라이딩)


class Motorcycle(Vehicle):
    """
    오토바이를 표현하는 클래스
    
    Attributes:
        has_sidecar (bool): 사이드카 유무
        fuel_efficiency (float): 연비 (km/L)
    """
    
    def __init__(self, make:str, model:str, year:int, fuel_capacity:float, has_sidecar:bool, fuel_efficiency:float)->None:
        """
        Motorcycle 클래스의 생성자
        
        Args:
            make (str): 제조사
            model (str): 모델명
            year (int): 제조년도
            fuel_capacity (float): 연료 용량
            has_sidecar (bool): 사이드카 유무
            fuel_efficiency (float): 연비 (km/L)
        """
        # 부모 클래스 생성자 호출 및 추가 속성 초기화
        
    def drive(self, distance:float)->float:
        """
        주행하여 연료 소모 (연비 기반)
        
        Args:
            distance (float): 주행 거리
            
        Returns:
            float: 남은 연료량
            
        Raises:
            ValueError: 연료가 부족할 경우
        """
        # 메서드 구현 (부모 클래스 메서드 오버라이딩)
