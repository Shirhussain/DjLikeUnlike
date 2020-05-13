from django.shortcuts import render, redirect
from .models import Post, Like


def post_view(request):
    qs = Post.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user
    }
    return render(request, "index.html", context)


def like_post(request):
    user = request.user
    
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        # it means that the user like the post already so we gonna remve them if the user going to hit the like again
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        
        if not created:
            if like.value == "Like":
                like.value = "Like"
            else:
                like.value = "Unlike"
        like.save()
        return redirect("blog:index")
            








# def like_post(request):
#     if request.method == "POST":
#         post_id = request.POST.get('post_id')
#         post_obj = Post.objects.get(id=post_id)

#         # it means that the user like the post already so we gonna remve them if the user going to hit the like again
#         if request.user in post_obj.liked.all():
#             post_obj.liked.remove(request.user)
#         else:
#             post_obj.liked.add(request.user)

#         like, created = Like.objects.get_or_create(user=request.user, post_id=post_id)
        
#         if not created:
#             if like.value == "Like":
#                 like.value = "Unlike"
#             else:
#                 like.value = "Like"
#         like.save
#     return redirect('blog:index')

