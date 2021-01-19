# import datetime
#
# from .models import Logg


# def LogMiddleware(get_response):
#     def middleware(request):
#
#         request.current_time = datetime.datetime.now()
#         # a = [i for i in str(request.path).split('/')]
#         logg = Logg(path=request.path,
#                     method=request.method,
#                     timestamp=request.current_time)
#
#         logg.save()
#         response = get_response(request)
#
#         return response
#
#     return middleware
