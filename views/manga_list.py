from flask import request
from flask_restful import Resource
from utils.consts import GENRES_DICT
from helpers.scrapper import Scrapper


class MangaList(Resource):
    def get(self):
        args = request.args
        orby = args.get("orby", "")
        in_genre = args.get("inGenre")
        keyw = args.get("keyw")
        language = args.get("language", "br")
        page = args.get("page", "1")

        genre_dict = GENRES_DICT[language]
        genre = ""
        for manga_genre in genre_dict:
            if manga_genre == in_genre:
                genre = genre_dict[manga_genre]

        if keyw is not None:
            data = Scrapper.scrape_advanced_search_mangas(
                f"https://{language}.novelcool.com/search/?name_sel=contain&name={keyw}&author_sel=contain&author=&"
                f"category_id={genre}&out_category_id=&publish_year="
                f"&completed_series=&rate_star=&orby={orby}&page={page}")
        elif orby == "latestUpdates":
            data = Scrapper.scrape_recent_mangas(
                f"https://br.novelcool.com/category/latest/category_id-{genre}.html")
        else:
            data = Scrapper.scrape_advanced_search_mangas(
                f"https://{language}.novelcool.com/search/?name_sel=contain&name=&author_sel=contain&author=&"
                f"category_id={genre}&out_category_id=&publish_year="
                f"&completed_series=&rate_star=&page={page}")
        return data
