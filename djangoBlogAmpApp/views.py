from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from django.http import HttpResponse
from django.views import View
from .forms import CommentForm, CommentFormAmp
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.mail import EmailMessage

class PostListAmp(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog-amp.html'
    paginate_by = 6

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog-regular.html'
    paginate_by = 6

# class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'blog_detail.html'

def post_detail_amp(request, slug):
    template_name = 'blog-detail-amp.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentFormAmp(request.POST)
        if comment_form.is_valid():
            new_comment = Comment()
            new_comment.name = comment_form.cleaned_data['name']
            new_comment.email = comment_form.cleaned_data['email']
            new_comment.body = comment_form.cleaned_data['body']
            
            # Assign the current post to the comment
            new_comment.post = post

            # For User
            subject = 'Regi Apriandi Blog Newsletters'
            message = f'Hi {new_comment.name}, Thank you for your valuable support and comments on our blog page "{new_comment.post}". Every word you write is an inspiration for us to continue sharing and creating.\nYour comments will soon appear on the blog page.\n\nThank You.\nRegards, Regi Apriandi.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [f'{new_comment.email}']
            mail = EmailMessage(subject, message, email_from, recipient_list)
            mail.send(fail_silently=False)

            # For Admin
            subject_admin = f'New Comment on "{new_comment.post}" from {new_comment.email}'
            message_admin = f'{new_comment.body}'
            email_from_admin = settings.EMAIL_HOST_USER
            recipient_list_admin = ['regi@regiapriandi.com']
            mail_admin = EmailMessage(subject_admin, message_admin, email_from_admin, recipient_list_admin)
            mail_admin.send(fail_silently=False)

            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentFormAmp()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def post_detail(request, slug):
    template_name = 'blog-detail-regular.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = Comment()
            new_comment.name = comment_form.cleaned_data['name']
            new_comment.email = comment_form.cleaned_data['email']
            new_comment.body = comment_form.cleaned_data['body']

            # Assign the current post to the comment
            new_comment.post = post

            # For User
            subject = 'Regi Apriandi Blog Newsletters'
            message = f'Hi {new_comment.name}, Thank you for your valuable support and comments on our blog page "{new_comment.post}". Every word you write is an inspiration for us to continue sharing and creating.\nYour comments will soon appear on the blog page.\n\nThank You.\nRegards, Regi Apriandi.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [f'{new_comment.email}']
            mail = EmailMessage(subject, message, email_from, recipient_list)
            mail.send(fail_silently=False)

            # For Admin
            subject_admin = f'New Comment on "{new_comment.post}" from {new_comment.email}'
            message_admin = f'{new_comment.body}'
            email_from_admin = settings.EMAIL_HOST_USER
            recipient_list_admin = ['regi@regiapriandi.com']
            mail_admin = EmailMessage(subject_admin, message_admin, email_from_admin, recipient_list_admin)
            mail_admin.send(fail_silently=False)

            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class AdsView(View):
    def get(self, request, *args, **kwargs):
        line = "google.com, pub-5362230413425518, DIRECT, f08c47fec0942fa0"
        return HttpResponse(line)
        # Test
        
"""def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)"""

## Mail Configuration
"""
subject = 'welcome to GFG world'
    message = f'Hi Regi, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['regiapriandi024@gmail.com', 'regiapriandi012@gmail.com']
    mail = EmailMessage(subject, message, email_from, recipient_list)
    mail.send(fail_silently=False)
"""