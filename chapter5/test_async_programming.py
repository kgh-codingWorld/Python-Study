# test_chapter7.py
import pytest
import asyncio
from async_programming import fetch_data, process_urls, process_data_with_timeout

# 비동기 프로그래밍 테스트
@pytest.mark.asyncio
async def test_fetch_data():
    # fetch_data 테스트
    result = await fetch_data("https://example.com/api/data", delay=0.1)
    assert "url" in result
    assert result["url"] == "https://example.com/api/data"

@pytest.mark.asyncio
async def test_process_urls():
    # process_urls 테스트
    urls = [
        "https://example.com/api/data1",
        "https://example.com/api/data2",
        "https://example.com/api/data3"
    ]
    results = await process_urls(urls)
    assert len(results) == 3
    assert all("url" in result for result in results)

@pytest.mark.asyncio
async def process_data_with_timeout():
    # process_data_with_timeout 테스트
    async def fast_task():
        await asyncio.sleep(0.1)
        return "빠른 작업"
    
    async def slow_task():
        await asyncio.sleep(0.5)
        return "느린 작업"
    
    results = await process_data_with_timeout([fast_task(), slow_task()], timeout=0.3)
    # 빠른 작업은 완료되고 느린 작업은 취소됨
    assert len(results) == 1
    assert results[0] == "빠른 작업"

