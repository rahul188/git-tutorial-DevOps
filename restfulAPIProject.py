from flask import Flask,jsonify,request
from flask_restful import Api,Resource

app = Flask("__name__")
api = Api(app)

def checkPostedData(postedData,functionName):

    if functionName=="add" or functionName=="Subtraction" or functionName=="multiply":
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200    

    if functionName=="division":
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif postedData["y"]==0:
            return 302
        else:
            return 200

class Add(Resource):

    def post(self):       

        postedData = request.get_json()
        statusCode = checkPostedData(postedData,"add")

        if statusCode==301:
            retJson = {
                "Message":"An error happened",
                "Status Code":statusCode
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retJson = {
            "Message":ret,
            "Status Code":statusCode
        }
        return jsonify(retJson)

class Subtraction(Resource):

    def post(self):       

        postedData = request.get_json()
        statusCode = checkPostedData(postedData,"Subtraction")

        if statusCode==301:
            retJson = {
                "Message":"An error happened",
                "Status Code":statusCode
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x-y
        retJson = {
            "Message":ret,
            "Status Code":statusCode
        }
        return jsonify(retJson)


class multiply(Resource):

    def post(self):       

        postedData = request.get_json()
        statusCode = checkPostedData(postedData,"multiply")

        if statusCode==301:
            retJson = {
                "Message":"An error happened",
                "Status Code":statusCode
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x*y
        retJson = {
            "Message":ret,
            "Status Code":statusCode
        }
        return jsonify(retJson)


class Division(Resource):

    def post(self):       

        postedData = request.get_json()
        statusCode = checkPostedData(postedData,"division")

        if statusCode==301:
            retJson = {
                "Message":"An error happened",
                "Status Code":statusCode
            }
            return jsonify(retJson)

        if statusCode==302:
            retJson = {
                "Message":"invalid value for y element",
                "Status Code":statusCode
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x/y
        retJson = {
            "Message":ret,
            "Status Code":statusCode
        }
        return jsonify(retJson)


api.add_resource(Add,"/add")
api.add_resource(Subtraction,"/sub")
api.add_resource(multiply,"/mul")
api.add_resource(Division,"/div")


@app.route("/")
def entry():
    return "Welcome To digitalOedipus API world."


if __name__=="__main__":
    app.run(debug=True)