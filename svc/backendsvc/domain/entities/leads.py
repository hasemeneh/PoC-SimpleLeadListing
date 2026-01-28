from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from svc.backendsvc.domain.value_objects.enrichment import EnrichmentStatus


@dataclass
class Leads:
    job_title: str
    phone_number: str
    company: str
    headcount: str
    email: str
    industry: str
    name: str
    enrichment: EnrichmentStatus = field(default=EnrichmentStatus.raw)
    id: UUID = field(default_factory=uuid4)

    def encrich_leads(self) -> None:
        self.enrichment = EnrichmentStatus.enriched
