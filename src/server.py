import json

from flask import Flask, request

from doc_store import DocStore

doc_store = None
app = Flask(__name__)


def main():
    global doc_store

    print("Making doc store")
    doc_store = DocStore()
    doc_store.load_documents('./documents')

    print("Starting Server")
    start_server()


def start_server():
    global app
    app.run()


@app.route('/search')
def search():
    query = request.args.get('query')
    search_results = doc_store.search(query)
    return json.dumps(search_results)


if __name__ == "__main__":
    main()
