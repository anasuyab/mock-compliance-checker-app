# api/analyzeblueprint.py
import json

def handler(request):
    # Check if the request is a POST method (or an OPTIONS pre-flight check)
    print(
        "hello"
    )

    if request.method == 'POST':
        print("POST request received!") # Debug log in vercel dev console
        
        # In this simple runtime, it's easier to return a tuple or dict
        # Vercel handles setting the headers and writing the body from the return value.
        
        # The Vercel runtime is based on the ASGI/WSGI concept, but for Python 
        # serverless functions, returning a simple structure is supported.
        
        response_data = {
            "status": "success",
            "message": "Analysis complete",
            "data": {
                "compliant": 8,
                "violations": 3,
                "warnings": 2
            }
        }
        
        # Return a response tuple: (status_code, headers_dict, body)
        return (
            200,
            {
                'Content-type': 'application/json',
                # This is important for CORS in development
                'Access-Control-Allow-Origin': '*' 
            },
            json.dumps(response_data).encode('utf-8')
        )
        
    elif request.method == 'OPTIONS':
        # Handle the CORS pre-flight request
        return (
            200,
            {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            '' # Empty body for OPTIONS
        )
        
    else:
        # Handle other methods
        return (405, {}, 'Method Not Allowed')