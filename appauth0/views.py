from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from autentication.auth0backend import getRole

@login_required
def landing_page(request):
    role = getRole(request)
    if role in ["Asesor Bancario", "Cliente"]:
        context = {
            'username': request.user.username,
            'role': role
        }
        # Asegúrate de especificar la ruta completa dentro del directorio de templates
        return render(request, 'auth0/landing_page.html', context)
    else:
        return HttpResponse("Unauthorized User", status=401)