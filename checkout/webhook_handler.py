from django.http import HttpResponse

class StripeWH_Handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """" Handle a webhook event """
        return HttpResponse(
            content = f'Unhandled webhook received: {event['type']}',
            status = 200
        )
    
    def handle_payment_intent_succeeded(self, event):
        """" Handle the stripe payment_intent.succeeded webhook """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content = f'Webhook received: {event['type']}',
            status = 200
        )
    
    def handle_payment_intent_failed(self, event):
        """" Handle the stripe payment_intent.failed webhook """
        return HttpResponse(
            content = f'Webhook received: {event['type']}',
            status = 200
        )