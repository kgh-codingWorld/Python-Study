from meta_classes import singleton, LoggingMeta

# 클래스 데코레이터와 메타클래스 테스트
def test_sigleton():
    # singleton 데코레이터 테스트
    @singleton
    class TestSingleton:
        def __init__(self, value):
            self.value = value
    
    instance1 = TestSingleton(1)
    instance2 = TestSingleton(2)
    assert instance1 is instance2
    assert instance1.value == instance2.value

def test_LoggingMeta():
    # LoggingMeta 메타클래스 테스트
    class TestService(metaclass=LoggingMeta):
        def process(self, data):
            return f"처리된 데이터: {data}"
        
        def analyze(self, data):
            return {"result": f"분석 결과: {data}"}
    
    service = TestService()
    # 로깅 메시지는 출력으로 확인해야 함
    result = service.process("테스트")
    assert result == "처리된 데이터: 테스트"
