from django.http import HttpResponse
from django.db import connection

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola mundo!")

def ejemplo(request):
    return HttpResponse("Esto es un ejemplo de respuesta")

def consulta_sql(request):
    response = ""
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `users`")
        rows = cursor.fetchall()
        for row in rows:
            response += row
    return response