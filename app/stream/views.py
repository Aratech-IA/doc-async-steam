from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
import asyncio
# Create your views here.


async def index(request):
    return HttpResponse("Hello, async Django!")


async def stream_text():
    for i in range(100):
        await asyncio.sleep(0.1)
        yield f"{i} toto"


async def stream_messages_view(request):
    return StreamingHttpResponse(
        streaming_content=stream_text(),
        content_type="text/event-stream",
    )
