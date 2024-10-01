# django gevent gunicorn test

Emulate huge django gevent app that loads 10 seconds (see `time.sleep(10)` in code) running on gunicorn.

    --worker-class=gevent
    --workers=2
    --worker-connections=50
    --max-requests=100
    --timeout=5

For test runs 180 request, that should fit 200 requests before all workers restart (2 workers x 100 max_requests).

## Setup

    pip install -r requirements.txt

## Start App

    bash run.sh

## Test

    python test.py

## Test Results

No warm:

    num of requests: 180
    num of error: 20
    num duration from 0ms to 20ms: 33
    num duration from 20ms to 50ms: 57
    num duration from 50ms to 100ms: 56
    num duration from 100ms to 200ms: 13
    num duration from 200ms to 500ms: 1
    num duration from 500ms to 1000ms: 0
    num duration from 1000ms to 2000ms: 0
    num duration from 2000ms to 5000ms: 0
    num duration from 5000ms to 10000ms: 0
    num duration more 10000ms: 20

Warm one worker:

    num of requests: 180
    num of error: 2
    num duration from 0ms to 20ms: 50
    num duration from 20ms to 50ms: 92
    num duration from 50ms to 100ms: 15
    num duration from 100ms to 200ms: 2
    num duration from 200ms to 500ms: 0
    num duration from 500ms to 1000ms: 0
    num duration from 1000ms to 2000ms: 0
    num duration from 2000ms to 5000ms: 0
    num duration from 5000ms to 10000ms: 19
    num duration more 10000ms: 2

Warm all workers:

    num of requests: 180
    num of error: 0
    num duration from 0ms to 20ms: 62
    num duration from 20ms to 50ms: 66
    num duration from 50ms to 100ms: 35
    num duration from 100ms to 200ms: 15
    num duration from 200ms to 500ms: 2
    num duration from 500ms to 1000ms: 0
    num duration from 1000ms to 2000ms: 0
    num duration from 2000ms to 5000ms: 0
    num duration from 5000ms to 10000ms: 0
    num duration more 10000ms: 0
