from flask_smorest import Blueprint, abort
from schemas import BookSchema
from flask.views import MethodView


book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []

# 엔드포인트 구현...
@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200,BookSchema(many=True))
    def get(self):
        return books
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(201,BookSchema)
    def post(self, new_book):
        new_book['id']=len(books)+1
        books.append(new_book)
        return new_book


@book_blp.route('/<int:book_id>')
class Book(MethodView):
    @book_blp.response(200,BookSchema)
    def get(self,book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book == None:
            abort(404,message='Book Not Found')
        return book
    
    @book_blp.arguments(BookSchema)
    @book_blp.response(200,BookSchema)
    def put(self,new_book,book_id):
        book = next((book for book in books if book[id]==book_id), None)
        if book == None:
            abort(404,message='Book Not Found')
        book.update(new_book)
        return book
    
    @book_blp.response(204)
    def delete(self,book_id):
        global books
        book = next((book for book in books if book[id]==book_id), None)
        if book == None:
            abort(404,message='Book Not Found')
        books = [book for book in books if book['id'] != book_id]
        return ''