from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PinForm, ActivityForm, PictureForm
from perdiqma_homepage.models import Perdiqma, Perdiqmaadmin, Activity, GalleryPicture
from django.contrib.auth.decorators import login_required
# Create your views here.
PIN_PASSWORD = "290406"

def index(request):
    return render(request, "index.html")

def login_selection(request):
    return render(request, "login_selection.html")

def pin_pass(request):
    if request.method == 'POST':
        form = PinForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data.get('pin')
            if pin == PIN_PASSWORD:
                return redirect('register_admin')
            else:
                form.add_error('pin', 'Invalid PIN')
    else:
        form = PinForm()
    return render(request, 'pin_pass.html', {'form': form})

def register_admin(request):
    if request.method == 'POST':
        adminID = request.POST.get('adminID')
        adminname = request.POST.get('adminname')
        adminphone = request.POST.get('adminphone')
        adminpass = request.POST.get('adminpass')
        passw2 = request.POST.get('passw2')

        if adminpass != passw2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=adminID).exists():
            messages.error(request, "ADMIN ID is already taken. Please use a different ADMIN ID.")
        else:
            admin_member = User.objects.create_user(username=adminID, password=adminpass)
            admin_member.first_name = adminname
            admin_member.save()
            perdiqmaadmin = Perdiqmaadmin(adminID=adminID, adminname=adminname, adminphone=adminphone)
            perdiqmaadmin.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('adminlogin')
    return render(request, 'register_admin.html')

def adminlogin(request):
    if request.method == 'POST':
        adminID = request.POST.get('adminID')
        adminpass = request.POST.get('adminpass')
        user = authenticate(request, username=adminID, password=adminpass)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Username or password is incorrect")
    return render(request, "adminlogin.html")

@login_required
def admin_dashboard(request):
    logged_in_admin = Perdiqmaadmin.objects.get(adminID=request.user.username)
    
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PictureForm()
    
    context = {
        'form': form,
        'admin_name': logged_in_admin.adminname,
    }
    
    return render(request, "admin_dashboard.html", context)

def gallery(request):
    pictures = GalleryPicture.objects.all()
    return render(request, 'gallery.html', {'pictures': pictures})

def activitylistdetailuser(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activity_detailuser.html', {'activity': activity})

@login_required
def register_perd(request):
    if request.method == 'POST':
        perdiqmaID = request.POST.get('perdiqmaID')
        perdiqmaname = request.POST.get('perdiqmaname')
        perdiqmaphone = request.POST.get('perdiqmaphone')
        perdiqmapass = request.POST.get('perdiqmapass')
        perdiqmabureau = request.POST.get('perdiqmabureau')
        passw2 = request.POST.get('passw2')

        if perdiqmapass != passw2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=perdiqmaID).exists():
            messages.error(request, "PERDIQMA ID is already taken. Please use a different PERDIQMA ID.")
        else:
            perdiqma_member = User.objects.create_user(username=perdiqmaID, password=perdiqmapass)
            perdiqma_member.save()
            perdiqma = Perdiqma(perdiqmaID=perdiqmaID, perdiqmaname=perdiqmaname, perdiqmaphone=perdiqmaphone, perdiqmabureau=perdiqmabureau)
            perdiqma.save()
            messages.success(request, "Registration successful.")
            return redirect('admin_dashboard')
    return render(request, 'register_perd.html')

@login_required
def update_member(request, perdiqmaID):
    member = get_object_or_404(Perdiqma, perdiqmaID=perdiqmaID)
    if request.method == 'POST':
        perdiqmaID = request.POST.get('perdiqmaID')
        perdiqmaname = request.POST.get('perdiqmaname')
        perdiqmaphone = request.POST.get('perdiqmaphone')
        perdiqmabureau = request.POST.get('perdiqmabureau')
        
        member.perdiqmaID = perdiqmaID
        member.perdiqmaname = perdiqmaname
        member.perdiqmaphone = perdiqmaphone
        member.perdiqmabureau = perdiqmabureau
        member.save()
        
        messages.success(request, 'Member updated successfully.')
        return redirect('perdiqma_list')
    return render(request, 'update_member.html', {'member': member})

@login_required
def delete_member(request, perdiqmaID):
    member = get_object_or_404(Perdiqma, perdiqmaID=perdiqmaID)
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Member deleted successfully.')
        return redirect('perdiqma_list')
    return render(request, 'delete_member.html', {'member': member})


@login_required
def perdiqma_list(request):
    perdiqma_member = Perdiqma.objects.all()
    return render(request, "perdiqma_list.html", {'members': perdiqma_member})

@login_required
def activitylist(request):
    activities = Activity.objects.all()
    return render(request, 'activitylistadmin.html', {'activities': activities})

@login_required
def activitycreate(request, pk=None):
    if pk:
        # If pk is provided, we're editing an existing activity
        activity = get_object_or_404(Activity, pk=pk)
    else:
        # Otherwise, we're creating a new activity
        activity = None

    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            activity = form.save(commit=False)
            if not pk:  # Only set the created_by if creating a new activity
                activity.created_by = Perdiqmaadmin.objects.get(adminID=request.user.username)  # Assuming a OneToOne relationship with User
            activity.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)

    return render(request, 'activity_create.html', {'form': form})

    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.created_by = Perdiqmaadmin.objects.get(adminID=request.user.username)  # Assuming a OneToOne relationship with User
            activity.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm()
    return render(request, 'activity_create.html', {'form': form})

@login_required
def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activity_detail.html', {'activity': activity})


def activity_update(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_detail', pk=activity.pk)
    else:
        form = ActivityForm(instance=activity)
    return render(request, 'activity_create.html', {'form': form})

    return render(request, 'activity_update.html')

@login_required
def activity_delete(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    
    if request.method == 'POST':
        activity.delete()
        messages.success(request, 'Activity was successfully deleted.')
        return redirect('activitylistadmin')  # or any other URL you want to redirect to after deletion

    return render(request, 'activity_delete.html', {'activity': activity})


def loginpageperdiqma(request):
    if request.method == 'POST':
        perdiqmaID = request.POST.get('perdiqmaID')
        perdiqmapass = request.POST.get('perdiqmapass')
        user = authenticate(request, username=perdiqmaID, password=perdiqmapass)
        if user is not None:
            login(request, user)
            return redirect('perdiqma_dashboard')
        else:
            messages.error(request, "Username or password is incorrect")
    return render(request, 'loginpage.html')

@login_required
def perdiqma_dashboard(request):
    activities = Activity.objects.all() 
    context = {
        'activities': activities,
    }
    return render(request, "perdiqma_dashboard.html", context)

@login_required
def assign_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        perdID = request.POST.get('perdID')
        perd = get_object_or_404(Perdiqma, perdiqmaID=perdID)
        activity.members.add(perd)
        messages.success(request, f'{perd.perdiqmaname} has been assigned to {activity.title}.')
        return redirect('track_activity')
    
    perdiqma_members = Perdiqma.objects.all()
    context = {
        'activity': activity,
        'members': perdiqma_members,
    }
    return render(request, 'assign_activity.html', context)

@login_required
def track_activity(request):
    try:
        perdiqma_member = Perdiqma.objects.get(perdiqmaID=request.user.username)
        activities = perdiqma_member.activities.all()
    except Perdiqma.DoesNotExist:
        activities = []

    context = {
        'activities': activities,
    }
    return render(request, 'track_activity.html', context)
    return render(request, 'track_activity.html', context)

def gallery(request):
    pictures = GalleryPicture.objects.all()  # Or use filtering as needed
    context = {
        'pictures': pictures,
    }
    return render(request, 'gallery.html', context)

def activitylistuser(request):
    activities = Activity.objects.all()
    return render(request, 'activitylistuser.html', {'activities': activities})
