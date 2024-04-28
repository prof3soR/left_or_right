from django.shortcuts import render, redirect
import os
import random
from .models import *
# List to store image filenames
image_list = []
voted = []

# Populate image_list with filenames from IMAGE_FOLDER
for filename in os.listdir('main_app/static/images'):
    if filename.endswith('.jpg'):
        image_list.append(filename)


def index(request):
    new_image_list = [img for img in image_list if img not in voted]
    random_images = random.sample(new_image_list, 2)
    return render(request, 'index.html', {'p1': random_images[0], 'p2': random_images[1]})


def vote(request):
    if request.method == 'POST':
        selected_image = request.POST.get('selected_image')
        voted.append(selected_image)
    try:
        image_vote = votes.objects.get(Redg_no=selected_image)
        image_vote.votes += 1
        image_vote.save()
    except votes.DoesNotExist:
        image_vote = votes.objects.create(Redg_no=selected_image, votes=1)
    return redirect('home')


def votes_list(request):
    # Get all votes objects
    all_votes = votes.objects.all()

    # Handle search functionality
    query = request.GET.get('search')
    if query:
        all_votes = all_votes.filter(Redg_no__icontains=query)

    context = {
        'votes': all_votes
    }
    return render(request, 'show_votes.html', context)


def feedback_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        feedback_obj = feedback.objects.create(name=name, message=message)
        feedback_obj.save()
    return render(request, 'feedback.html')
