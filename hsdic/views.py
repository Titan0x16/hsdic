from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import DeckCodeForm
from random import choice
from .images2async import main
from time import sleep
 
def index(request):

    if request.method == "POST":
    	deckform = DeckCodeForm()
    	code_string = request.POST.get("deck_code") #стока из формы

    	file_name = main(code_string)
    	# images = ['EX1_001.png', 'EX1_001.png', 'EX1_002.png', 'EX1_004.png', 'EX1_006.png', ]

    	# try:
    	# 	file_name = images[int(code_string)]
    	# except:
    	# 	file_name = images[0]

    	image_link = "hsdic/{}".format(file_name)

    	return render(request, "hsdic/index.html", {"deckform": deckform, 'code': file_name, 'img': image_link,})
    else:
    	deckform = DeckCodeForm()
    	code_string = 'placeholder'
    	image_link = "hsdic/big_placeholder.jpg"
    	return render(request, "hsdic/index.html", {"deckform": deckform, 'code': code_string, 'img': image_link,})

    # code_string = 'AAECAaoIAt6CA5ybAw7FA9sD/gPjBdAHpwiTCeKJA4yUA7WYA8aZA/SZA6+nA8qrAwA='

    # return render(request, "hsdic/index.html", context={'img': image_link, 'code': code_string})

def signup(request):
    image_link = "hsdic/hslogo.png"
    return render(request, 'hsdic/signup.html', {'img': image_link,})

def signup_user(request):

    user_name = request.POST["user_name"]

    print(user_name)
    return HttpResponseRedirect("/")

def check_username(request):
    if request.method == "GET":
        user_name = request.GET.get("user_name")
        print("----->>>")
        print(user_name)
        print("----->>>")
        # names = ['HERONDOS', 'LOPATA'] #Проверить работает ли со списком
        # if user_name in names:
        #     return HttpResponse('no', content_type='text/html')
        # else:
        #     return HttpResponse('ok', content_type='text/html')
        names = {'1': 'EX1_001', '2': 'EX1_002', '3': 'EX1_004', '4': 'EX1_006', }
        sleep(3)
        print(names[user_name])
        return HttpResponse(names[user_name], content_type='text/html')

    else:
        return HttpResponse('NOT GET Request', content_type='text/html')

def check_code(request):
    if request.method == "GET":
        deck_code = request.GET.get("deck_code")
        deck_language = request.GET.get("deck_language")
        print("")
        print(deck_code, deck_language)
        print("")
        file_name = main(deck_code, deck_language)
        image_link = "hsdic/{}".format(file_name)
        sleep(1)
        return HttpResponse(image_link, content_type='text/html')

    else:
        return HttpResponse('NOT GET Request', content_type='text/html')