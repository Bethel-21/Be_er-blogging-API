from django.http import HttpResponse

def comment_list(request):
    return HttpResponse("This is the comment list page.")

def comment_detail(request, id):
    return HttpResponse(f"This is the detail page for comment {id}.")
