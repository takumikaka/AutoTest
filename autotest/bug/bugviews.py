from django.shortcuts import render
from bug.models import Bug

# Create your views here.

def bug_manage(request):
    username = request.session.get("user", "")
    bug_list = Bug.objects.all()
    return render(request, "bug_manage.html", {"username": username, "bugs": bug_list})
