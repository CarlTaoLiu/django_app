from django.http import JsonResponse
from .models import Companies

# Create your views here.
def get_companies(request):
    companies = Companies.objects.all()
    
    return JsonResponse({
        "code": 200,
        "message": "success",
        "data": [
            {
                "name": company.name,
                "email": company.email
            } for company in companies
        ]
    })