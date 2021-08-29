from django.shortcuts import render , redirect

from .forms import DocForm


def index_view(request):
    form = DocForm()
    if request.method == 'POST':
        form = DocForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('/')
    return render(request, 'text/index.html', {'form': form})
