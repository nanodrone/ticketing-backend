from fastapi import APIRouter, Depends, HTTPException
from requests import session
from sqlmodel import Session, select

from app.db import get_session
from app.security import get_current_user
from app.models import Ticket, User, Asset
from app.schemas import TicketCreate, TicketRead
from app.schemas import TicketUpdate

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


@router.get("/", response_model=list[TicketRead])
def read_tickets(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    tickets = session.exec(select(Ticket)).all()
    return tickets

@router.patch("/{ticket_id}", response_model=TicketRead)
def update_ticket(ticket_id: int, ticket_update: TicketUpdate, session: Session = Depends(get_session)):
    db_ticket = session.get(Ticket, ticket_id)

    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket non trovato")

    ticket_data = ticket_update.model_dump(exclude_unset=True)
    db_ticket.sqlmodel_update(ticket_data)

    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)
    return db_ticket