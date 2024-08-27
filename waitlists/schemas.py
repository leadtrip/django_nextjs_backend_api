from datetime import datetime
from pydantic import EmailStr
from ninja import Schema


class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr


class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryIn
    id: int
    email: EmailStr


class WaitlistEntryDetailsSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime