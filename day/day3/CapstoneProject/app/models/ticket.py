

from enum import Enum


class TicketStatus(str, Enum):
    """The fixed set of statuses a ticket can be in."""
    NEW = "new"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    ON_HOLD = "on_hold"
    RESOLVED = "resolved"
    CLOSED = "closed"



ALLOWED_TRANSITIONS: dict[TicketStatus, set[TicketStatus]] = {
    TicketStatus.NEW: {TicketStatus.ASSIGNED},
    TicketStatus.ASSIGNED: {TicketStatus.IN_PROGRESS},
    TicketStatus.IN_PROGRESS: {TicketStatus.ON_HOLD, TicketStatus.RESOLVED},
    TicketStatus.ON_HOLD: {TicketStatus.IN_PROGRESS},
    TicketStatus.RESOLVED: {TicketStatus.CLOSED},
    TicketStatus.CLOSED: set(),  # CLOSED is terminal — no further transitions allowed
}


def is_valid_transition(current_status: TicketStatus, new_status: TicketStatus) -> bool:
    """
    Custom application-specific rule: is moving from current_status to
    new_status allowed by the ticket lifecycle?
    Used by the status-transition endpoint before writing to the database.
    """
    return new_status in ALLOWED_TRANSITIONS.get(current_status, set())
