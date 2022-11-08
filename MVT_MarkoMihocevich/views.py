from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context




def vista_saludo(request):
    
    archivo = open(r"C:\Users\MARKO\Desktop\MVTMARKOMIHOCEVICH\MVT_MarkoMihocevich\MVT_MarkoMihocevich\templates\plantilla.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context()

    documento = plantilla.render(contexto)
    
    
    return HttpResponse (documento)


def dia_hoy(request):
       
       hoy = datetime.now()

       respuesta = f"""Hoy es {hoy}"""

       return HttpResponse(respuesta)
