from uuid import UUID



class LeadsNotFoundError(Exception):
    def __init__(self, lead_id: UUID):
        self.lead_id = lead_id

    def __str__(self) -> str:
        return f"Leads not found: {self.lead_id}"

