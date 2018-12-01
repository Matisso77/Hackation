import json
from BeerTracker.populartimes import prepareForMap
from django.http import HttpResponse


def index(request):
    return HttpResponse("Siemano")


def add(request):
    try:
        received_json_data = json.loads(request.body)
        return HttpResponse(received_json_data)
    except Exception as ex:
        return HttpResponse(ex)


def getFak(request):
    # get id from database
    mocklist = ["ChIJh7xFOrjDD0cRATauodAEmuE"]
    jsondata = prepareForMap(mocklist)
    return HttpResponse(jsondata)
