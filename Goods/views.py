from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms

def main(request):
    banners = models.Banner.objects.all()
    category = models.Category.objects.all()
    last_img = models.ProductImg.objects.all()
    feature_pro = models.FeatureProduct.objects.all()
    recent_articles = models.RecentArticles.objects.all()
    side_menu = models.SideMenu.objects.all()
    total_price = sum(sm.price * sm.quantity for sm in side_menu)
    total_items = side_menu.count()

    context = {}
    context['banners'] = banners
    context['categories'] = category
    context['products'] = last_img
    context['feature'] = feature_pro
    context['rec_articles'] = recent_articles
    context['side_menu'] = side_menu
    context['total_price'] = total_price
    context['total_items'] = total_items



    return render(request, 'index.html', context)


def user(request):
    return render(request, 'user/detail.html')
    
def contact(request):
    return render(request, 'contact.html')


def banner_create(request):
    if request.method == 'POST':
        form = forms.BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = forms.BannerForm()
    return render(request, 'banners/banner_form.html', {'form': form})
    
    
def banner_list(request):
    banners = models.Banner.objects.all()
    return render(request, 'banners/banner_list.html', {'banners': banners})
    
    
def banner_update(request, pk):
    banner = get_object_or_404(models.Banner, pk=pk)
    if request.method == 'POST':
        form = forms.BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = forms.BannerForm(instance=banner)
    return render(request, 'banners/banner_form.html', {'form': form})
    
    
def banner_delete(request, pk):
    banner = get_object_or_404(models.Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        return redirect('banner_list')
    return render(request, 'banners/banner_confirm_delete.html', {'banner': banner})


def footer_bottom_list(request):
    items = models.FooterBottom.objects.all()
    return render(request, 'footer_bottom/footer_bottom_list.html', {'items': items})

def footer_bottom_detail(request, pk):
    item = get_object_or_404(models.FooterBottom, pk=pk)
    return render(request, 'footer_bottom/footer_bottom_detail.html', {'item': item})

def footer_bottom_create(request):
    if request.method == 'POST':
        form = forms.FooterBottomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('footer_bottom_list')
    else:
        form = forms.FooterBottomForm()
    return render(request, 'footer_bottom/footer_bottom_form.html', {'form': form})

def footer_bottom_update(request, pk):
    item = get_object_or_404(models.FooterBottom, pk=pk)
    if request.method == 'POST':
        form = forms.FooterBottomForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('footer_bottom_detail', pk=item.pk)
    else:
        form = forms.FooterBottomForm(instance=item)
    return render(request, 'footer_bottom/footer_bottom_form.html', {'form': form})

def footer_bottom_delete(request, pk):
    item = get_object_or_404(models.FooterBottom, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('footer_bottom_list')
    return render(request, 'footer_bottom/footer_bottom_confirm_delete.html', {'item': item})

def footer_bottom_img_create(request):
    if request.method == 'POST':
        form = forms.FooterBottomImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('footer_bottom_list')
    else:
        form = forms.FooterBottomImgForm()
    return render(request, 'footer_bottom/footer_bottom_img_form.html', {'form': form})
