from typing import Annotated
from fastapi import FastAPI, Depends

from smallerwebhexagon.raters import IncodeRater
from smallerwebhexagon.smaller_web_hexagon import Rater
# from smallerwebhexagon.smaller_web_hexagon import SmallerWebHexagon, Rater

app = FastAPI()


@app.get("/{value}")
def root(
    value: float,
    rater: Annotated[Rater, Depends()] = IncodeRater(),
    # app: Annotated[SmallerWebHexagon, Depends()] = SmallerWebHexagon(rater=IncodeRater())
) -> dict[str, float]:
    # descomente se utilizar aplicação ao invés do rater
    # rate, result = rater.rate_and_result(value)
    rate = rater.rate(value)
    result = value * rate
    return {"value": value, "rate": rate, "result": result}
