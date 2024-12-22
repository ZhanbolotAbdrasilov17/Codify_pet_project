from django.shortcuts import render
from .models import *

def home(request):
    up_part_icons = UpPartField.objects.all()
    context = {"up_part_icons": up_part_icons,}
    return render(request, 'index.html', context)