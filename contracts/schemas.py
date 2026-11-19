from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class OCPPFrame:
    charge_point_id: str
    message_id: str
    transaction_id: int | None
    action: str
    timestamp_ms: int


@dataclass(frozen=True)
class PowerAllocation:
    charge_point_id: str
    connector_id: int
    limit_amps_l1: float
    limit_amps_l2: float
    limit_amps_l3: float
    state: Literal["PENDING_COMMIT", "ACTIVE", "FAILSAFE"]
