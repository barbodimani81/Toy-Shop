# from django.http import HttpResponse
# from django.shortcuts import render
# from .forms import SignUpForm
# from .models import User
#
# def SignUp(request):
#     if request.method == "GET":
#         form = SignUpForm()
#         context = {'form': form}
#         return render(request, 'create_user.html', context)
#
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             User.objects.create_user(
#                 username=data["username"],
#                 email=data["email"],
#                 first_name=data["first_name"],
#                 last_name=data["last_name"],
#                 password=data["password"],
#             )
#             context = {'form': form}  # Adjust the context as needed
#             return render(request, 'success.html', context)
#         else:
#             return HttpResponse('method not allowed')
