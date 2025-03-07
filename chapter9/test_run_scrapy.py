# Scrapy 테스트 (실행만 테스트)
from run_scrapy import run_spider
import pytest
import os

@pytest.mark.skip(reason="Scrapy 테스트는 시간이 오래 걸림")
def test_scrapy_run():
    # 스파이더 실행 테스트 (출력 파일 생성 확인)
    output_file = "test_output.json"
    run_spider("news", output_file)
    assert os.path.exists(output_file)
    os.remove(output_file)  # 테스트 후 파일 삭제