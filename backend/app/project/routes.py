from apistar import Route
from project.views import welcome, datain

routes = [
    Route('/{name}', 'GET', welcome),
    Route('/data', 'POST', datain),
]
