from django.shortcuts import render
from django.http import HttpResponse
import asyncio


async def index(request):
    await asyncio.sleep(5)
    return HttpResponse("Hello, async Django!")