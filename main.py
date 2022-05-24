from flask import Flask
from flask_restful import Api
from views.home import Home
from views.manga_info import MangaInfo
from views.manga_list import MangaList
from views.read_manga import ReadManga

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(MangaList, '/manga_list')
api.add_resource(MangaInfo, '/manga_info')
api.add_resource(ReadManga, '/read_manga')

if __name__ == '__main__':
    app.run(debug=False)
