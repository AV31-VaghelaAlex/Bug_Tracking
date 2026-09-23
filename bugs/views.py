from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm, CommentForm


def dashboard(request):
    bugs = Bug.objects.all()

    search = request.GET.get("search")
    status = request.GET.get("status")

    if search:
        bugs = bugs.filter(title__icontains=search)

    if status:
        bugs = bugs.filter(status=status)

    return render(
        request,
        "bugs/dashboard.html",
        {"bugs": bugs}
    )


def create_bug(request):
    form = BugForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(
        request,
        "bugs/form.html",
        {"form": form}
    )


def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)

    form = CommentForm(request.POST or None)

    if form.is_valid():
        c = form.save(commit=False)
        c.bug = bug

        # Since we are not using login anymore,
        # don't use request.user here.
        c.save()

        return redirect(f"/bug/{pk}/")

    return render(
        request,
        "bugs/detail.html",
        {
            "bug": bug,
            "form": form
        }
    )


def my_bugs(request):
    bugs = Bug.objects.all()

    return render(
        request,
        "bugs/my_bugs.html",
        {"bugs": bugs}
    )