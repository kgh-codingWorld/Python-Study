from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

class BaseCustomException(Exception):
    """모든 커스텀 예외의 기본 클래스"""
    def __init__(self, status_code: int, detail: str, code: str = None):
        self.status_code = status_code
        self.detail = detail
        self.code = code
    
    def __str__(self):
        return self.detail

class ResourceNotFoundException(BaseCustomException):
    """리소스를 찾을 수 없을 때 발생하는 예외"""
    def __init__(self, resource_type: str, resource_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource_type} with ID {resource_id} not found",
            code="RESOURCE_NOT_FOUND"
        )

class UnauthorizedAccessException(BaseCustomException):
    """권한이 없을 때 발생하는 예외"""
    def __init__(self, resource: str):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Unauthorized access to {resource}",
            code="UNAUTHORIZED_ACCESS"
        )

class DuplicateResourceException(BaseCustomException):
    """리소스가 이미 존재할 때 발생하는 예외"""
    def __init__(self, resource_type: str, identifier: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"{resource_type} with identifier {identifier} already exists",
            code="DUPLICATE_RESOURCE"
        )

def add_exception_handlers(app: FastAPI):
    """애플리케이션에 예외 핸들러를 등록합니다"""
    
    @app.exception_handler(BaseCustomException)
    async def custom_exception_handler(request: Request, exc: BaseCustomException):
        """모든 커스텀 예외를 처리하는 핸들러"""
        response_content = {"detail": exc.detail}
        if exc.code:
            response_content["code"] = exc.code
        return JSONResponse(
            status_code=exc.status_code,
            content=response_content
        )
    
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """기본 HTTP 예외 핸들러 재정의"""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
                "code": "HTTP_ERROR"
            }
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """요청 검증 예외 핸들러 재정의"""
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": str(exc),
                "code": "VALIDATION_ERROR",
                "errors": exc.errors()
            }
        )
