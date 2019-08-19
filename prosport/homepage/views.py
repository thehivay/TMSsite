from django.shortcuts import render

# Create your views here. Здесь происходит вся бизнес логика, в которой делается выборка из базы данных,
#                         чтоб подготовить вывод ее в шаблоне .html


def index(request):
    return render(request, 'homepage/home.html')


def address(request):
    return render(request, 'homepage/address.html', {'addresses': ['Минск, пр-т Независимости 93/2, +375(29)444-44-44',
                                                                   'Минск, пр-т Дзержинского 92, +375(33)904-25-44',
                                                                   'Минск, пр-т Партизанский 150А, +375(44)714-27-97',
                                                                   'Минск, ул. Ленинградская 5, +375(44)714-18-47']})

