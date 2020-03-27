from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render
import stripe
from django.contrib.auth.models import Permission
# Create your views here.

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    # Add to user's permission set
    permission = Permission.objects.get(codename='special_status')

    # Get user
    u = request.user

    # Add to user's permission set
    u.user_permissions.add(permission)

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='Premium Images',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
