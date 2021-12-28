from django.shortcuts import redirect,render, get_object_or_404
from django.contrib.auth import login, authenticate
from hood.forms import CreateBusinessForm, CreateNeighborHoodForm, CreatePostForm, SignUpForm, UpdateBusinessForm, UpdateNeighborhoodForm, UpdatePostForm, UpdateProfileFrom
from django.contrib.auth.models import User
from .models import Profile, Business, Post, Neighborhood
from django.contrib import messages


# Create your views here.
def home(request):
    neighborhoods = Neighborhood.objects.all()
    return render(request, 'index.html', {'neighborhoods':neighborhoods})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    


def users_profile(request,pk):
    user = User.objects.get(pk = pk)
    user_posts = Post.objects.filter(user_id = user.id).all()
    current_user = request.user
    
    return render(request,'profile.html',{'user_posts':user_posts,"user":user,"current_user":current_user})



def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileFrom()
    return render(request, 'update_profile.html', {'form': form})



# def neighbourhoods(request):
#     all_hoods = Neighborhood.objects.all()
#     all_hoods = all_hoods[::-1]
#     params = {
#         'all_hoods': all_hoods,
#     }
#     return render(request, 'neighbourhoods.html', params)

def neighborhood(request, neighborhood_id):
    current_user = request.user
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    business = Business.objects.filter(neighborhood=neighborhood)
    users = Profile.objects.filter(neighborhood=neighborhood)
    posts = Post.objects.filter(neighborhood=neighborhood)

    return render(request, 'neighbourhoods.html', {'users':users,'current_user':current_user, 'neighborhood':neighborhood,'business':business,'posts':posts})



# def create_neighborhood(request):
#     if request.method == 'POST':
#         form = CreateNeighborHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hood = form.save(commit=False)
#             hood.admin = request.user.profile
#             hood.save()
#             return redirect('hood')
#     else:
#         form = CreateNeighborHoodForm()
#     return render(request, 'newhood.html', {'form': form})

def neighborhood(request):
    if request.method == 'POST':
        create_neighborhood_form = CreateNeighborHoodForm(request.POST, request.FILES)
        if create_neighborhood_form.is_valid():
            neighborhood = create_neighborhood_form.save(commit=False)
            neighborhood.admin = request.user.profile
            neighborhood.save()
            return redirect('home')
    else:
        create_neighborhood_form = CreateNeighborHoodForm()
    return render(request, 'newhood.html', {'create_neighborhood_form': create_neighborhood_form})
  
def update_neighborhood(request, neighborhood_id):
    neighborhood = Neighborhood.objects.get(pk=neighborhood_id)
    if request.method == 'POST':
        update_neighborhood_form = UpdateNeighborhoodForm(request.POST,request.FILES, instance=neighborhood)
        if update_neighborhood_form.is_valid():
            update_neighborhood_form.save()
            messages.success(request, f'Post updated!')
            return redirect('home')
    else:
        update_neighborhood_form = UpdateNeighborhoodForm(instance=neighborhood)

    return render(request, 'update_neighborhood.html', {"update_neighborhood_form":update_neighborhood_form})

def delete_neighborhood(request,neighborhood_id):
    current_user = request.user
    neighborhood = Neighborhood.objects.get(pk=neighborhood_id)
    if neighborhood:
        neighborhood.delete_neighborhood()
    return redirect('home')

def join_neighborhood(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood, id=neighborhood_id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('home')

def get_neighborhood_users(request, neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    users = Profile.objects.filter(neighborhood=neighborhood)
    return render(request, 'neighborhood_users.html', {'users': users})


def leave_neighborhood(request, neighborhood_id):
    hood = get_object_or_404(Neighborhood, id=neighborhood_id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('home')


def single_neighbourhood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = CreateBusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = CreateBusinessForm()
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)


# def post(request, hood_id):
#     hood = Neighborhood.objects.get(id=hood_id)
#     if request.method == 'POST':
#         form = CreatePostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.hood = hood
#             post.user = request.user.profile
#             post.save()
#             return redirect('single-hood', hood.id)
#     else:
#         form = CreatePostForm()
#     return render(request, 'post.html', {'form': form})

def post(request, neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        add_post_form = CreatePostForm(request.POST,request.FILES)
        if add_post_form.is_valid():
            post = add_post_form.save(commit=False)
            post.neighborhood = neighborhood
            post.user = request.user
            post.save()
            return redirect('neighborhood', neighborhood.id)
    else:
        add_post_form = CreatePostForm()
    return render(request, 'post.html', {'add_post_form': add_post_form,'neighborhood':neighborhood})

def update_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        update_post_form = UpdatePostForm(request.POST,request.FILES, instance=post)
        if update_post_form.is_valid():
            update_post_form.save()
            messages.success(request, f'Post updated!')
            return redirect('home')
    else:
        update_post_form = UpdatePostForm(instance=post)

    return render(request, 'update_post.html', {"update_post_form":update_post_form})

def delete_post(request,post_id):
    current_user = request.user
    post = Post.objects.get(pk=post_id)
    if post:
        post.delete_post()
    return redirect('home')


def business(request,neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        new_business_form = CreateBusinessForm(request.POST, request.FILES)
        if new_business_form.is_valid():
            business = new_business_form.save(commit=False)
            business.neighborhood =neighborhood
            business.user = request.user
            business.save()
            return redirect('neighborhood', neighborhood.id)
    else:
        new_business_form = CreateBusinessForm()
    return render(request, 'business.html', {'new_business_form': new_business_form,'neighborhood':neighborhood})

def delete_business(request,business_id):
    current_user = request.user
    business = Business.objects.get(pk=business_id)
    if business:
        business.delete_business()
    return redirect('home')

def update_business(request, business_id):
    business = Business.objects.get(pk=business_id)
    if request.method == 'POST':
        update_business_form = UpdateBusinessForm(request.POST,request.FILES, instance=business)
        if update_business_form.is_valid():
            update_business_form.save()
            messages.success(request, f'Business updated!')
            return redirect('home')
    else:
        update_business_form = UpdateBusinessForm(instance=business)

    return render(request, 'update_business.html', {"update_business_form":update_business_form})  