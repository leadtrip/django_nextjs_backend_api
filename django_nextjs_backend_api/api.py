from ninja import NinjaAPI, Schema
from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_jwt.authentication import JWTAuth
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")

class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None

@api.get("/hello")
def hello(request):
    print(request)
    return {"message": "Hello world"}


@api.get("/me",
         response=UserSchema,
         auth=JWTAuth())
def me (request):
    return request.user
