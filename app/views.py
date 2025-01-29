from django.shortcuts import render, redirect
from .models import comentuser, products, like, bascet
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
def about(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    return render(request, 'about.html', {'posts': son, 'posts1' : son1})
def contac(request):
    user1 = request.user
    data = like.objects.filter(user=user1)
    data1 = bascet.objects.filter(user = user1)
    son1 = str(len(data1))
    son = str(len(data))
    if request.method == 'POST':
        but = request.POST.get('buttom')
        if but == 'salom':
            if request.user.is_authenticated:
                user = request.POST.get('name')
                email = request.POST.get('email')
                message = request.POST.get('message')
                comentuser.objects.create(name = user, email = email, izoh = message)
            else:
                messages.info(request, "Adminga yozish uchun birinchi ro'yxatdan o'ting")
                return redirect('register')
    
    return render(request, 'contact.html', {'posts': son, 'posts1' : son1})


def home(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    return render(request, 'index.html', {'posts': son, 'posts1' : son1})

def shop_single(request, slug):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    if request.method == 'POST':
        user = request.user
        rasm_id = request.POST.get('image_id')
        try:
            data_id = products.objects.get(id=rasm_id)
        except:
            messages.info('Serverda xatolik!')
        rasm = data_id.rasm
        slug1 = data_id.slug
        title = request.POST.get('title')
        narx = request.POST.get('narx')
        button = request.POST.get('submit')
        
        if button == 'fourite':
            if like.objects.filter(user=user, slug=slug1).exists():
                messages.info(request, 'Ishbu maxsulot allaqachon yoqtirganlarim bo\'limida')
            else:
                like.objects.create(user=user, rasm= rasm, slug=slug1, title=title, narx=narx)
            return redirect('fourite')
        
        rang = request.POST.get('rang')
        rezmer = request.POST.get('razmer')
        action = request.POST.get('action')
        value = int(request.POST.get('value1'))  # Boshlang'ich qiymat 1 deb olamiz
        if action == 'plus':
            value = value + 1
        elif action == 'minus':
            value = value - 1
        if button == 'buy':
            if bascet.objects.filter(title = title).exists():
                messages.info(request, 'Ushbu maxsulot tanlangan')
                return redirect('bascet')
            else:
                jami = int(narx) * value
                bascet.objects.create(user = user, rasm = rasm, title=title, rang = rang, razmer = rezmer, narx = narx, soni = value, jami = jami, slug = slug1)
                return redirect('bascet')
        a = products.objects.filter(slug=slug)
        return render(request, 'shop-single.html', {'value': value, 'posts' : son, 'product':a, 'posts1' : son1})
            
    a = products.objects.filter(slug=slug)
    return render(request, 'shop-single.html', {'product':a, 'posts': son, "value" : 1, 'posts1' : son1})

def shop(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    a = products.objects.all()
    paginator = Paginator(a, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'shop.html', {'product' : page_obj, 'page' : page_obj, 'posts': son, 'posts1' : son1})

def fourite(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    a = like.objects.filter(user=request.user)
    return render(request, 'fourite.html', {'like' : a, 'posts': son, 'posts1' : son1})



def bascet1(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    bas = bascet.objects.filter(user = user)
    b = 0
    for i in bas:
        b+=i.jami
    return render(request, 'bascet.html', {'posts': son, 'like' : bas, 'jami1' : b, 'posts1' : son1})





def addfourite(request, slug):
    if like.objects.filter(slug=slug, user=request.user).exists():
        messages.info(request, 'Ishbu maxsulot allaqachon yoqtirganlarim bo\'limida')
        return redirect('fourite')
    else:
        a = products.objects.get(slug=slug)
        rasm = a.rasm
        title = a.title
        narx = a.narx
        like.objects.create(user = request.user, rasm = rasm, slug = slug, title = title, narx = narx)
        return redirect('fourite')

def delete_bascet(request, product_id):
    pro = bascet.objects.get(id = product_id)
    pro.delete()
    return redirect('bascet')



def delete_fourite(request, product_id):
    lik = like.objects.get(id=product_id)
    lik.delete()
    return redirect('fourite')


def LikeViews(request):
    ...







def register(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    if request.method == 'POST':
        ism = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        passw1 = request.POST.get('password1')
        if passw == passw1:
            if User.objects.filter(username = ism).exists():
                messages.error(request, 'Ushbu username band')
            else:
                User.objects.create_user(username=ism, email=email, password=passw)
                messages.success(request, 'Muavfaqiyatli ro\'yxatdan o\'tdingiz')
                return redirect('login')
        else:
            messages.error(request, '2 xil parol kiritildi')
    return render(request, 'actions/register.html' , {'posts': son, 'posts1' : son1})

def loginPage(request):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            ism = request.POST.get('username')
            passw = request.POST.get('password')
            
            user = authenticate(request, username=ism, password=passw)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'username yoki parol notog\'ri')
                return redirect('login')
    return render(request, 'actions/login.html', {'posts': son, 'posts1' : son1})

def logoutpage(request):
    logout(request)
    messages.info(request, 'Accountdan muaffaqiyatli chiqildi')
    return redirect('login')



def categoryVeiw(request, slug):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    a = products.objects.filter(category__slug=slug)
    return render(request, 'categories/category.html', {'product' : a, 'posts': son, 'posts1' : son1})

def category2Veiw(request, slug):
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    posts = products.objects.filter(category1__slug=slug)
    return render(request, 'categories/category2.html', {'product' : posts, 'posts': son, 'posts1' : son1})

def category3Veiw(request, slug):
    a = products.objects.filter(category2__slug=slug)
    user = request.user
    data = like.objects.filter(user=user)
    data1 = bascet.objects.filter(user = user)
    son1 = str(len(data1))
    son = str(len(data))
    return render(request, 'categories/category3.html', {'product' : a, 'posts': son, 'posts1' : son1})

