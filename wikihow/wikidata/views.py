from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Content
from .serializers import UserSerializer, GroupSerializer
from .wiki_how import wiki_how_content


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
        try:
            url_ = request.GET.get('url')
            url_ = url_.replace(' ', '-')

            try:
                content_q = get_object_or_404(Content, url_text=url_)
                content = content_q.content
            except:
                try:
                    content = wiki_how_content(url_)
                except:
                    content = "Wiki How not found."

            ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Type': 'How To '+url_, 'Content': content}
            return Response(ans)
        except:
            ans = {'status': status.HTTP_422_UNPROCESSABLE_ENTITY, 'item': 'GET', 'Type': None,
                   'Content': "Type Error"}
            return Response(ans)
