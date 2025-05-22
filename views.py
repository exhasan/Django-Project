from django.shortcuts import render, redirect
from .forms import PropertyForm
from .models import Property
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def properties(request):
    all_properties = Property.objects.all()
    query = request.GET.get('q')
    location = request.GET.get('location')

    if query:
        all_properties = all_properties.filter(title__icontains=query)
    if location:
        all_properties = all_properties.filter(details__icontains=location)  # Change to .filter(location__icontains=location) if you have a location field

    return render(request, 'properties.html', {'properties': all_properties})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('properties')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})
@login_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    # Optionally: check if request.user is the owner
    if request.method == 'POST':
        property.delete()
        return redirect('properties')
    return render(request, 'delete_property_confirm.html', {'property': property})

@login_required
def liked_properties(request):
    all_properties = Property.objects.all()
    return render(request, 'liked_properties.html', {'properties': all_properties})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('properties')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})