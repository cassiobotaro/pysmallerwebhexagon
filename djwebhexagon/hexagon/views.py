from django.http import Http404
from django.shortcuts import render

from .models import Rate


def index(request, slug, value):
    try:
        rate = Rate.objects.get(slug=slug).value
        result = rate * value
    except Rate.DoesNotExist:
        raise Http404("Rate does not exist")
    return render(
        request, "hexagon/index.html", {"value": value, "rate": rate, "result": result}
    )
