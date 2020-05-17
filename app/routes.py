# third-party imports
from flask import redirect,request,jsonify
import requests

# local imports
from app import app
from app import cache
from app import catalog_servers,order_servers
from app.helpers import getCachedBooks,getCachedBook,getResponse 




@app.route("/cleare-cache",methods=['POST'])
def cleareCache():
    data = request.get_json()
    print("clear cache for: "+ str(data['id']))
    cache.delete_memoized(getCachedBooks)
    if(data['id' != 'books']):
        cache.delete_memoized(getCachedBook,str(data['id']))
    return jsonify() ,200

# index route, redirect to api dcumentation url
@app.route('/')
def index():
    return redirect('https://bazar2.docs.apiary.io')


# Book Collection 
@app.route('/books',methods=['GET', 'POST'])
def Books():
    #add new book
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        sqlite_insert_query = "INSERT INTO books (title, amount) VALUES ('"+data['title']+"',"+str(data['amount'])+")"
        # TODO:- add the order srver url
        req = {
            'sqlite_query':sqlite_insert_query
        }
        

        result = getResponse('books','/query',req)
        
        resData=result.json()
        data={'id':resData['id'],'title':data['title'],'amount':data['amount']}
        return jsonify(data) ,201
    #list all books
    elif request.method == 'GET':
        title = request.args.get('title') 
        if(title is None):
            title =''
                
        result = getCachedBooks(title)
        
        res =result.json()
        return jsonify(res) ,200

# Book Object 
@app.route('/books/<book_id>',methods=['GET', 'POST'])
def Book(book_id):
    #add new book
    if request.method == 'POST':
        data = request.get_json()

        if data['operation'] == 'buy':
            
            result = getCachedBook(book_id)
           
            records = result.json()
            if(len(records) == 0):
                res = {
                    'message': 'Record Not Found'
                }
                return jsonify(res) ,404
            book = records[0]

            result = getResponse('order','/operation/buy',book)

            if result.status_code == 410:
                res = {
                    'message': 'Out of stock'
                }
                return jsonify(res) ,410
            print(result)
            book = result.json()

            return jsonify(book) ,200

        else:
            res = {
                'message': 'Unsupported operation'
            }
            return jsonify(res) ,405

    #list book object data
    elif request.method == 'GET':
        sqlite_insert_query = "SELECT * FROM books where id = "+ book_id
        
        result = getCachedBook(book_id)
        
        records = result.json()

        if(len(records) == 0):
            res = {
                'message': 'Record Not Found'
            }
            return jsonify(res) ,404

        
        row = records[0]
        res = {'id':row['id'],'title':row['title'],'amount':row['amount']}
        
        return jsonify(res) ,200



