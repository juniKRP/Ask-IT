import json

from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    names = ("bob")

    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20, 80),
            "url": "https://example.com",
        })

    context = {}
    context["items"] = items
    context["items_json"] = json.dumps(items)

    return render(request, 'ask_questions.html', context)