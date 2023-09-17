from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from server.helpers import generate_prompt
import json
import openai

openai.api_key = "<PUT YOUR API KEY HERE>"
@api_view(['GET', 'POST'])
def recipe_list(request):
    
    response = {
         'data': 'This endpoint only supports POST'
	}
    
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'ingredients' not in body:
            response['data'] = 'Please provide an ingredients array'
        else:
            ingredients = body['ingredients']
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": generate_prompt(ingredients) }])
            response['data'] = completion.choices[0].message.content
        
    return Response(response, status=status.HTTP_200_OK)