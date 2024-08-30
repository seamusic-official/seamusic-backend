from fastapi import APIRouter, Depends, status

from src.models.auth import User
from src.schemas.licenses import (
    License,
    SMyLicensesResponse,
    SLicensesResponse,
    SLicenseResponse,
    SCreateLicenseResponse,
    SCreateLicenseRequest,
    SEditLicensesResponse,
    SLicensesDeleteResponse,
    SEditLicenseRequest,
)
from src.services.licenses import LicensesService, get_licenses_service
from src.utils.auth import get_current_user

licenses = APIRouter(prefix="/licenses", tags=["Licenses"])


@licenses.post(
    path="/my",
    summary="Packs by current user",
    response_model=SMyLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SMyLicensesResponse}},
)
async def get_my_licenses(
    user: User = Depends(get_current_user),
    service: LicensesService = Depends(get_licenses_service),
) -> SMyLicensesResponse:

    response = await service.get_user_licenses(user_id=user.id)

    licenses_ = list(map(
        lambda license_: License(
            id=license_.id,
            title=license_.title,
            picture_url=license_.picture_url,
            description=license_.description,
            file_path=license_.file_path,
            co_prod=license_.co_prod,
            prod_by=license_.prod_by,
            playlist_id=license_.playlist_id,
            user_id=license_.user_id,
            beat_pack_id=license_.beat_pack_id,
            price=license_.price,
            created_at=license_.created_at,
            updated_at=license_.updated_at,
        ),
        response.licenses
    ))

    return SMyLicensesResponse(licenses=licenses_)


@licenses.get(
    path="/",
    summary="Get all licenses",
    response_model=SLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesResponse}},
)
async def all_licenses(service: LicensesService = Depends(get_licenses_service)) -> SLicensesResponse:

    response = await service.get_all_licenses()

    licenses_ = list(map(
        lambda license_: License(
            id=license_.id,
            title=license_.title,
            picture_url=license_.picture_url,
            description=license_.description,
            file_path=license_.file_path,
            co_prod=license_.co_prod,
            prod_by=license_.prod_by,
            playlist_id=license_.playlist_id,
            user_id=license_.user_id,
            beat_pack_id=license_.beat_pack_id,
            price=license_.price,
            created_at=license_.created_at,
            updated_at=license_.updated_at,
        ),
        response.licenses
    ))
    return SLicensesResponse(licenses=licenses_)


@licenses.get(
    path="/{license_id}",
    summary="Get license by id",
    response_model=SLicenseResponse,
    responses={status.HTTP_200_OK: {"model": SLicenseResponse}},
)
async def get_one(
    license_id: int,
    service: LicensesService = Depends(get_licenses_service),
) -> SLicenseResponse:

    license_ = await service.get_one(license_id=license_id)

    return SLicenseResponse(
        id=license_.id,
        title=license_.title,
        picture_url=license_.picture_url,
        description=license_.description,
        file_path=license_.file_path,
        co_prod=license_.co_prod,
        prod_by=license_.prod_by,
        playlist_id=license_.playlist_id,
        user_id=license_.user_id,
        beat_pack_id=license_.beat_pack_id,
        price=license_.price,
        created_at=license_.created_at,
        updated_at=license_.updated_at,
    )


@licenses.post(
    path="/new",
    summary="Add a file for new beat",
    response_model=SCreateLicenseResponse,
    responses={status.HTTP_200_OK: {"model": SCreateLicenseResponse}},
)
async def add_license(
    data: SCreateLicenseRequest,
    user: User = Depends(get_current_user),
    service: LicensesService = Depends(get_licenses_service),
) -> SCreateLicenseResponse:

    license_id = await service.add_license(
        title=data.title,
        price=data.price,
        user_id=user.id,
        description=data.description,
    )

    return SCreateLicenseResponse(id=license_id)


@licenses.put(
    path="/{license_id}/update",
    summary="Edit license by id",
    response_model=SEditLicensesResponse,
    responses={status.HTTP_200_OK: {"model": SEditLicensesResponse}},
)
async def update_license(
    license_id: int,
    data: SEditLicenseRequest,
    user: User = Depends(get_current_user),
    service: LicensesService = Depends(get_licenses_service),
) -> SEditLicensesResponse:

    license_id = await service.update_license(
        license_id=license_id,
        user_id=user.id,
        title=data.title,
        description=data.description,
        price=data.price,
    )

    return SEditLicensesResponse(id=license_id)


@licenses.delete(
    path="/{license_id}/delete",
    summary="Create new licenses",
    response_model=SLicensesDeleteResponse,
    responses={status.HTTP_200_OK: {"model": SLicensesDeleteResponse}},
)
async def delete_licenses(
    license_id: int,
    user: User = Depends(get_current_user),
    service: LicensesService = Depends(get_licenses_service)
) -> SLicensesDeleteResponse:

    await service.delete_license(license_id=license_id, user_id=user.id)
    return SLicensesDeleteResponse()
