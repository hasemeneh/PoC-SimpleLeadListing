from svc.backendsvc.domain.entities.leads import Leads
from svc.backendsvc.ports.repositories.leads_repository import LeadsRepository
from svc.backendsvc.use_cases.exceptions import (
    LeadsNotFoundError,
)


class ListingUseCase:
    def __init__(self, lead_repository: LeadsRepository):
        self._lead_repository = lead_repository

    async def add(self, new_lead: Leads) -> None:
        await self._lead_repository.add(new_lead)

    async def get_all(self) -> list[Leads]:
        return await self._lead_repository.get_all()
    
    async def enrich(self, id) -> Leads | None:
        leads = await self._lead_repository.enrich(id=id)
        if leads is None :
            raise LeadsNotFoundError(id)
        return leads