from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()

    #Exibir usuários já cadastrados em um nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuario/usuarios.html',usuarios)
    