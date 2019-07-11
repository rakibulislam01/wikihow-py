from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

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
        url_ = request.GET.get('url')
        # try:
        content = wiki_how_content(url_)
        # except:
        #     content = "Wiki How not found."

        ans = {'status': status.HTTP_200_OK, 'item': 'GET', 'Name': content}
        return Response(ans)
