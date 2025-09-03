from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    'Faz o logout do usuário.'
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    'Faz o cadastro de um novo usuário.'

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
        '''
        form.fields['username'].help_text = 'Usuário'
        form.fields['password1'].help_text = 'TEXTO SENHA 1'
        form.fields['password2'].help_text = 'TEXTO SENHA 2'
        '''

    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
        
    context = {'form': form}
    return render(request, 'users/register.html', context)