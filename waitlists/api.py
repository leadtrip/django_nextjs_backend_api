from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailsSchema
from.models import WaitlistEntry
from ninja_jwt.authentication import JWTAuth

router = Router()

@router.get("", response=List[WaitlistEntryListSchema], auth=JWTAuth())
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.get("{entry_id}/", response=WaitlistEntryDetailsSchema, auth=JWTAuth())
def get_waitlist_entries(request, entry_id:int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return obj