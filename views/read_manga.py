from flask import request
from flask_restful import Resource
from helpers.scrapper import Scrapper


class ReadManga(Resource):
    def get(self):
        url = request.headers["url"]
        data = Scrapper.scrape_chapter_imgs(url)

        return data
