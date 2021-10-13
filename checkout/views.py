from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jk5DjEGAJ0QdMrrRPD8VlyYaYQXjxFkAzbCOIvuCYmlCxXAx1CNbbIBj6wWD7saHJUfCLZ8DRGkTnvagSy2Zsne00xfQ5wEMu',
        'client_secret': 'sk_test_51Jk5DjEGAJ0QdMrrCeWKpdn8zBUW7EEfhLWYygdCSbxTVCDOdDR6nbvp1XB6vzFORuHuexJtqfopJ5rEuz6rHTIv00JfDgB9HU',
    }

    return render(request, template, context)