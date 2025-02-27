# # from rest_framework import viewsets
# # from .models import Student
# # from .serializers import StudentSerializer

# # class StudentViewSet(viewsets.ModelViewSet):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer


# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Student
# from .serializers import StudentSerializer

# class StudentListCreateAPIView(APIView):
#     def get(self, request, format=None):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentRetrieveUpdateDestroyAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return None

#     def get(self, request, pk, format=None):
#         student = self.get_object(pk)
#         if student is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         student = self.get_object(pk)
#         if student is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         student = self.get_object(pk)
#         if student is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def patch(self, request, pk, format=None):
#         student = self.get_object(pk)
#         if student is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework import mixins, generics
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer

# class StudentListCreateView(mixins.ListModelMixin,
#                             mixins.CreateModelMixin,
#                             generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class StudentRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
#                                        mixins.UpdateModelMixin,
#                                        mixins.DestroyModelMixin,
#                                        generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
