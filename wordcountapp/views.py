from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_diction = {}
    for word in words:
        if word in word_diction:
            word_diction[word] += 1
        else:
            word_diction[word] = 1

    return render(request, 'result.html', {'full': text, 'total':len(words), 'dictionary':word_diction.items()})
