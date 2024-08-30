from fastapi import APIRouter, Depends, status

from src.schemas.subscriptions import STelegramAccountResponse, STelegramAccountsIDResponse, OnlyTelegramSubscribeYear, \
    OnlyTelegramSubscribeMonth
from src.services.subscriptions import SubscriptionsService, get_subscriptions_service

subscription = APIRouter(prefix="/subscription", tags=["Subscription"])


@subscription.post(
    path="/telegram",
    summary="Create telegram subscription account",
    response_model=STelegramAccountResponse,
    responses={status.HTTP_201_CREATED: {"model": STelegramAccountResponse}},
)
async def create_telegram_account(
    telegram_id: int,
    service: SubscriptionsService = Depends(get_subscriptions_service),
) -> STelegramAccountResponse:

    telegram_id = await service.create_telegram_account(telegram_id=telegram_id)

    return STelegramAccountResponse(telegram_id=telegram_id)


@subscription.get(
    path="/telegram",
    summary="Get telegram subscription account",
    response_model=STelegramAccountResponse,
    responses={status.HTTP_200_OK: {"model": STelegramAccountResponse}},
)
async def get_telegram_account(
    telegram_id: int,
    service: SubscriptionsService = Depends(get_subscriptions_service),
) -> STelegramAccountResponse:

    telegram_account = await service.get_telegram_account(telegram_id=telegram_id)

    only_telegram_subscribe_year = telegram_account.only_telegram_subscribe_year
    only_telegram_subscribe_month = telegram_account.only_telegram_subscribe_month

    return STelegramAccountResponse(
        telegram_id=telegram_account.telegram_id,
        subscribe=telegram_account.subscribe,
        only_telegram_subscribe_year=OnlyTelegramSubscribeYear(**only_telegram_subscribe_year.model_dump()) if only_telegram_subscribe_year else None,
        only_telegram_subscribe_month=OnlyTelegramSubscribeMonth(**only_telegram_subscribe_month.model_dump()) if only_telegram_subscribe_month else None,
    )


@subscription.get(
    path="/telegram/users",
    summary="Get telegram subscriptions IDs",
    response_model=STelegramAccountsIDResponse,
    responses={status.HTTP_200_OK: {"model": STelegramAccountsIDResponse}},
)
async def get_telegram_accounts_ids(
    service: SubscriptionsService = Depends(get_subscriptions_service)
) -> STelegramAccountsIDResponse:

    telegram_ids = await service.get_telegram_accounts_ids()

    return STelegramAccountsIDResponse(ids=list(telegram_ids.ids))
