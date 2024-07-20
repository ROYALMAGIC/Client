from django.shortcuts import render

def ClientHome(request):
    return render(request,'client_Home.html')
def ClientProfile(request):
    return render(request,'ClientProfile.html')
def ClientProjectlist(request):
    return render(request,'ClientProjectlist.html')
def ClientTicketlist(request):
    return render(request,'ClientTicketlist.html')
def ClientFeedback(request):
    return render(request,'ClientFeedback.html')
def ClientHistory(request):
    return render(request,'ClientHistory.html')


