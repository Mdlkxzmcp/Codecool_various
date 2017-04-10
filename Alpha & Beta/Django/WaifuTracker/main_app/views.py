from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Waifu
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import WaifuForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
	waifus = Waifu.objects.all()
	form = WaifuForm()
	return render(request, 'index.html', {'waifus': waifus, 'form': form})


def detail(request, waifu_id):
	waifu = Waifu.objects.get(id=waifu_id)
	return render(request, 'detail.html', {'waifu': waifu})


def profile(request, username):
	user = User.objects.get(username=username)
	waifus = Waifu.objects.filter(user=user)
	return render(request, 'profile.html', {'username': username, 'waifus': waifus})


def post_waifu(request):
	form = WaifuForm(request.POST, request.FILES)
	if form.is_valid():
		waifu = form.save(commit=False)
		waifu.user = request.user
		waifu.save()
	return HttpResponseRedirect('/')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login/')
	else:
		form = UserCreationForm()
		return render(request, 'registration.html', {'form': form})


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print("The account has been disabled!")
			else:
				print("The username and password were incorrect.")
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def heart_waifu(request):
	waifu_id = request.POST.get('waifu_id', None)

	hearts = 0
	if waifu_id:
		waifu = Waifu.objects.get(id=int(waifu_id))
		if waifu is not None:
			hearts = waifu.hearts + 1
			waifu.hearts = hearts
			waifu.save()
	return HttpResponse(hearts)


def search(request):
	search_val = request.GET.get('search', None)

	if search_val is not None:
		results = []
		waifus = Waifu.objects.filter(name__icontains=search_val)
		for waifu in waifus:
			json = {'name': waifu.name, 'link': '/' + str(waifu.id) + '/'}
			results.append(json)
		return JsonResponse({'results':results})
	else:
		return render(request, 'search.html')
