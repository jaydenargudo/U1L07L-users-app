from django.shortcuts import render

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             messages.success(request, 'Account created successfully! You can now log in.')  # Success message
#             return redirect('users:login')  # Redirect to login page (make sure you have this URL)
#     else:
#         form = UserCreationForm()  # Create an empty form for GET requests

#     return render(request, 'users/register.html', {'form': form})  # Render the registration template

def register(request):
    return render(request, 'users/register.html')

# Create your views here.
