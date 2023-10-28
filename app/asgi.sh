#!/usr/bin/env bash

# uvicorn is good for light application with --reload
uvicorn --ws auto  --host 0.0.0.0 --port 9090 --reload hello_django.asgi:application
