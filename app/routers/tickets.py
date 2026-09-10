from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db import get_session
from app.models import Ticket, User, Asset
from app.schemas import TicketCreate, TicketRead

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/", response_model=TicketRead)
def create_ticket(ticket: TicketCreate, session: Session = Depends(get_session)):
    user = session.get(User, ticket.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Utente non trovato")

    if ticket.asset_id is not None:
        asset = session.get(Asset, ticket.asset_id)
        if not asset:
            raise HTTPException(status_code=404, detail="Asset non trovato")

    db_ticket = Ticket.model_validate(ticket)
    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)
    return db_ticket


@router.get("/", response_model=list[TicketRead])
def read_tickets(session: Session = Depends(get_session)):
    tickets = session.exec(select(Ticket)).all()
    return tickets


@router.get("/{ticket_id}", response_model=TicketRead)
def read_ticket(ticket_id: int, session: Session = Depends(get_session)):
    ticket = session.get(Ticket, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket non trovato")

    return ticket