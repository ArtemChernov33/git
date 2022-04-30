from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
context = {}
new_indigrients = {}

def omlet(request):
    servings = int(request.GET.get("servings", 1))
    for product, unit in DATA['omlet'].items():
        rezult = float(unit) * servings
        new_indigrients[product] = '{:.2f}'.format(rezult)
    context['omlet'] = new_indigrients
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get("servings", 1))
    for product, unit in DATA['pasta'].items():
        rezult = float(unit) * servings
        new_indigrients[product] = '{:.2f}'.format(rezult)
    context['pasta'] = new_indigrients
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get("servings", 1))
    for product, unit in DATA['buter'].items():
        rezult = float(unit) * servings
        new_indigrients[product] = '{:.2f}'.format(rezult)
    context['buter'] = new_indigrients
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
