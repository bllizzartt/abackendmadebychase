from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from server.helpers import generate_prompt
import json
import openai
from roboflow import Roboflow

#chat gpt api key placement
openai.api_key = "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"
@api_view(['GET', 'POST'])
def recipe_list(request):
    print('\033[92m' + request.method + ': /recipes')
    
    response = {
         'data': 'This endpoint only supports POST'
	}
    #post if statement
    if request.method == 'POST':
        body = json.loads(request.body)
        if 'ingredients' not in body:
            response['data'] = 'Please provide an ingredients array'
        else:
            ingredients = body['ingredients']
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": generate_prompt(ingredients) }])
            response = {}
            response['data'] = { 'recipes': completion.choices[0].message.content} 

            prediction = get_roboflow_prediction('./test.png')
            
            response['data']['__roboflow__'] = {
                'message': 'This is just a test to see if we can get roboflow stuff on the frontend',
                'prediction': prediction 
            }
        
    return Response(response, status=status.HTTP_200_OK)


rf = Roboflow(api_key="uLEcLJqb1gFOIuYtSM5J")
project = rf.workspace().project("shopping-items")
model = project.version(1).model


def get_roboflow_prediction(image_path):
    return model.predict(image_path, confidence=40, overlap=30).json()




