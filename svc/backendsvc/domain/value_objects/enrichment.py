from dataclasses import dataclass
from enum import StrEnum


class EnrichmentStatus(StrEnum):
    enriched = "ENRICHED"
    raw = "RAW"

