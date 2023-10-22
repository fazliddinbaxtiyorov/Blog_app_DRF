from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import BlogModel
from .serializers import BlogSerializer, SomeSerializer


class All_Blogs(ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'all'


class Blog_Create(CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication ]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'create'


class Blog_Detail(RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'detail'
    lookup_field = 'id'


class Blog_Delete(DestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'delete'
    lookup_field = 'id'


class Blog_Update(UpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'update'
    lookup_field = 'id'


class User_Blog_Search(ListAPIView):
    queryset = BlogModel
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    throttle_scope = 'user'

    def get_queryset(self):
        user = self.request.user
        return BlogModel.objects.filter(username=user)


class Sorted(ListAPIView):
    queryset = BlogModel
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def filter_queryset(self, queryset):
        queryset = super(Sorted, self).filter_queryset(queryset)
        return queryset.objects.order_by('title')
