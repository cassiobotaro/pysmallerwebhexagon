from fastapi import FastAPI

from smallerwebhexagon.raters import IncodeRater
from smallerwebhexagon.smaller_web_hexagon import SmallerWebHexagon

app = FastAPI()
_hex = SmallerWebHexagon(rater=IncodeRater())


@app.get("/{value}")
def root(
    value: float,
) -> dict[str, float]:
    rate, result = _hex.rate_and_result(value)
    return {"value": value, "rate": rate, "result": result}
