from abc import ABC, abstractmethod
from typing import Any

from svc.backendsvc.domain.entities.leads import Leads


class LeadsRepository(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> Leads | None:
        pass
    @abstractmethod
    async def remove(self, **filters: Any) -> bool:
        pass
    @abstractmethod
    async def add(self, new_leads: Leads) -> None :
        pass
    @abstractmethod
    async def enrich(self, **filters: Any) -> Leads | None:
        pass
    @abstractmethod
    async def get_all(self) -> list[Leads]:
        pass
    
    