from django.shortcuts import render
from .models import Waifu


def index(request):
	waifus = Waifu.objects.all()
	return render(request, 'index.html', {'waifus': waifus})
