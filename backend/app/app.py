from apistar import ASyncApp
from project.routes import routes

app = ASyncApp(routes=routes)
