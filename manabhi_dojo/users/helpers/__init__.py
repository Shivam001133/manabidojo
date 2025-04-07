def userloggedin(request):
    return request.user.username if request.user.is_authenticated else None
