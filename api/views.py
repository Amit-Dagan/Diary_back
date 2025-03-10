from post.models import Post
import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_home(request):
    model_data = Post.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)
