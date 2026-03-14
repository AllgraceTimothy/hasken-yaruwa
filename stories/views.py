from django.shortcuts import render, get_object_or_404
from .models import BlogPost, SuccessStory

def blog_list(request):
  posts = BlogPost.objects.filter(published=True).order_by('-created_at')

  return render(request,'stories/blog_list.html',{'posts': posts})

def blog_detail(request, slug):

    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True
    )

    return render(
        request,
        'stories/blog_detail.html',
        {'post': post}
    )

def success_story_list(request):

    stories = SuccessStory.objects.filter(
        published=True
    ).order_by('-created_at')

    return render(
        request,
        'stories/success_list.html',
        {'stories': stories}
    )

def success_story_detail(request, pk):

    story = get_object_or_404(
        SuccessStory,
        pk=pk,
        published=True
    )

    return render(
        request,
        'stories/success_detail.html',
        {'story': story}
    )