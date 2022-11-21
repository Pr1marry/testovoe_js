import os
import stripe
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from .models import Item
from .serializers import ItemSerializer

stripe.api_key = os.getenv('API_KEY')


class BuyViewSet(viewsets.ViewSet):
    http_method_names = ['get']

    def retrieve(self, request, pk=None):
        stripe.api_key = os.getenv('API_KEY')
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        id_stripe = stripe.Product.create(name=item.name)
        stripe.Price.create(
            unit_amount=item.price,
            currency=item.currency,
            recurring={"interval": "month"},
            product=id_stripe,
        )
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )

        return HttpResponse(session)


class ItemViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return render(request, 'payments.html', {
            'item': serializer.data,
        })

