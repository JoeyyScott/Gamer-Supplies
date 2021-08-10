from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import Stripe_Controller
import stripe


@require_POST
@csrf_exempt
def webhook(request):
    # Listen for Stripe webhooks and setup
    wh_secret_gs = settings.STRIPE_WH_SECRET_GS
    stripe.api_key = settings.STRIPE_SECRET_KEY_GS

    # Verify signature from webhook data
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret_gs
        )
    except ValueError as e:
        # Payload error
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Signature error
        return HttpResponse(status=400)
    except Exception as e:
        # General fallback error
        return HttpResponse(content=e, status=400)

    # Initialize handler for webhook
    wh_handler = Stripe_Controller(request)

    # Variable to hold handler functions that are relevant
    events = {
        'payment_intent.succeeded': wh_handler.handle_payment_intent_succeeded,
        'payment_intent.\
            payment_failed': wh_handler.handle_payment_intent_payment_failed,
    }

    # Variable to hold event type from Stripe
    event_type = event['type']

    # If a handler exists use it, else fallback to default
    event_handler = events.get(event_type, wh_handler.handle_event)

    # Initialize event handler on the event
    response = event_handler(event)
    return response
