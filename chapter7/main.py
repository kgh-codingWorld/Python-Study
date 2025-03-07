from fastapi import FastAPI, Depends, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from datetime import datetime
import time
from typing import Callable

from routes import users, products
from exceptions import add_exception_handlers
from background_tasks import generate_reports

@asynccontextmanager
async def lifespan(app:FastAPI):
    # 애플리케이션 시작 이벤트 핸들러
    print("애플리케이션이 시작되었습니다!")
    yield
    # 애플리케이션 종료 이벤트 핸들러
    print("애플리케이션이 종료됩니다!")

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="고급 FastAPI 애플리케이션",
    description="FastAPI의 고급 기능을 활용한 웹 애플리케이션",
    version="1.0.0"
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 프로덕션에서는 구체적인 오리진 지정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 처리 시간 측정 미들웨어
@app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable):
    """
    요청 처리 시간을 측정하고 응답 헤더에 추가하는 미들웨어
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# 라우터 등록
app.include_router(users.router)
app.include_router(products.router)

# 예외 핸들러 등록
add_exception_handlers(app)

# 루트 경로 핸들러
@app.get("/")
async def root():
    """API 루트 경로"""
    return {
        "message": "고급 FastAPI 애플리케이션에 오신 것을 환영합니다!",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

# 상태 확인 엔드포인트
@app.get("/health")
async def health_check():
    """API 상태 확인"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

# 보고서 생성 엔드포인트
@app.post("/reports/{report_type}")
async def create_report(
    report_type: str,
    background_tasks: BackgroundTasks
):
    """
    백그라운드 태스크로 보고서 생성을 요청합니다
    
    Args:
        report_type: 생성할 보고서 유형
    """
    background_tasks.add_task(generate_reports, datetime.now(), report_type)
    return {"message": f"{report_type} 보고서 생성이 요청되었습니다"}


# 애플리케이션 실행 (개발 환경)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
