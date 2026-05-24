from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class RequestStatus(str, Enum):
    PENDING = "pendiente"
    ASIGNED = "asignado"
    COLLECTED = "recogido"
    CANCELED = "cancelado"

class RequestEntity(BaseModel):
    id: Optional[str] = Field(None, description="ID de la solicitud")
    sucursal_id: str = Field(..., description="ID de la sucursal")
    pickup_address: str = Field(..., description="Dirección de recogida")
    package_description: str = Field(..., description="Descripción del paquete")
    requires_refrigeration: bool = Field(..., description="Indica si el paquete requiere refrigeración")

    status: RequestStatus = Field(RequestStatus.PENDING, description="Estado de la solicitud")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de creación de la solicitud")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Fecha de última actualización de la solicitud")
    asigned_driver_id: Optional[str] = Field(None, description="ID del conductor asignado")

    #Para cancelar la solicitud
    def cancel(self)-> bool:
        """Cancela la solicitud si no ha sido recogida."""
        return self.status in [RequestStatus.PENDING, RequestStatus.ASSIGNED]