
def login_required(fx):
    def wrapper(user):
        if user.get("is_logged_in"):
            return fx(user)
        else:
            return "Acces Denied"
    return wrapper

@login_required
def dashboard(user):
    return f'Welcome {user["name"]}'

user1 = {"name": "Adi" , "is_logged_in": True}
print(dashboard(user1))