from django.shortcuts import render
from datetime import datetime
from  django.http import JsonResponse, HttpResponse
from .models import visitor
# Create your views here.


def get_client_info(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"

    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    return [ip, os_type, os_version, device_type, browser_type, browser_version]

def h(request, *args, **kwargs):
    info = get_client_info(request)
    with open('F:/try/info.txt', 'a') as f:
        print(
            "\nkkkk : " , request.META['HTTP_X_FORWARDED_FOR'],
            "\n---------------------------------------------------------------------------------------------------------------------",
            "\nuser : ", request.user,

            "\nCOOKIES"
            "\ncsrftoken : ", request.COOKIES['csrftoken'],
            "\nsession id : ", request.COOKIES['sessionid'],
            "\ndevice info"
            "\nip : ", info[0],
            "\nos_type : ", info[1],
            "\nos_version : ", info[2],
            "\ndevice_type : ", info[3],
            "\nbrowser_type : ", info[4],
            "\nbrowser_version : ", info[5],

            "\nheaders"
            "\nContent Length : ", request.headers['Content-Length'],
            "\nContent Type : ", request.headers['Content-Type'],
            "\nConnection : ", request.headers['Connection'],
            "\nCache Control : ", request.headers['Cache-Control'],
            "\nUpgrade Insecure Requests : ", request.headers['Upgrade-Insecure-Requests'],
            "\nUser Agent : ", request.headers['User-Agent'],
            "\nAccept : ", request.headers['Accept'],
            "\nSec Fetch Site : ", request.headers['Sec-Fetch-Site'],
            "\nSec Fetch Mode : ", request.headers['Sec-Fetch-Mode'],
            "\nSec Fetch User : ", request.headers['Sec-Fetch-User'],
            "\nSec Fetch Dest : ", request.headers['Sec-Fetch-Dest'],
            "\nAccept Encoding : ", request.headers['Accept-Encoding'],
            "\nAccept Language : ", request.headers['Accept-Language'],
            "\nDnt : ", request.headers['Dnt'],

            # meta data
            "\nmeta data : ", request.META,
            # end meta data

            "\npath : ", request.path,
            "\nmethod : ", request.method,
            "\nbody : ", request.body,
            "\nscheme : ", request.scheme,
            "\ntime : ", datetime.now(),
            "\n---------------------------------------------------------------------------------------------------------------------",
            file=f
        )
    visitor.objects.create(
        path = request.path,
        method = request.method,
        scheme = request.scheme,
        headers = request.headers,
        body = request.body,
        user = request.user,
        info = info,
        COOKIES = request.COOKIES,
        METAdata = request.META,
        time = datetime.now(),
    )
    return HttpResponse("<h1>hello world h view</h1>")  # html code

