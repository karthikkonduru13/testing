
theOriginURL = 'http://localhost:3000'
def add_cors_headers(response):
    print("Adding CORS headers")
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response
