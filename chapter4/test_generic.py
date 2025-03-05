import pytest
from generic import DataProcessor,ListProcessor

# 데이터 처리 클래스 테스트
def test_data_processor():
    # 기본 DataProcessor 테스트
    processor = DataProcessor(10, [lambda x: isinstance(x, int)])
    assert processor.get_data() == 10

    # 유효하지 않은 데이터로 초기화
    with pytest.raises(ValueError):
        DataProcessor("not an int", [lambda x: isinstance(x, int)])

    # map 메서드 테스트
    new_processor = processor.map(lambda x: x * 2)
    assert new_processor.get_data() == 20
    
    # filter 메서드 테스트 (리스트 처리)
    list_processor = DataProcessor([1, 2, 3, 4, 5])
    filtered = list_processor.filter(lambda x: all(i % 2 == 0 for i in x))
    assert filtered.get_data() == [2, 4]

# ListProcessor 테스트
def test_list_processor():
    users = [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 25}
    ]
    
    processor = ListProcessor(users)
    
    # group_by 테스트
    grouped = processor.group_by(lambda user: user["age"])
    assert grouped == {
        25: [{"id": 1, "name": "Alice", "age": 25}, {"id": 3, "name": "Charlie", "age": 25}],
        30: [{"id": 2, "name": "Bob", "age": 30}]
    }
    
    # sort_by 테스트
    sorted_processor = processor.sort_by(lambda user: user["name"])
    assert sorted_processor.get_data() == [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 25}
    ]
    
    # 역순 정렬 테스트
    reverse_sorted = processor.sort_by(lambda user: user["name"], reverse=True)
    assert reverse_sorted.get_data() == [
        {"id": 3, "name": "Charlie", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 1, "name": "Alice", "age": 25}
    ]
