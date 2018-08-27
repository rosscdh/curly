import json
import typing
from apistar import http
from project.serializers import DataIn


def welcome(name: str=None) -> typing.Dict:
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def datain(request: http.Request) -> http.JSONResponse:
    data = DataIn(name='EventLog',
                  request_id='fd',
                  payload=request.body.decode('utf-8').strip())

    headers = {'Vary': 'Accept-Language'}
    return http.JSONResponse(data,
                             status_code=200,
                             headers=headers)
