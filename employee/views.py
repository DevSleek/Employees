import json

import httpx
import asyncio

from django.http import JsonResponse
from django.conf import settings

from employee.models import Employee


async def get_employees(request):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            settings.EXTERNAL_API_CONFIG['URL'],
            json={
                "Request_id": settings.EXTERNAL_API_CONFIG['REQUEST_ID'],
                "ClubId": "59115d1e-9052-11eb-810c-6eae8b56243b",
                "Method": "GetSpecialistList",
                "Parameters": {"ServiceId": ""}
            },
            auth=(settings.EXTERNAL_API_CONFIG['LOGIN'], settings.EXTERNAL_API_CONFIG['PASSWORD'])
        )

    data = response.json()
    for item in data.get('specialists', []):
        employees = Employee.objects.create(
            id=item.get('id'),
            name=item.get('name'),
            last_name=item.get('last_name'),
            phone=item.get('phone'),
            image_url=item.get('image_url'),
        )

    return JsonResponse(employees, safe=False)
