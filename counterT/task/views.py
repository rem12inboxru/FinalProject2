import asyncio
from matplotlib import pyplot as plt
from tortoise import Tortoise
import requests
from django.shortcuts import render
import datetime
from time import sleep, time
from bs4 import BeautifulSoup
from task.models import Data



async def tortoise_init():
    await Tortoise.init(
        db_url="sqlite:///C:\\SWSetup\\PythonProjectForUniversity\\CounterT\\counterT\\db.sqlite3",
        modules={'models': ['task.models']},
    )
    await Tortoise.generate_schemas()

asyncio.run(tortoise_init())

def parser(x, y):
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    k = 0
    data_two = []
    while k <= y:
        ticker = 'BTC'
        response = requests.get(url)
        bs = BeautifulSoup(response.text, 'lxml')
        price_btc = bs.find('span', 'sc-65e7f566-0 WXGwg base-text')
        btc = float(price_btc.text[1:].replace(',', ''))
        timeevent = datetime.datetime.now()
        print(timeevent)
        data_one = [ticker, btc, x, timeevent]
        print(data_one)
        data_two.append(data_one)
        sleep(x * 60)
        k+=1
    print(data_two)
    return data_two


async def render_up(request):
    for i in parser(1, 10):
        await Data.create(ticker= i[0], lastprice=i[1], timeframe=i[2], timeevent=i[3])
        await Tortoise.close_connections()
    return (request, 'render_up.html')

async def render_pausa(request):
    return (request, 'render_pausa.html' )

async def render_calc(request):
    lastprices = []
    dateevents = []
    timer1 = time()
    data = await Data.all()
    for i in data:
        lastprices.append(i.lastprice)
        dateevents.append(i.timeevent)
    timer2 = time()
    y = timer2 - timer1     # извлечение всех элементов
    z1 = time()
    data1 = await Data.get(id=35)
    z2 = time()
    z = z2 - z1             # извлечение одного элемента
    a1 = time()
    data2 = await Data.filter(lastprice__gte = 68)
    a2 = time()
    a = a2 - a1             # фильтрация по цене больше или равно 68
    b1 = time()
    await Data.all().delete()
    b2 = time()
    b = b2 - b1             # удаление всех объектов
    await Tortoise.close_connections()
    context = {'y': y, 'z': z, 'a': a, 'b': b }
    plt.plot(dateevents, lastprices)
    plt.savefig('static/plot.jpg', format='jpg')


    await Tortoise.close_connections()
    return (request, 'render_calc.html', context)

def render_up1(request):
    a = asyncio.run(render_up(request))
    return render(a[0], a[1])

def render_pausa1(request):
    b = asyncio.run(render_pausa(request))
    return render(b[0], b[1])

def render_calc1(request):
    c = asyncio.run(render_calc(request))
    return render(c[0], c[1], c[2])

# Create your views here.
