
import time
from importlib import import_module

from django.conf import settings
from django.contrib.sessions.backends.base import UpdateError
from django.contrib.sessions.exceptions import SessionInterrupted
from django.utils.cache import patch_vary_headers
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import http_date


class CookieDomainMiddleware(MiddlewareMixin):
    """
    This is the custom cookie domain middleware which changes the domain of the sessionid.
    """
    def process_request(self, request):
        request.change_domain=False

    def process_view(self, request, view_func, view_args, *view_kwargs):

        if view_func.__name__ in ["GoogleLogin","FacebookLogin"]:
            request.change_domain = True
        return None
    def process_response(self, request, response):
        if settings.HTTP_ONLY_COOKIE_DOMAIN and request.change_domain:
            if "sessionid" in response.cookies:
                del response.cookies["sessionid"]
            if "messages" in response.cookies:
                del response.cookies["messages"]
            # for cookie in response.cookies.keys():
            #     print(response.cookies[cookie])
            #     ref = response.cookies[cookie]
            #     ref['domain'] = settings.HTTP_ONLY_COOKIE_DOMAIN
        return response
    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def __call__(self, request):
    #     response = self.get_response(request)
    #     print("This is response:",response)
    #     if response.cookies:
    #         host = request.get_host()
    #         print("ji",host)
    #         # check if it's a different domain
    #         # if host not in settings.SESSION_COOKIE_DOMAIN:
    #         # domain = ".{domain}".format(domain=host)
    #         domain = settings.HTTP_ONLY_COOKIE_DOMAIN
    #         for cookie in response.cookies:
    #             if 'domain' in response.cookies[cookie]:
    #                 response.cookies[cookie]['domain'] = domain
    #     return response
