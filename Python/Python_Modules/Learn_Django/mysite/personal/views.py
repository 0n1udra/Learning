from django.shortcuts import render
from ipware import get_client_ip
from django.shortcuts import render_to_response
from django.template import RequestContext

from . import saveip

# Create your views here.

def index(request):
    #get_client_ip(request) For function in this file
    # Better way to get ip using ipware
    ip, is_routable = get_client_ip(request)
    if ip is None:
        print('ERROR: Getting IP address')
    else:
        if is_routable:
            print("INFO: Routable IP", ip)
            saveip.saveip(ip, True)
        else:
            print("INFO: Non-Routable IP", ip)
            saveip.saveip(ip, False)

    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html',
            {'content': ['Contact Me', 'Mail: dxzt99@gmail.com\n']})

def about(request):
    return render(request, 'personal/basic.html',
                {"content": ['About', 'This is my website to study Django']} )

# 404/500
def handler404(request, context_instance=None):
    print('HI')
    response = render(request, 'personal/error.html',
                    {'content': ['404 Page Not Found']})
    response.status_code = 404
    return response

def handler500(request, context_instance=None):
    response = render(request, 'personal/error.html',
                    {'content': ['500 Error']})
    response.status_code = 500
    return response

# def get_client_ipp(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[-1].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     print("INFO: Connection From:", ip)
#     return ip
