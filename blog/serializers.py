from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



class ProfileSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'blogs']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['blog', 'text', 'author', 'created_at']
        read_only_fields = ['author']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)



class ProfileSerializer(serializers.ModelSerializer):
    blog_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'blog_count']

    def get_blog_count(self, obj):
        return obj.blog_set.count()
