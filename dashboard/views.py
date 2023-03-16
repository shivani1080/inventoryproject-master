from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Issued_Items
from django.contrib.auth.decorators import login_required
from .forms import ProductForm,orderform
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    items=Issued_Items.objects.all()
    product=Product.objects.all()
    items_count = items.count()
    product_count = product.count()
    workers_count =User.objects.all().count()
    
    if request.method=='POST':
        form=orderform(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboardindex')
    else:
        form=orderform()
    context={
        'items':items,
        'form':form,
        'product':product,
        'product_count': product_count,
        'workers_count': workers_count,
        'items_count': items_count,
        

    }
    return render(request,'dashboard/index.html',context)
@login_required
def staff(request):
    workers=User.objects.all()
    workers_count = workers.count()
    items_count =Issued_Items.objects.all().count()
    product_count =Product.objects.all().count()
    
    context= {
        'workers':workers,
        'workers_count': workers_count,
        'items_count': items_count,
        'product_count': product_count,
    }
    return render(request,'dashboard/staff.html',context)
@login_required
def staff_detail(request,pk):
    workers=User.objects.get(id=pk)
    context={
        'workers':workers
    }

    return render(request,'dashboard/staff_detail.html',context)
@login_required
def product(request):
    items=Product.objects.all()
    product_count = items.count()
    #items=Product.objects.raw('SELECT * FROM dashboard_product')
    workers_count =User.objects.all().count()
    items_count =Issued_Items.objects.all().count()
    
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboardproduct')
    else:
        form=ProductForm()
    context={
        'items':items,
        'form':form,
        'workers_count': workers_count,
        'items_count': items_count,
        'product_count': product_count,
        
    }
    return render(request,'dashboard/product.html',context)   
@login_required
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboardproduct')
    return render(request,'dashboard/product_delete.html') 
@login_required
def product_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboardproduct')
    else:
        form=ProductForm(instance=item)
    context={
        'form':form

    }
    return render(request,'dashboard/product_update.html',context)

@login_required
def issued_items(request):
 items=Issued_Items.objects.all()
 items_count = items.count()
 workers_count =User.objects.all().count()
 product_count =Product.objects.all().count()
 context={
     'items':items,
     'workers_count': workers_count,
     'items_count': items_count,
     'product_count': product_count,
 }

 return render(request,'dashboard/issueditems.html',context)