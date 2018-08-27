from apistar import ASyncApp, App
from project.routes import routes
from project.event_hooks import DataInIdentifyHook


app = ASyncApp(routes=routes,
               event_hooks=[DataInIdentifyHook])
