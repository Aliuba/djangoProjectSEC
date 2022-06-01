from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.
class UserView(APIView):
    def get(self, *args, **kwargs):
        qs= UserModel.objects.all()
        name=self.request.query_params.get('name')
        if name:
            qs=qs.filter(name__iexact=name)
        users= UserSerializer(qs, many=True).data
        return Response(users, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data=self.request.data
        serializer=UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def put(self, *args, **kwargs):
        return Response("put")
class ReadUpdateDelet(APIView):
    def get(self, *args, **kwargs):
        pk=kwargs.get('pk')
        instance=get_object_or_404(UserModel, pk=pk)
        serializer=UserSerializer(instance).data
        return Response(serializer, status.HTTP_200_OK)


    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(instance, self.request.data, partial=True )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)



    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        instance.delete()
        return Response("", status.HTTP_204_NO_CONTENT)

