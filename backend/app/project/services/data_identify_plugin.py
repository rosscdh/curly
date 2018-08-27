"""
Services that help identify the type of data being sent
"""

import uuid
from apistar import http
from project import plugins
from project.serializers import DataIn


class DataInIdentifyService:
    def __init__(self, request: http.Request):
        self.request = request
        self.payload = request.body.decode('utf-8').strip()

    def identify_data(self):
        return DataIn

    def data(self):
        return DataIn(name='EventLog',
                      request_id=uuid.uuid4(),
                      payload=self.payload)