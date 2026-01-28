from typing import Any

from svc.backendsvc.domain.entities.leads import Leads
from svc.backendsvc.ports.repositories.leads_repository import LeadsRepository

leads_list:  list[Leads] = []

class InMemoryLeadsRepository(LeadsRepository):

    async def get(self, **filters: Any) -> Leads | None:
        for lead_item in leads_list:
            if (f := filters.get("id")) and f == lead_item.id:
                return lead_item
        return None

    async def remove(self, **filters: Any) -> bool:
        for lead_item in leads_list:
            if (f := filters.get("id")) and f == lead_item.id:
                leads_list.remove(lead_item)
                return True
        return False

    async def enrich(self, **filters: Any) -> Leads | None:
        for index,lead_item in enumerate(leads_list):
            if (f := filters.get("id")) and f == lead_item.id:
                leads_list[index].encrich_leads()
                return lead_item
        return None

    async def add(self, new_leads: Leads) -> None :
        leads_list.append(new_leads)

    async def get_all(self) -> list[Leads]:
        return list(leads_list)