from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

user = {"name": "Сергей",
        "midlename": "Александрович",
        "fam": "Куренев",
        "tel": "8-923-346-3366"}


def home(request):
    name = "Куренев Сергей"
    context = {
        "page_title": "Главная",
        "name": "Сергей",
        "surname": "Куренев"

    }
    return render(request, 'Index.html', context)


def about(request):
    result = f"""
                Имя:{user["name"]}<br>
                Отчество:{user["midlename"]}<br>
                Фамилия:{user["fam"]}<br>
                Телефон:{user["tel"]}<br>
            """
    return HttpResponse(result)


def get_item(request, id):
    try:
        item = Item.objects.get(id=id)
        context = {
            "page_title": "Товар",
            "item": item,
        }
        return render(request, 'item.html', context)
    except ObjectDoesNotExist:
        raise Http404


def items_list(request):
    context = {
        "page_title": "Страница товаров",
        "items": Item.objects.all(),
    }
    return render(request, 'items_list.html', context)
