from flask.views import MethodView
from flask_smorest import Blueprint,abort
from schemas import ItemSchema

blp = Blueprint('items','items',url_prefix='/items',description='Operations on items')

items = []

@blp.route('/')
class ItemList(MethodView):
    @blp.response(200)
    def get(self):
        return items
    
    @blp.arguments(ItemSchema)
    @blp.response(201,'Item added')
    def post(self,new_data):
        items.append(new_data)

        return new_data
    
    