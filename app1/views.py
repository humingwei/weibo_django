from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from app1.models import Status


def say(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' %request.path)

    statuses = Status.objects.filter(user=request.user)
    statuses = statuses.order_by('-id')
    return render(request, 'say.html', {'statuses': statuses})

def result(request):
    msg = request.POST['msg']

    if msg.strip() == '':
        errormsg = 'please input msg!'
        return render(request, 'result.html', {'errormsg': errormsg})

    Status(msg=msg, user=request.user).save()
    return redirect('/history')

def history(request):
    data_list = Status.objects.order_by("-id")
    paginator = Paginator(data_list, 5)

    page = request.GET.get('page')
    try:
        statuses = paginator.page(page)
    except PageNotAnInteger:
        statuses = paginator.page(1)
    except EmptyPage:
        statuses = paginator.page(paginator.num_pages)

    return render(request, 'history.html', {"statuses": statuses})

def status(request):
    sid = request.GET['id']
    s = Status.objects.get(id=sid)
    return render(request, 'status.html', {'s': s})

def mylogin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/say/')
    else:
        return HttpResponse("login failed")

def data(request):
    return render(request, 'data.html', {})

def data_csv(request):
    result_data = {}
    statuses = Status.objects.all()
    for st in statuses:
        result_data.setdefault(st.user, 0)
        result_data[st.user] += 1
    return render(request, 'data.csv', {'result': result_data.iteritems()})
