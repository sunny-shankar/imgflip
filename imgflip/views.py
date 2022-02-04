from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import requests
from imgflip.models import MemeModel

## url
URL = "https://api.imgflip.com/get_memes"


def fetch_data_from_api(url):
    """fetch data from api"""
    res = requests.get(url)
    results = res.json()["data"]["memes"]

    return results


def home_view(requests):
    """return all data from db"""
    data_from_database = MemeModel.objects.all()

    return render(requests, "imgflip/home.html", {"results": data_from_database})


def memes_view(requests, pk):
    obj = MemeModel.objects.get(id=pk)
    return render(requests, "imgflip/img.html", {"result": obj})


def populate_db(requests):
    """fetch data from api and write into database"""
    results = fetch_data_from_api(URL)

    for result in results:
        obj = MemeModel(
            name=result["name"],
            url=result["url"],
            width=result["width"],
            height=result["height"],
            box_count=result["box_count"],
        )
        obj.save()
    return redirect(home_view)
