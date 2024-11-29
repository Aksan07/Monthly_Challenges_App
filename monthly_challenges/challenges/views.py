from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

monthly_challenges_dic = {
    "january":"Learn",
    "february":"Work Hard",
    "march": "Pray Hard",
    "april": "Keep Going",
    "may":"Fight On",
    "june":"Understand Defeat",
    "july":"Become Better",
    "august":"Live for God",
    "september": "Stay Humble", 
    "october":"He didnot abandon you",
    "november":"Sacrifice the evil in your hurt",
    "december":"Kill Lust",
                      }

# Create your views here.

def monthly_challenges_int(request,month):
    return HttpResponse(month)

def monthly_challenges(request,month):
    try:
        challenge_text = monthly_challenges_dic[month]
        return HttpResponse(challenge_text)
    except KeyError:
        return HttpResponseNotFound("Believe Man, God Bless Your Soul")
