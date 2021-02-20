from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Vocab, Definition


def index(request):
    context = {'vocabList': Vocab.objects.all()}
    return render(request,"vocab/index.html",context)

def detail(request, vocab_id):
    vocab = get_object_or_404(Vocab,pk=vocab_id)
    print(vocab)
    context = {'vocab':vocab}
    return render(request,"vocab/detail.html",context)

def addWordPage(request):
    return HttpResponse("ลองเพิ่มคำศัพท์ดูสิ")