from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Result
from .forms import ContactForm
from django.core.mail import send_mail


# def home(request):
#     return render(request, 'home.html')
#
#
# def main(request):
#     return render(request, 'euromilhoesapp/main.html')
#
#
# def user_info(request):
#     return render(request, 'euromilhoesapp/user_info.html')


def main_view(request):
    return render(request, 'euromilhoesapp/index.html')


def stats_view(request):
    result = Result.objects.all()
    return render(request, 'euromilhoesapp/statistics.html', context={'result': result})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из форы
            name = form.cleaned_data['name']  # тема письма
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                [name],
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect(reverse('euromilhoesapp:index'))  # редирект с помощью функции redirect
        else:
            return render(request, 'euromilhoesapp/contacts.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'euromilhoesapp/contacts.html', context={'form': form})



