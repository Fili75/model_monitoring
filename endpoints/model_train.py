from fastapi import APIRouter
from src.train import train

router = APIRouter()

@router.get("/model_train")
def model_train():
    train()