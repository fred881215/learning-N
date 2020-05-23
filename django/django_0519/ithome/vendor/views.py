from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm

# Create your views here.
def vendor_index(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    context = {'vendor_list': vendor_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'vendor/vendor_detail.html', context)

# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VerdorForm() # 清空 form

    context = {
        'form' : form
    }
    return render(request, "vendor/vendor_create.html", context)