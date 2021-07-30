from django.http import HttpResponse


class Stripe_Controller:
    """Functions for stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Base handler for webhook events
        """
        return HttpResponse(
            content=f'Base webhook handler received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handler for the stripe payment_intent.succeeded event
        """
        return HttpResponse(
            content=f'Payment succeeded webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handler for the stripe payment_intent.payment_failed event
        """
        return HttpResponse(
            content=f'Payment failed webhook received: {event["type"]}',
            status=200)
