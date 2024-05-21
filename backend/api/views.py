from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    ProblemListSerializer,
    ProblemSerializer,
    NoteSerializer,
    StatusSerializer,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ProblemList, Problem, Note, Status

# Create your views here.


# working perfectly
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# working perfectly
class HomeView(generics.ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ProblemList.objects.all()


# working perfectly
class ProblemView(generics.ListAPIView):
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        problem_set_id = self.kwargs.get("id")
        problem_set_id = ProblemList.objects.get(problem_set_id=problem_set_id)
        if problem_set_id:
            return Problem.objects.filter(problem_set_id=problem_set_id)
        else:
            return Problem.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"Message": "Problemset does not exist."})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


#  need to check
class CreateNoteView(generics.CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        problem_id = self.kwargs.get("problem_id")
        user = self.request.user
        return Note.objects.filter(author=user, problem_id=problem_id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            return Response({"Error": serializer.errors})


# Working perfectly
class UserMarkedProblemsView(generics.ListAPIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        problem_set_id = self.kwargs.get("problem_set_id")
        return Status.objects.filter(user_id=user, problem_set_id=problem_set_id)


class UpdateStatusView(generics.UpdateAPIView):
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        problem_id = self.kwargs.get("problem_id")
        problem_set_id = self.kwargs.get("problem_set_id")
        user = self.request.user
        problem = Problem.objects.get(problem_id=problem_id)
        problem_set = ProblemList.objects.get(problem_set_id=problem_set_id)

        status_instance, created = Status.objects.get_or_create(
            user_id=user, problem_id=problem, problem_set_id=problem_set
        )
        if created:
            status_instance.status = True
        else:
            status_instance.status = not status_instance.status

        status_instance.save()

        return Response(self.serializer_class(status_instance).data)
