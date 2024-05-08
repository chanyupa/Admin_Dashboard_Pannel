from django.shortcuts import render, redirect
from .models import Data_Entry_Pannel, Customer_Table, Banner_Table, Payment_Table, Delifee_Table, Region_table, Product_Table, Information_Table, Category_Table,Brand_Table, Order_table
# Create your views here.
def home(request):
    return render(request, "home.html")

def border(request):
    return render(request, "border.html")

def customer(request):
    return render(request, "customer.html")

def banner(request):
    return render(request, "banner.html")

def payment(request):
    return render(request, "payment.html")

def delifee(request):
    return render(request, "delifee.html")

def region(request):
    return render(request, "region.html")

def product(request):
    return render(request, "product.html")

def information(request):
    return render(request, "information.html")

def cartegory(request):
    return render(request, "cartegory.html")

def brand(request):
    return render(request, "brand.html")

def order(request):
    return render(request, "order.html")


def dataentrypannel(request):
    data = Data_Entry_Pannel()
    data.bookingcode = request.POST.get("bookingcode")
    data.passengername = request.POST.get("passengername")
    data.prize = request.POST.get("prize")
    data.issueby = request.POST.get("issueby")
    data.eticketnumber =request.POST.get("eticketnumber")
    data.passportnumber =request.POST.get("passportnumber")
    data.ticketfees = request.POST.get("ticketfees")
    data.save()
    return render(request, "home.html", {"dataentry": data})

def customertable(request):
    data = Customer_Table()
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.email = request.POST.get("email")
    data.phone = request.POST.get("phone")
    data.createdat =request.POST.get("createdat")
    data.save()
    return render(request, "home.html", {"customer_1": data} )
def retrieve_customertable(request):
    data = Customer_Table.objects.raw("select * from main_app_customer_table where name != 'Remove' ") 
    return render(request, "home.html", {"customer": data})


def bannertable(request):
    data = Banner_Table()
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return render(request, "home.html", {"banner_1": data} )
def retrieve_bannertable(request):
    data = Banner_Table.objects.raw("select * from main_app_banner_table where name != 'Remove' ") 
    return render(request, "home.html", {"banner": data})


def paymenttable(request):
    data = Payment_Table()
    data.id = request.POST.get("id")
    data.paymenttype = request.POST.get("paymenttype")
    data.phonenumber = request.POST.get("phonenumber")
    data.createdat = request.POST.get("createdat")
    data.save()
    return render(request, "home.html", {"payment_1": data} )
def retrieve_paymenttable(request):
    data = Payment_Table.objects.raw("select * from main_app_payment_table where paymenttype != 'Remove' ") 
    return render(request, "home.html", {"payment": data})


def delifeetable(request):
    data = Delifee_Table()
    data.id = request.POST.get("id")
    data.regionname = request.POST.get("regionname")
    data.township = request.POST.get("township")
    data.deliveryfees = request.POST.get("deliveryfees")
    data.status = request.POST.get("deliveryfees")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return render(request, "home.html", {"delifee_1": data} )
def retrieve_delifeetable(request):
    data = Delifee_Table.objects.raw("select * from main_app_delifee_table where deliveryfees != 'Remove' ") 
    return render(request, "home.html", {"delifee": data})



def regiontable(request):
    data = Region_table()
    data.id = request.POST.get("id")
    data.regionname = request.POST.get("regionname")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return render(request, "home.html", {"region_1": data} )
def retrieve_regiontable(request):
    data = Region_table.objects.raw("select * from main_app_region_table where regionname != 'Remove' ") 
    return render(request, "home.html", {"region": data})


def producttable(request):
    data = Product_Table()
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.price = request.POST.get("price")
    data.stock = request.POST.get("stock")
    data.category = request.POST.get("category")
    data.brand = request.POST.get("brand")
    data.createdat = request.POST.get("createdat")
    data.save()
    return render(request, "home.html", {"product_1": data} )
def retrieve_producttable(request):
    data = Product_Table.objects.raw("select * from main_app_product_table where stock != 'Remove' ") 
    return render(request, "home.html", {"product": data})

def informationtable(request):
    data = Information_Table()
    data.id = request.POST.get("id")
    data.content = request.POST.get("content")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return render(request, "home.html", {"information_1": data} )
def retrieve_informationtable(request):
    data = Information_Table.objects.raw("select * from main_app_information_table where updatedat != 'Remove' ") 
    return render(request, "home.html", {"information": data})


def categorytable(request):
    data = Category_Table()
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return render(request, "home.html", {"category_1": data} )
def retrieve_categorytable(request):
    data = Category_Table.objects.raw("select * from main_app_category_table where createdat != 'Remove' ") 
    return render(request, "home.html", {"category": data})


def brandtable(request):
    data = Brand_Table()
    data.id = request.POST.get("id")
    data.categoryname = request.POST.get("categoryname")
    data.brandname = request.POST.get("brandname")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return render(request, "home.html", {"brand_1": data} )
def retrieve_brandtable(request):
    data = Brand_Table.objects.raw("select * from main_app_brand_table where brandname != 'Remove' ") 
    return render(request, "home.html", {"brand": data})


def ordertable(request):
    data = Order_table()
    data.orderid = request.POST.get("orderid")
    data.customer = request.POST.get("customer")
    data.status = request.POST.get("status")
    data.orderdate = request.POST.get("orderdate")
    data.save()
    return render(request, "home.html", {"order_1": data} )
def retrieve_ordertable(request):
    data = Order_table.objects.raw("select * from main_app_order_table where status != 'Remove' ") 
    return render(request, "home.html", {"order": data})

def edit_brandtable(request,pk):
    result = Brand_Table(id=pk)
    result.id = request.POST.get("id")
    result.categoryname = request.POST.get("categoryname")
    result.brandname = request.POST.get("brandname")
    result.createdat = request.POST.get("createdat")
    result.updatedat = request.POST.get("updatedat")
    result.save()
    return redirect( '/main_app/home' )
def showedit_brandtable(request,pk):
    result = Brand_Table.objects.get(id=pk) 
    return render(request, "branded.html", {"brandtable": result})

def edit_customertable(request, pk):
    data = Customer_Table(id=pk)
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.email = request.POST.get("email")
    data.phone = request.POST.get("phone")
    data.createdat =request.POST.get("createdat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_customertable(request,pk):
    data = Customer_Table.objects.get(id=pk) 
    return render(request, "customeredit.html", {"customertable": data})

def edit_bannertable(request, pk):
    data = Banner_Table(id=pk)
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_bannertable(request, pk):
    data = Banner_Table.objects.get(id=pk) 
    return render(request, "banneredit.html", {"bannertable": data})


def edit_paymenttable(request, pk):
    data = Payment_Table(id=pk)
    data.id = request.POST.get("id")
    data.paymenttype = request.POST.get("paymenttype")
    data.phonenumber = request.POST.get("phonenumber")
    data.createdat = request.POST.get("createdat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_paymenttable(request, pk):
    data = Payment_Table.objects.get(id=pk) 
    return render(request, "paymentedit.html", {"paymenttable": data})


def edit_delifeetable(request, pk):
    data = Delifee_Table(id=pk)
    data.id = request.POST.get("id")
    data.regionname = request.POST.get("regionname")
    data.township = request.POST.get("township")
    data.deliveryfees = request.POST.get("deliveryfees")
    data.status = request.POST.get("status")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_delifeetable(request, pk):
    data = Delifee_Table.objects.get(id=pk) 
    return render(request, "delifeeedit.html", {"delifeetable": data})



def edit_regiontable(request, pk):
    data = Region_table(id=pk)
    data.id = request.POST.get("id")
    data.regionname = request.POST.get("regionname")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_regiontable(request, pk):
    data = Region_table.objects.get(id=pk) 
    return render(request, "regionedit.html", {"regiontable": data})


def edit_producttable(request, pk):
    data = Product_Table(id=pk)
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.price = request.POST.get("price")
    data.stock = request.POST.get("stock")
    data.category = request.POST.get("category")
    data.brand = request.POST.get("brand")
    data.createdat = request.POST.get("createdat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_producttable(request, pk):
    data = Product_Table.objects.get(id=pk) 
    return render(request, "productedit.html", {"producttable": data})

def edit_informationtable(request, pk):
    data = Information_Table(id=pk)
    data.id = request.POST.get("id")
    data.content = request.POST.get("content")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_informationtable(request, pk):
    data = Information_Table.objects.get(id=pk) 
    return render(request, "informationedit.html", {"informationtable": data})


def edit_categorytable(request, pk):
    data = Category_Table(id=pk)
    data.id = request.POST.get("id")
    data.name = request.POST.get("name")
    data.createdat = request.POST.get("createdat")
    data.updatedat = request.POST.get("updatedat")
    data.save()
    return redirect( '/main_app/home' )
def showedit_categorytable(request,pk):
    data = Category_Table.objects.get(id=pk) 
    return render(request, "categoryedit.html", {"categorytable": data})


def edit_ordertable(request, pk):
    data = Order_table(id=pk)
    data.orderid = request.POST.get("orderid")
    data.customer = request.POST.get("customer")
    data.status = request.POST.get("status")
    data.orderdate = request.POST.get("orderdate")
    data.save()
    return redirect( '/main_app/home' )
def showedit_ordertable(request, pk):
    data = Order_table.objects.get(id=pk) 
    return render(request, "orderedit.html", {"ordertable": data})


def delete_data(request,pk):
    data = Customer_Table.objects.get(id=pk)
    data.name = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_banner(request, pk):
    data = Banner_Table.objects.get(id=pk)
    data.name = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_payment(request, pk):
    data = Payment_Table.objects.get(id=pk)
    data.paymenttype = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_delifee(request, pk):
    data = Delifee_Table.objects.get(id=pk)
    data.deliveryfees = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_region(request, pk):
    data = Region_table.objects.get(id=pk)
    data.regionname = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_product(request, pk):
    data = Product_Table.objects.get(id=pk)
    data.stock = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_information(request, pk):
    data = Information_Table.objects.get(id=pk)
    data.updatedat = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_category(request, pk):
    data = Category_Table.objects.get(id=pk)
    data.createdat = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_brand(request, pk):
    data = Brand_Table.objects.get(id=pk)
    data.brandname = "Remove"
    data.save()
    return redirect("/main_app/home")

def delete_order(request, pk):
    data = Order_table.objects.get(orderid=pk)
    data.status = "Remove"
    data.save()
    return redirect("/main_app/home")