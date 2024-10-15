from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
from django.contrib import messages
def index(request):
    allprd = []
    allCat = Product.objects.values('category')
    # print(allCat)
    cats = {item['category'] for item in allCat}
    for cat in cats:
        mypdt = Product.objects.filter(category=cat)
        n = len(mypdt)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        allprd.append([mypdt,range(1,nSlide),nSlide])
    value = {'allpdt': allprd}
    return render(request,"shop/index.html",value)


def SearchMatch(query,item):
    if query in item.name.lower() or query in item.description.lower() or query in item.category.name.lower():
        return True
    else:
        return False


def Search(request):
    query=request.GET.get('search').lower()
    allprd = []
    allCat = Product.objects.values('category')
    # print(allCat)
    cats = {item['category'] for item in allCat}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        mypdt=[item for item in prod if SearchMatch(query,item)]
        n = len(mypdt)
        print(n)
        nSlide = n // 4 + ceil((n / 4) - (n // 4))
        if len(mypdt)!=0:
            allprd.append([mypdt,range(1,nSlide),nSlide])
    value = {'allpdt': allprd}
    if len(allprd)==0 or len(query)<4:
        value={'msg':"The Item Is Not Avalabile Right Now! "}
    return render(request,"shop/Search.html",value)


def About(request):
    messages.success(request,"Welcome to the About ")
    return render(request,"shop/About.html")
def Faq(request):
    return render(request,"shop/Faq.html") 

def contact_form_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('description')
        phone = request.POST.get('phone')

        x = Contact(name=name, email=email, description=desc, phone=phone)
        x.save()

        return render(request,"shop/Contact_success.html")
    else:
        return render(request,"shop/Contact.html")

def product_list(request):
    products = Product.objects.all()
    return render(request,"shop/product_list.html",{"Products": products})




def tracking(request):
    if request.method == "POST":
        orderid=request.POST.get('OrderID','')
        email=request.POST.get("Email","")
        # return HttpResponse (f"{orderid}{email}")
        try:
            order=Orders.objects.filter(order_id=orderid,email=email)
            if order.exists():
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestap})
                response=json.dumps([updates,order[0].items_json],default=str)
                print(response)

                return HttpResponse(response)
            else:
                return HttpResponse('{}')
                
        except Exception as e:
            return HttpResponse (f"Error {e}")

        
    return render(request,'shop/Tracker.html')


def Product_view(request,myid):
    mypdt = Product.objects.filter(id=myid)
    return render(request,"shop/Product_view.html",{'products':mypdt[0]})


def Checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson','')
        print(items_json)
        name = request.POST.get('name1') +" "+request.POST.get('name2')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address1') +" "+ request.POST.get('address2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')

        # Create a Contact instance
        order = Orders(name=name, email=email, phone=phone, address=address, state=state, zip_code=zip_code,country=country,items_json=items_json)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The Order Has Been Placed")
        update.save()
        # id = order.order_id
        return redirect('order_success', order_id=order.order_id)
    else:
        return render(request, "shop/Checkout.html")
    # return render(request,"shop/Checkout.html")

def order_success(request, order_id):
    order = Orders.objects.filter(order_id=order_id)
    thank=True
    return render(request, 'shop/order_success.html', {'order': order[0],'thank':thank})