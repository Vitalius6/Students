from django.db import connection


class TestMiddleware(object):


    def process_response(self, request, response):

        return response
