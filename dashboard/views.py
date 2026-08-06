from django.shortcuts import render, redirect, get_object_or_404
from website.models import Program, Gallery, Banner, Contact
from .forms import ProgramForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def dashboard(request):
    
    latest_contacts = Contact.objects.order_by('-id')[:5]
    
    context = {
        "program_count": Program.objects.count(),
        "gallery_count": Gallery.objects.count(),
        "banner_count": Banner.objects.count(),
        "contact_count": Contact.objects.count(),
        "current_time": datetime.now(),
        "programs": Program.objects.all(),
        "latest_contacts": latest_contacts,
    }
    return render(request, "dashboard/dashboard.html", context)

@login_required(login_url='/admin/login/')
def add_program(request):
    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Program added successfully.")
            return redirect("dashboard")
    else:
        form = ProgramForm()

    return render(request, "dashboard/add_program.html", {"form": form})

@login_required(login_url='/admin/login/')
def edit_program(request, id):
    program = get_object_or_404(Program, id=id)

    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, "Program updated successfully.")
            return redirect("dashboard")
    else:
        form = ProgramForm(instance=program)

    return render(request, "dashboard/edit_program.html", {"form": form})

@login_required(login_url='/admin/login/')
def delete_program(request, id):
    program = get_object_or_404(Program, id=id)

    if request.method == "POST":
        program.delete()
        messages.success(request, "Program deleted successfully.")
        return redirect("dashboard")

    return render(request, "dashboard/delete_program.html", {"program": program})