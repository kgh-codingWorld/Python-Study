from fastapi import FastAPI, Query, Path, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field

# FastAPI 인스턴스 생성
app = FastAPI(
    title="학습용 API",
    description="FastAPI 학습을 위한 기본 API",
    version="0.1.0"
)

# 기본 모델 정의
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="아이템 이름")
    price: float = Field(..., gt=0, description="아이템 가격")
    is_offer: bool = Field(default=False, description="할인 여부")
    tags: List[str] = Field(default=[], description="아이템 태그")
    description: Optional[str] = Field(None, max_length=300, description="아이템 설명")

# 메모리 데이터베이스 역할을 하는 딕셔너리
items_db = {}

# 루트 경로 핸들러
@app.get("/")
async def root():
    """API 루트 경로"""
    return {"message": "안녕하세요! FastAPI에 오신 것을 환영합니다!"}

# 아이템 목록 조회 핸들러
@app.get("/items/", response_model=List[Item])
async def read_items(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    """
    아이템 목록을 조회합니다.
    
    - **skip**: 건너뛸 아이템 수
    - **limit**: 반환할 최대 아이템 수
    """
    # 함수 구현

# 특정 아이템 조회 핸들러
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int = Path(..., ge=1, description="조회할 아이템의 ID")):
    """
    특정 아이템을 조회합니다.
    
    - **item_id**: 조회할 아이템의 ID
    """
    # 함수 구현

# 아이템 생성 핸들러
@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    """
    새 아이템을 생성합니다.
    
    - **item**: 생성할 아이템 정보
    """
    # 함수 구현

# 아이템 업데이트 핸들러
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """
    아이템을 업데이트합니다.
    
    - **item_id**: 업데이트할 아이템의 ID
    - **item**: 업데이트할 아이템 정보
    """
    # 함수 구현

# 아이템 삭제 핸들러
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """
    아이템을 삭제합니다.
    
    - **item_id**: 삭제할 아이템의 ID
    """
    # 함수 구현

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)