from smallerwebhexagon.smaller_web_hexagon import SmallerWebHexagon
from smallerwebhexagon.raters import IncodeRater
from smallerwebhexagon.starlette_http_adapter import StarletteHttpAdapter
import uvicorn

hex = SmallerWebHexagon(rater=IncodeRater())
app = StarletteHttpAdapter(hex)

uvicorn.run(app, port=9292)
