from typing import Annotated

from fastapi import Depends

from svc.backendsvc.adapters.repositories.leads_repository.in_memory_repository import (
    InMemoryLeadsRepository,
)
from svc.backendsvc.ports.repositories.leads_repository import LeadsRepository
from svc.backendsvc.use_cases.listing_use_case import ListingUseCase


def get_lead_repository() -> LeadsRepository:
    return InMemoryLeadsRepository()


def get_lead_use_case(
    lead_repository: Annotated[LeadsRepository, Depends(get_lead_repository)],
) -> ListingUseCase:
    return ListingUseCase(lead_repository)
