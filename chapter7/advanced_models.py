from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, ValidationInfo
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    """사용자 역할 열거형"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class Address(BaseModel):
    """주소 모델"""
    street: str = Field(..., min_length=1, max_length=100)
    city: str = Field(..., min_length=1, max_length=50)
    country: str = Field(..., min_length=1, max_length=50)
    postal_code: str = Field(..., min_length=1, max_length=20)
    
    @field_validator('postal_code')
    @classmethod
    def validate_postal_code(cls, v: str) -> str:
        """우편번호 형식 검증"""
        # 검증 로직 구현
        return v

class UserBase(BaseModel):
    """사용자 기본 모델"""
    username: str = Field(..., min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr
    full_name: Optional[str] = None
    role: UserRole = UserRole.USER

class UserCreate(UserBase):
    """사용자 생성 모델"""
    password: str = Field(..., min_length=8)
    
    @field_validator('password')
    @classmethod
    def password_strength(cls, v: str) -> str:
        """비밀번호 강도 검증"""
        # 검증 로직 구현
        return v

class User(UserBase):
    """사용자 응답 모델"""
    id: int
    is_active: bool = True
    created_at: datetime
    address: Optional[Address] = None
    
    class Config:
        from_attributes = True

class ProductCategory(str, Enum):
    """제품 카테고리 열거형"""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    FOOD = "food"
    BOOKS = "books"
    OTHER = "other"

class Product(BaseModel):
    """제품 모델"""
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., gt=0)
    category: ProductCategory
    in_stock: bool = True
    tags: List[str] = []
    
    @model_validator(mode='after')
    def check_description_if_premium(self) -> 'Product':
        """프리미엄 제품은 설명이 필수"""
        # 검증 로직 구현
        return self
    
    class Config:
        from_attributes = True
