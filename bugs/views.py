
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bug
from .forms import BugForm,CommentForm

@login_required
def dashboard(request):
    bugs = Bug.objects.all()

    search = request.GET.get("search")
    status = request.GET.get("status")

    if search:
        bugs = bugs.filter(title__icontains=search)

    if status:
        bugs = bugs.filter(status=status)

    return render(request,'bugs/dashboard.html',{'bugs':bugs})

@login_required
def create_bug(request):
    form=BugForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'bugs/form.html',{'form':form})

@login_required
def bug_detail(request,pk):
    bug=get_object_or_404(Bug,pk=pk)
    form=CommentForm(request.POST or None)
    if form.is_valid():
        c=form.save(commit=False)
        c.bug=bug
        c.user=request.user
        c.save()
        return redirect(f'/bug/{pk}/')
    return render(request,'bugs/detail.html',{'bug':bug,'form':form})

@login_required
def my_bugs(request):
    bugs = Bug.objects.filter(assigned_to=request.user)
    return render(request,"bugs/my_bugs.html",{"bugs":bugs})
