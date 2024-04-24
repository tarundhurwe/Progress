from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import (
    UserSerializer,
    ProblemListSerializer,
    ProblemSerializer,
    NoteSerializer,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import ProblemList, Problem, Note

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class HomeView(generics.ListAPIView):
    serializer_class = ProblemListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ProblemList.objects.all()


class ProblemView(generics.ListAPIView):
    serializer_class = ProblemSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

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


class MarkedProblemsView(generics.UpdateAPIView):
    serializer_class = ProblemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        problem_id = self.kwargs.get("problem_id")
        return Problem.objects.filter(problem_id=problem_id).first()

    def put(self, request, *args, **kwargs):
        problem = self.get_queryset()
        problem.status = not problem.status
        problem.save()
        serializer = self.get_serializer(problem)
        return Response(serializer.data)
