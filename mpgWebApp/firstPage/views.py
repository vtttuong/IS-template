from django.shortcuts import render
from django.http import JsonResponse
from .models import Match
from django.core import serializers
import json
# Create your views here.

def index(request):
    round = 1
    league ='bundesliga'
    match_list = json.loads(serializers.serialize("json", Match.objects.filter(round=round)))
    context = {
        'round': round,
        'league': league,
        'match_num': len(match_list),
        'matches': match_list,
        }
    # context = {
    #     'league': league,
    #     'round': []
    # }
    # for i in range(1,35):
    #     match_list = json.loads(serializers.serialize("json", Match.objects.filter(round=round)))
    #     context["round"].append({
    #         'round': round,
    #         'match_num': len(match_list),
    #         'matches': match_list,
    #         })
    return render(request,'matches.html', context=context)   

def match_detail(request, league, round, match_id):
    match_object = Match.objects.get(pk = match_id)
    data = serializers.serialize('json', [match_object,])
    struct = json.loads(data)
    match = struct[0]
    context = {
        'match': match,
        'round': round,
        'league': league,
        }
    print(context)
    #return JsonResponse(context)
    return render(request,'match-live.html', context=context)   

def matches(request, league, round):
    match_list = json.loads(serializers.serialize("json", Match.objects.filter(round=round)))
    data = {
        'round': round,
        'league': league,
        'match_num': len(match_list),
        'matches': match_list,

        }
    return JsonResponse(data)
