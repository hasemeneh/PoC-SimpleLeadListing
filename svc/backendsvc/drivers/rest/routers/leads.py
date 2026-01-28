from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, status

from svc.backendsvc.drivers.rest.dependencies import get_lead_use_case
from svc.backendsvc.drivers.rest.routers.schema import (LeadInput , LeadList)
from svc.backendsvc.use_cases.listing_use_case import ListingUseCase
from svc.backendsvc.domain.entities.leads import Leads

router = APIRouter(prefix="/api")

@router.post("/leads", status_code=status.HTTP_204_NO_CONTENT)
async def submit_bid(
    data: LeadInput,
    use_case: Annotated[ListingUseCase, Depends(get_lead_use_case)],
) -> None:
    await use_case.add(data.to_entity())

@router.get("/leads", status_code=status.HTTP_200_OK)
async def submit_bid(
    use_case: Annotated[ListingUseCase, Depends(get_lead_use_case)],
) :
    leads = await use_case.get_all()
    return leads

@router.post("/leads/{leads_id}/enrich", status_code=status.HTTP_200_OK)
async def submit_bid(
    leads_id: UUID,
    use_case: Annotated[ListingUseCase, Depends(get_lead_use_case)],
) :
    lead = await use_case.enrich(leads_id)
    return lead