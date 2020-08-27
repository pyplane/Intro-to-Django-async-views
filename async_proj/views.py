from django.http import HttpResponse
import time, asyncio
from movies.models import Movie
from stories.models import Story
from asgiref.sync import sync_to_async

# helper funcs

def get_movies():
    print('prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all the movies!')

def get_stories():
    print('prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all the stories!')

@sync_to_async
def get_movies_async():
    print('prepare to get the movies...')
    time.sleep(2)
    qs = Movie.objects.all()
    print(qs)
    print('got all the movies!')

@sync_to_async
def get_stories_async():
    print('prepare to get the stories...')
    time.sleep(5)
    qs = Story.objects.all()
    print(qs)
    print('got all the stories!')

# views

def home_view(request):
    return HttpResponse('Hello world')

def main_view(request):
    start_time = time.time()
    get_movies()
    get_stories()
    total = (time.time()-start_time)
    print('total: ', total)
    return HttpResponse('sync')
    # total:  7.0053699016571045

async def main_view_async(request):
    start_time = time.time()
    # task1 = asyncio.ensure_future(get_movies_async())
    # task2 = asyncio.ensure_future(get_stories_async())
    # await asyncio.wait([task1, task2])
    await asyncio.gather(get_movies_async(), get_stories_async())
    total = (time.time()-start_time)
    print('total: ', total)
    return HttpResponse('async')

    # total:  5.002896070480347