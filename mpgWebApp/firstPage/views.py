from django.shortcuts import render
from django.http import JsonResponse
from .models import Match
from django.core import serializers
from django.db.models import Avg, Max, Min, Q
from django.forms.models import model_to_dict

import json
# Create your views here.

def index(request):
    round = 1
    series ='Bundesliga'
    match_list = json.loads(serializers.serialize("json", Match.objects.filter(series=series,round=round)))
    best_match = Match.objects.filter(series=series,round=round).get(Q(homename='Bayern Munich')|Q(awayname='Bayern Munich'))
    round_max = Match.objects.filter(series=series).aggregate(Max('round'))
    context = {
        'round': round,
        'round_list': range(2, round_max['round__max'] + 1),
        'series': series,
        'series_slug': series.lower().replace(' ','-'),
        'match_num': len(match_list),
        'matches': match_list,
        'best_match': best_match,
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

def match_detail(request, series, round, match_id):
    match_object = Match.objects.get(pk = match_id)
    data = serializers.serialize('json', [match_object,])
    struct = json.loads(data)
    match = struct[0]
    context = {
        'match': match,
        'round': round,
        'series': series,
        }
    #return JsonResponse(context)
    return render(request,'match-live.html', context=context)   

def matches(request, series, round):
    series = convert_slug(series)
    match_list = json.loads(serializers.serialize("json", Match.objects.filter(series=series, round=round)))
    star_team = ''
    if (series=='Premier League'):
        star_team = 'Manchester United'
    elif (series=='Bundesliga'):
        star_team = 'Bayern Munich'
    elif (series=='La Liga'):
        star_team = 'Real Madrid'
    elif (series=='Serie A'):
        pstar_team = 'Juventus'
    best_match = Match.objects.filter(series=series,round=round).get(Q(homename=star_team)|Q(awayname=star_team))
    best_match_obj = serializers.serialize('json', [ best_match, ])
    data = {
        'round': round,
        'match_num': len(match_list),
        'matches': match_list,
        'best_match': json.loads(best_match_obj)[0]
        }
    return JsonResponse(data)

def convert_slug(series):
    res = ''
    for i in series.split('-'):
        res += i.capitalize() + ' '
    return res[:len(res)-1]
