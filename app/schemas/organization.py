from pydantic import BaseModel


class OrganizationSchema(BaseModel):
    name: str
    bin: str
    organizationId: str
