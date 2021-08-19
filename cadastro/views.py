from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cadastro.forms import PessoaForm
@login_required
def cadastro (request):
    form = PessoaForm(data=request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'cadastro/index.html', { 'form': form })