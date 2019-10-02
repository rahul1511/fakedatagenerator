from django.shortcuts import render
from django.http import HttpResponse
from.models import FakeGen
import faker

# Create your views here.
f=faker.Faker()
def fake_view(request):
    for i in range(100):
        name=f.name()
        email=f.email()
        location=f.random_element(elements=("hyd","pune","bang","delhi"))
        dob=f.date_time()
        salary=f.random_element(elements=(25645.25,286754.25,302564.25,32856.65))

        data=FakeGen(
            name=name,
            email=email,
            location=location,
            dob=dob,
            salary=salary,)
        data.save()
    return HttpResponse("data Inserted sucessfully......")
def FetchData(request):
    Fdata=FakeGen.objects.all()
    return render(request,'fakedata.html',{'Fdata':Fdata})


