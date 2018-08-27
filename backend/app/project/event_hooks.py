from apistar import http
from project.services import DataInIdentifyService


class DataInIdentifyHook:
    def on_request(self, request: http.Request, exc: Exception):
        if request.method in ['POST']:
            request.dataid_service = DataInIdentifyService(request=request)