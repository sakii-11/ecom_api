from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductLCView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, *args, **kwargs):
      queryset = Product.objects.all()  
      param = int(self.request.query_params.get('order', None))
      if param == None:
        data = self.get_serializer(queryset, many= True)
        return Response({
            'data': data.data
          }, status= status.HTTP_200_OK)        
      elif param == 0:                                 #order=0 -> ascending order
          data = queryset.order_by('price')
          data = self.get_serializer(data, many= True)
          return Response({
            'data': data.data
          }, status= status.HTTP_200_OK)
      else:                             #order=1 -> descending order
          data = queryset.order_by('-price')
          data = self.get_serializer(data, many = True)
          return Response({
            'data': data.data
          }, status= status.HTTP_200_OK)     
      return Response({
        'error': 'There was some error'
      }, status= status.HTTP_400_BAD_REQUEST)

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


  
  