from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, UserProfile

def index(request):
    page = request.GET.get()
    return render(request, 'wish_list.html')

@login_required
def view_wish_list(request):
    user_profile = request.user.userprofile
    wish_list_books = user_profile.wish_list.all()

    return render(request, 'wish_list.html', {'wish_list_books': wish_list_books})

@login_required
def add_to_wish_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_profile = request.user.userprofile
    user_profile.wish_list.add(book)
    return redirect('view_wish_list')

@login_required
def remove_from_wish_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user_profile = request.user.userprofile
    user_profile.wish_list.remove(book)
    return redirect('view_wish_list')
