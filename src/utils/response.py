from flask import jsonify

def success(data): 
    return jsonify({
        "success": True,
        "data": data
    })
    
def error(message):
    return jsonify({
        "success": False,
        "message": message
    })

def response(data,status_code = 200):
   match status_code:
       case 200:
           return success(data)
       case 400:
            return error(data)
       case 422:
            return error(data)
