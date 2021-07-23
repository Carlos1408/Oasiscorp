from .models.category import Category

def allCategories(request):
    categories = Category.objects.all()
    context = {'categories' : categories}
    return context
