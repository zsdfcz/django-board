from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def board_list(request):
    q = Board.objects.all()
    return render(request, 'board/board_list.html' , {'board_list':q})

def write(request):
    return render(request, 'board/board_write.html')

def board_write(request):
    board = Board(title=request.POST['title'], body=request.POST['content'])
    board.save()
    return HttpResponseRedirect(reverse('board:board_list'))

def detail(request,board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board/detail.html', {'board': board})

def comment(request, board_id):
    board = Board.objects.get(id = board_id)
    board.comment_set.create(message=request.POST['message'], created_at=timezone.now())
    return HttpResponseRedirect(reverse('board:detail', args=(board_id,)))  

def delete(request, board_id):
    board = Board.objects.get(id = board_id)
    board.delete()
    return HttpResponseRedirect(reverse('board:board_list'))

def update(request, board_id):
    board = Board.objects.get(id = board_id)
    return render(request, 'board/board_update.html',{'board': board})



def board_update(request, board_id):
    board = Board.objects.get(id = board_id)
    board.title = request.POST['title']
    board.body = request.POST['content']
    board.updated_at = timezone.now()
    board.save()
    return HttpResponseRedirect(reverse('board:board_list'))
    