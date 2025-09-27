from django.http import HttpResponse

def category_list(request):
    return HttpResponse("This is the category list page.")

def category_detail(request, id):
    return HttpResponse(f"This is the detail page for category {id}.")
