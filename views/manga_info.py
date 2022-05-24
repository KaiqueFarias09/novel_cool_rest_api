from flask import request
from flask_restful import Resource
from helpers.scrapper import Scrapper


class MangaInfo(Resource):
    def get(self):
        url = request.headers["url"]
        data = Scrapper.scrape_manga_info(url)

        return data
