from django.shortcuts import render
from .models import Banner, Program, Gallery, Contact


def home(request):
    banners = Banner.objects.all()
    programs = Program.objects.all()[:3]
    gallery = Gallery.objects.all()[:6]

    context = {
        "banners": banners,
        "programs": programs,
        "gallery": gallery,
    }

    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


from django.core.paginator import Paginator

def programs(request):
    search = request.GET.get("search", "")

    programs = Program.objects.all()

    if search:
        programs = programs.filter(title__icontains=search)

    paginator = Paginator(programs, 5)   # 5 programs per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "programs.html", {
        "page_obj": page_obj,
        "search": search,
    })


def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, "gallery.html", {"gallery": gallery})


from django.shortcuts import render, redirect
from .models import Banner, Program, Gallery, Contact


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        return redirect("contact")

    return render(request, "contact.html")

# Create your views here.
