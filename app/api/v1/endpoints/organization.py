from . import session
from fastapi import APIRouter
from app.models.organization import Organization
from app.schemas.organization import OrganizationSchema

router = APIRouter()


@router.get("/")
async def get_organizations():
    query = session.query(Organization).all()
    return query


@router.get("/{organization_id}")
async def get_organization(organization_id: int):
    query = session.query(Organization).filter(Organization.id == organization_id).first()
    if query:
        return query
    return {"error": "Not Found"}


@router.post("/")
async def create_organization(organization: OrganizationSchema):
    query = Organization(name=organization.name, bin=organization.bin, organizationId=organization.organizationId)

    for i in session.query(Organization).all():
        if i.name == organization.name:
            return {"error": "A organization with this name has already been created"}

    session.add(query)
    session.commit()

    last_id = query.id
    organization = organization.dict()

    return {**organization, "id": last_id}


@router.put("/{organization_id}")
async def update_organization(organization_id:int, organization: OrganizationSchema):
    query = session.query(Organization).filter(Organization.id == organization_id).first()
    for i in session.query(Organization).all():
        if i.name == organization.name and i.id != query.id:
            return {"error": "A organization with this name has already been created"}
    if query:
        query.name = organization.name
        query.bin = organization.bin
        query.organizationId = organization.organizationId
        return {"message": "Organization ({}) updated".format(query.name)}
    return {"error": "Not Found"}


@router.delete("/{organization_id}")
async def delete_organization(organization_id:int):
    query = session.query(Organization).filter(Organization.id == organization_id).first()
    if query:
        session.delete(query)
        session.commit()
        return {"message": "Organization ({}) deleted".format(query.name)}
    return {"error": "Not Found"}
