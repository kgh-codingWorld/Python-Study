from generators import fibonacci_generator, chunk_iterator, infinite_sequence

# 제너레이터 테스트
def test_fibonacci_generator():
    # fibonacci_generator 테스트
    fib_seq = list(fibonacci_generator(7))
    assert fib_seq == [0, 1, 1, 2, 3, 5, 8]

def test_chunk_iterator():
    # chunk_iterator 테스트
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    chunks = list(chunk_iterator(data, 3))
    assert chunks == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 불규칙한 크기의 마지막 청크 테스트
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    chunks = list(chunk_iterator(data, 3))
    assert chunks == [[1, 2, 3], [4, 5, 6], [7, 8]]

def test_infinite_sequence():
    # infinite_sequence 테스트
    seq = infinite_sequence()
    assert [next(seq) for _ in range(5)] == [0, 1, 2, 3, 4]