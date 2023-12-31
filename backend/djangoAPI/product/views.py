
from django.http import JsonResponse
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework import authentication,generics,mixins,permissions


class DetailApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class ListCreateProductView(generics.ListCreateAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer
     authentication_classes=[authentication.SessionAuthentication]
     permission_classes=[permissions.DjangoModelPermissions]
     
     def perform_create(self, serializer):
         name =serializer.validated_data.get('name')
         content =serializer.validated_data.get('content') or None
         if content is None:
             content=name
             serializer.save(content=content)
             
class UpdateProductView(generics.UpdateAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer
     lookup_field='pk'
     
     def perform_update(self, serializer):
         name =serializer.validated_data.get('name')
         content =serializer.validated_data.get('content') or None
         if content is None:
             content=name
         serializer.save(content=content)
         
class DeleteProductView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    
class ListProductView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def get_queryset(self):
        return super().get_queryset().filter(name_contains='mangue')
    
    
    
class ProductMixinsViews(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin,):
                    queryset=Product.objects.all()
                    serializer_class=ProductSerializer
                    lookup_field='pk'
                    
                    def perform_create(self, serializer):
                        name =serializer.validated_data.get('name')
                        content =serializer.validated_data.get('content') or None
                        if content is None:
                            content=name
                            serializer.save(content=content)
                            
                    def perform_update(self, serializer):
                        name =serializer.validated_data.get('name')
                        content =serializer.validated_data.get('content') or None
                        if content is None:
                            content=name
                            serializer.save(content=content)
                            
                    def get(self,request,*args, **kwargs):
                        pk=kwargs.get('pk')
                        if pk is not None:
                            return self.retrieve(request,*args, **kwargs)
                        return self.list(request,*args, **kwargs) 
                     
                    def post(self,request,*args, **kwargs):
                        return self.create(request,*args, **kwargs)
                                        
                    def delete(self,request,*args, **kwargs):
                        return  self.destroy(request,*args, **kwargs)
                    
                    def put(self,request,*args, **kwargs):
                        return self.update(request,*args, **kwargs)
    
        
        
             
                 
   
    

@api_view(['GET'])
def api_view(request):
    query=Product.objects.all().order_by('?').first()
    data={}
    if query:
        # data=model_to_dict(query,fields=('name','content','price','get_discount'))
        data=ProductSerializer(query).data
    return Response(data)    