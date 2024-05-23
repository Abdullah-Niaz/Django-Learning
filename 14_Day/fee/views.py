from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    fee_dic = {
        "fee": "500",
    }
    return render(request,"fee/home.html",fee_dic)

feepay_dummy = {
    "user": {
        "user_id": "123456",
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "+1234567890",
        "address": {
            "line1": "123 Main St",
            "line2": "Apt 4B",
            "city": "Anytown",
            "state": "Anystate",
            "zip": "12345",
            "country": "USA"
        }
    },
    "transaction": {
        "transaction_id": "txn_001",
        "amount": 1500,  # amount in cents
        "currency": "USD",
        "date": "2024-05-22T15:30:00Z",
        "status": "completed",  # statuses could be 'completed', 'pending', 'failed'
        "description": "Payment for order #ORD1234"
    },
    "payment_method": {
        "method": "credit_card",  # could be 'credit_card', 'paypal', 'bank_transfer', etc.
        "details": {
            "card_number": "**** **** **** 1234",
            "expiry_date": "12/26",
            "card_holder_name": "John Doe",
            "billing_address": {
                "line1": "123 Main St",
                "line2": "Apt 4B",
                "city": "Anytown",
                "state": "Anystate",
                "zip": "12345",
                "country": "USA"
            }
        }
    },
    "merchant": {
        "merchant_id": "m_7890",
        "merchant_name": "Example Store",
        "contact_email": "support@examplestore.com",
        "contact_phone": "+1987654321"
    },
    "fees": {
        "service_fee": 100,  # service fee in cents
        "tax": 50,  # tax in cents
        "total": 1650  # total amount in cents
    },
    "metadata": {
        "order_id": "ORD1234",
        "customer_notes": "Please deliver between 9 AM and 5 PM",
        "internal_notes": "VIP customer"
    }
}

def feepay(request):

    return render(request,"fee/fee.html",feepay_dummy)