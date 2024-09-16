from django.shortcuts import redirect

def redirect_to_mabar_admin(request):
    return redirect('/admin/mabar/mabar/')
