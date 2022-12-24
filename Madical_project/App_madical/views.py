from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from App_madical.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import random
import string
import pandas as pd


# Create your views here.

# @login_required()
def Homepage(request):
    inpt  = request.POST.get('find_by')
    mdata = order.objects.all().order_by('-id')
    # product_name = order.objects.filter(M_name__iexact=inpt)
    return render(request,'Home_pages/home.html',{'data':mdata})
    # x)
    # print(mdata)

def addpage(request):
    return render(request,'add.html')

def datapage(request):
    mt = request.POST
    nm = mt.get('name')
    pr = mt.get('price')
    quan = mt.get('quantity')
    sal = mt.get('saller')
    com = mt.get('company')
    tol = float(pr)*float(quan)
    # gst_ = mt.get('GST_Number')
    # indus = mt.get('industry')
    cus = mt.get('Customer')
    # print(tol)
    # print(com)
    s = order.objects.create(M_name=nm,M_price=pr,M_quantity=quan,M_saller=sal,M_comapany=com,M_amount=tol,customer_name=cus)
    s.save()
    # print(s)
    return  HttpResponseRedirect('/')

def view_content_page(request,a):
    content_data = order.objects.get(id=a)
    return render(request,'view.html',{'D':content_data})


def update_page(request,D):
    val = order.objects.get(id=D)
    # print(val)
    return render(request,'UpdateItems/1Update.html',{'V':val})


def update_page2(request):
    dt = request.POST
    id = dt.get("id")
    nm = dt.get('name')
    pr = dt.get('price')
    qn = dt.get('quantity')
    sel = dt.get('saller') 
    com = dt.get('company')
    # amount = dt.get('total_amount')
    gst_num = dt.get('gest_number')
    indust = dt.get('indus')
    customer_name = dt.get('customer')
    total_amount = float(pr) * float(qn)
    # print("----------------------{}".format(total_amount))
    # print(pr)
    # print(qn)
    # print(amount)
    # gst = dt.get('')
    # to = dt.get('total')
    # tr = order.objects.create(M_name=nm,M_price=pr,M_quantity=qn,M_saller=sel,M_comapany=com)
    tr = order.objects.get(id=id)
    tr.M_name = nm
    tr.M_price = pr
    tr.M_quantity = qn
    tr.M_saller = sel
    tr.M_comapany = com
    tr.M_amount = total_amount
    tr.gst_number = gst_num
    tr.industry_type = indust
    tr.customer_name = customer_name
    # print(tr)
    tr.save()
    return HttpResponseRedirect('/')


def deletepage(request,d):
    dl = order.objects.get(id=d)
    dl1=dl
    dl.delete()
    return render(request,'del.html',{'D1':dl1})

def product_page(request):
    fil = 'Instock/input_instock.html'
    D1 = Instock.objects.all()
    # print(Instock.N_supplier_name)
    # print()
    return render(request,fil,{'D':D1})
    


def enter_product_page(request):
    rt = request.POST
    nm = rt.get('name')
    pr = rt.get('price')
    qn = rt.get('quantity')
    sup = rt.get('supplier')
    nt = Instock.objects.create(N_name=nm,N_price=pr,N_quantity=qn,N_supplier_name=sup)
    nt.save()
    return HttpResponseRedirect('/')


def updateData_page(request):
    h_file = 'UpdateItems/Find_update.html'
    d1 = order.objects.all()
    # print(d1)
    # ln = 0
    # for i in d1.values():
    #     ln +=int(i)
    # print(len(ln))
    return render (request,h_file,{'D1':d1})


def find_and_update(request):
    h_file = 'UpdateItems/Find_update.html'
    sr = request.POST.get('Search')
    # print(sr)
    if(request.method == 'POST'):
        dt = order.objects.filter(M_name__iexact=sr)
        dt1 = order.objects.filter(M_saller__iexact=sr)
        return render(request,h_file,{'data':dt,'sel':dt1,'res':sr})
    else:
        return render(request,h_file,{'res':sr})


def report_page(request):
    h_file = 'Bill_Report/report.html'
    # dt = order.objects.all()
    return render(request,h_file)


def get_report_page(request):
    sum = 0
    h_file = 'Bill_Report/report.html'
    if(request.method == 'POST'):
        st = request.POST.get('start_date')
        et = request.POST.get('end_date')
        dt = order.objects.filter(M_date__gte=st,M_date__lte=et)
        for i in dt.values():
            # print(i['M_amount'])
            sum = sum +i['M_amount']
        # print(sum)
        # df = pd.DataFrame()
        # import pdb;pdb.set_trace()
        # print("DT DATa type :- ",dir(dt))
        return render(request,h_file,{'data':dt,'sum':sum,'start':st,'end':et})
        # df_ = pd.DataFrame(dt.values())
        # if df_ & dt.values():
        #     return render(request,h_file,{'data':dt,'sum':sum,'start':st,'end':et,"DF":df_})
        # else:
        #     return render(request,h_file,{'data':dt,'sum':sum,'start':st,'end':et})

        # print(dir(dt))

        # return render(request,h_file,{'data':dt,'sum':sum,'start':st,'end':et,"DF":df_})
    else:
        return HttpResponseRedirect('/')

def billing_page(request):
    # pr = order.objects.all()
    return render(request,'Bill_Report/Bill.html')

def bill_data_page(request):
    sum = 0
    bil = request.POST.get('generat_bill')
    # print(bil)
    if(request.method == "POST"):
        prd = order.objects.filter(customer_name__iexact=bil)
        for i in prd.values():
            sum = sum +i['M_amount']
        # print(sum)
        return render(request,'Bill_Report/Bill.html',{'pr':prd,'sum':sum})


def delete_page2(request,d):
    dl = order.objects.get(id=d)
    dl1=dl
    dl.delete()
    return render(request,'del.html',{'D1':dl1})


# def find_anything_page(request):
#     inpt  = request.POST.get('find_by')
#     print(inpt)
#     if(request.method == 'POST'):
#             product_name = order.objects.filter(M_name__iexact=inpt)
#             company_name = order.objects.filter(M_comapany__iexact=inpt)
#             total_amount = order.objects.filter(M_amount__iexact=inpt)
#             customer_ = order.objects.filter(customer_name__iexact=inpt)
#             # for i in product_name.values():
#             #     print(i)
#             return render(request,'Home_pages/search_home.html',{'product':product_name,'company':company_name,'total':total_amount,'customer':customer_})

def Search_item(reqest):
    saerch_item = reqest.GET.get("search_item")
    dt = order.objects.filter(M_name__iexact=saerch_item)
    print(dt)
    dt1 = order.objects.filter(M_saller__iexact=saerch_item)
    return render(reqest,'Home_pages/home.html',{'data':dt,"data1":dt1})


def the_pagination(reqest):
    contact_list = order.objects.all()
    paginator = Paginator(contact_list, 2)
    print("@@@@@ ;- {}".format(paginator))

    




