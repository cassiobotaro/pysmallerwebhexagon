from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route
from starlette.templating import Jinja2Templates

from smallerwebhexagon.smaller_web_hexagon import SmallerWebHexagon


class StarletteHttpAdapter:
    def __init__(self, hex_app: SmallerWebHexagon, tpl_folder: str = "templates"):
        self.app = hex_app
        self.templates = Jinja2Templates(directory=tpl_folder)
        self.starlette = Starlette(
            routes=[
                Route("/{value}", endpoint=self.root),
            ]
        )

    def root(self, request: Request) -> HTMLResponse:
        value = float(request.path_params["value"])
        rate, result = self.app.rate_and_result(value)
        out = {"out_action": "result", "value": value, "rate": rate, "result": result}
        return self.templates.TemplateResponse(request, "result.html", out)

    async def __call__(self, scope, receive, send):
        await self.starlette(scope, receive, send)
