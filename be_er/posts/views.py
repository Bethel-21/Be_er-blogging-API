from django.http import HttpResponse

def post_list(request):
    return HttpResponse("This is the post list page.")

def post_detail(request, id):
    return HttpResponse(f"This is the detail page for post {id}.")
