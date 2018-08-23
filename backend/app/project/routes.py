from apistar import Route
from project.views import welcome, datain

routes = [
    Route('/', 'GET', welcome),
    Route('/data', 'POST', datain),
]
