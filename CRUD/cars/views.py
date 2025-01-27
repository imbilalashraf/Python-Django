from django.shortcuts import render, redirect
from cars.forms import AddCarForm
from cars.models import Car


#Create function

def car_data(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)
        # print(form)
        if form.is_valid():
            carName = form.cleaned_data['car_name']
            carModel = form.cleaned_data['car_model']
            carSpeed = form.cleaned_data['car_speed']
            reg = Car(car_name = carName, car_model = carModel, car_speed = carSpeed)
            print(carName)
            print(carModel)
            print(carSpeed)
            reg.save()
        return redirect("/show/")
    else:
        form = AddCarForm()

    carData = Car.objects.all()

    return render(request, 'cars/addAndShow.html', {'form': form, 'Show_data': carData})


#Read function

def show_car_data(request):
    carData = Car.objects.all()
    print(carData)
    return render(request, 'cars/show.html', {'Show_data': carData})


#Update function

def update_data(request, id):
    # print(data)
    if request.method == "POST":
        data = Car.objects.get(pk=id)
        form = AddCarForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    else:
        data = Car.objects.get(pk=id)
        form = AddCarForm(instance=data)
    return render(request, 'cars/update.html', {'form': form})
    


#Delete function

def delete_data(request, id):
    if request.method == "POST":
        data = Car.objects.get(pk = id)
        data.delete()
        return redirect("/show/")
    

