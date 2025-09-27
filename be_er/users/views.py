from django.http import HttpResponse

def user_list(request):
    return HttpResponse("This is the user list page.")

def user_detail(request, id):
    return HttpResponse(f"This is the detail page for user {id}.")
