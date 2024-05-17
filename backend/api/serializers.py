from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Problem, ProblemList, Note, Status
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("This username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("This email is already taken.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemList
        fields = ["problem_set_id", "problem_set_name", "author", "link"]


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = [
            "problem_id",
            "problem_set_id",
            "problem_name",
            "problem_type",
            "problem_link",
        ]


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "content", "updated_at", "problem_id", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["problem_id", "status", "user_id"]