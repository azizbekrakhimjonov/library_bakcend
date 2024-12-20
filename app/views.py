from django.shortcuts import render
from .models import Yonalish, Malumot


def home(request):
    yonalish_id = request.GET.get('yonalish_id')  # Get the selected category if available
    yonalishlar = Yonalish.objects.all()

    # Filter malumotlar based on the selected yonalish_id, if provided
    if yonalish_id:
        malumotlar = Malumot.objects.filter(yonalish_id=yonalish_id)
    else:
        malumotlar = Malumot.objects.all()

    context = {
        'yonalishlar': yonalishlar,
        'malumotlar': malumotlar
    }

    return render(request, 'index.html', context)
