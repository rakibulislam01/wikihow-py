from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Content
from .serializers import UserSerializer, GroupSerializer
# from .wiki_how import wiki_how_content
from .wiki_how_test import wiki_how_content
from .wiki_how_search import search
from .wiki_how_image import wiki_how_content as image
# from .wiki_how_image_test import wiki_how_content as image_test


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class WikiHowViewSet(viewsets.ViewSet):
    """
    API endpoint that allows to get wikihow content
    """

    def list(self, request):
        global user_text, item, url
        try:
            url_ = request.GET.get('url')
            url_ = url_.replace(' ', '-')

            try:
                content_q = get_object_or_404(Content, user_text=url_)
                content = content_q.content
                user_text = content_q.url_text
                ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Title': 'How To ' + user_text, 'Content': content}
                return Response(ans)
            except:
                try:
                    try:
                        item = search(url_)
                        url = item.lower()
                        content_q = get_object_or_404(Content, url=url)
                        content = content_q.content
                        user_text = content_q.url_text
                        ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Title': 'How To ' + user_text,
                               'Content': content}
                        return Response(ans)
                    except:
                        content, user_text, status_value = image(url, url_)
                        ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Title': 'How To ' + user_text,
                               'status_value': status_value, 'Content': content}
                        return Response(ans)
                except:
                    content = "Wiki How not found."
                    ans = {'status': status.HTTP_422_UNPROCESSABLE_ENTITY, 'item': 'GET', 'Title': None,
                           'Content': content}
                    return Response(ans)

            # ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Title': 'How To ' + user_text, 'Content': content}
            # return Response(ans)
        except:
            ans = {'status': status.HTTP_422_UNPROCESSABLE_ENTITY, 'item': 'GET', 'Title': None,
                   'Content': "Type Error"}
            return Response(ans)


# class WikiHowTestViewSet(viewsets.ViewSet):
#     """
#     API endpoint that allows to get wikihow content
#     """
#
#     def list(self, request):
#         global user_text, item, url
#         # url_ = request.GET.get('url')
#         # url_ = url_.replace(' ', '-')
#
#         content, status_value = image_test('https://www.wikihow.com/Ride-a-Motorcycle')
#
# ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Title': 'How To ', 'status_value':status_value, 'Content': content} return Response(ans)
