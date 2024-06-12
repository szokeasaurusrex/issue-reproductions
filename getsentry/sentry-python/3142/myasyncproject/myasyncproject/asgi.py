"""
ASGI config for myasyncproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import asyncio
import os

from django.core.asgi import get_asgi_application
from django.http import HttpResponse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myasyncproject.settings")

application = get_asgi_application()


async def async_view(request):
    print("async_view")
    await asyncio.sleep(0.6)
    return HttpResponse("Hello, world!")


async def error(request):
    await asyncio.sleep(0.6)
    raise Exception("error")


def sync_view_in_asgi(request):
    print("sync_view_in_asgi")
    return HttpResponse("Hello, world!")
