from django.http import HttpResponse, JsonResponse
from django.db import connection

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola mundo!")

def ejemplo(request):
    return HttpResponse("Esto es un ejemplo de respuesta")

def consulta_sql(request):
    data = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `users`")
        columns = [col[0] for col in cursor.description] 
        rows = cursor.fetchall()
        for row in rows:
            data.append(dict(zip(columns, row))) 

    return JsonResponse(data, safe=False)