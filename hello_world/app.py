import os
import json
import pickle
import numpy as np


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    model_path = "model.pkl"
    if not os.path.exists(model_path):
        raise Exception("Model not found")
    model = pickle.load(open(model_path, "rb"))
    
    features = event["features"]
    prediction = model.predict(np.array(features).reshape([1, -1]))[0]
    

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "prediction": prediction,
            }
        ),
    }

# if __name__ == '__main__':
#     print("os.getcwd():", os.getcwd())
#     with open('events/event.json') as f:
#         data = json.load(f)
#     print(lambda_handler(data, {}))