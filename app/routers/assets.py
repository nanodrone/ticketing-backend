from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db import get_session
from app.models import Asset
from app.schemas import AssetCreate, AssetRead

router = APIRouter(prefix="/assets", tags=["Assets"])


@router.post("/", response_model=AssetRead)
def create_asset(asset: AssetCreate, session: Session = Depends(get_session)):
    existing_asset = session.exec(
        select(Asset).where(Asset.serial_number == asset.serial_number)
    ).first()

    if existing_asset:
        raise HTTPException(status_code=400, detail="Serial number già registrato")

    db_asset = Asset.model_validate(asset)
    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)
    return db_asset


@router.get("/", response_model=list[AssetRead])
def read_assets(session: Session = Depends(get_session)):
    assets = session.exec(select(Asset)).all()
    return assets


@router.get("/{asset_id}", response_model=AssetRead)
def read_asset(asset_id: int, session: Session = Depends(get_session)):
    asset = session.get(Asset, asset_id)

    if not asset:
        raise HTTPException(status_code=404, detail="Asset non trovato")

    return asset