import json

from django.shortcuts import render
from app1.models import Book, TODO
from django.http import JsonResponse

def index_page(request):
    # Read
    books = Book.objects.all()
    b1 = Book.objects.get(id = 2)
    print(b1)

    # Update
    #b1.author = "А. П. Чехов"
    #b1.save()

    # Create
    #b2 = Book(name = "Мастер и Маргарита", author = "М. А. Булгаков", year = 1940)
    #b2.save()

    # Delete
    #Book.objects.get(name = "Мастер и Маргарита").delete()


    tasks = TODO.objects.all()
    for i in tasks:
        id = '✔' if i.is_done else '❌'
        print(f"{i.text}, выполнение: {id}")

    return render(request, "index.html", context={"text": "Hallownest",
                                                  "data": tasks})

def add(r):
    return JsonResponse({"success": True})

def my_view(r):
    if r.method == 'POST':
        my_data = json.loads(r.body).get('todo', '')
        print(my_data)
        return JsonResponse({'status': 'ok'})