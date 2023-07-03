from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .serializers import (BookSerializers,AuthorSerializers,BookCategorySerializers)
from .models import (AuthorModel,BookModel,BookCategoryModel)

class AllBookGetView(APIView):
    def get(self, request, *args, **kwargs):
        all_book = BookModel.objects.all()
        respons = BookSerializers(all_book, many=True)
        return Response(respons.data)


class CreateBookApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateBookApiView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(BookModel,pk=kwargs['id'])
        serializer = BookModel(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteBookApiView(APIView):
    def delete(self,request,*args,**kwargs):
        book = get_object_or_404(BookModel,pk=kwargs['id'])
        book.delete()
        return Response({"delete":"massage del"})


class AllAuothorGetView(APIView):
    def get(self, request, *args, **kwargs):
        all_book = AuthorModel.objects.all()
        respons = AuthorSerializers(all_book, many=True)
        return Response(respons.data)


class CreateAouthorApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateAuthorApiView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(AuthorModel,pk=kwargs['id'])
        serializer = AuthorModel(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteAuthorApiView(APIView):
    def delete(self,request,*args,**kwargs):
        book = get_object_or_404(AuthorModel,pk=kwargs['id'])
        book.delete()
        return Response({"delete":"massage del"})
