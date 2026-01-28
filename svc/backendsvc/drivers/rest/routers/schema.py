from uuid import UUID

from pydantic import BaseModel

from svc.backendsvc.domain.entities.leads import Leads




class LeadInput(BaseModel):
    job_title: str
    phone_number: str
    company: str
    headcount: str
    email: str
    industry: str
    name: str

    def to_entity(self) -> Leads:
        return Leads(
            job_title=self.job_title,
            phone_number=self.phone_number,
            company=self.company,
            headcount=self.headcount,
            email=self.email,
            industry=self.industry,
            name=self.name,
        )


class LeadList(BaseModel):
    leads: list[Leads]

    def __init__(self, lead_list: list[Leads]):
        self.leads = lead_list