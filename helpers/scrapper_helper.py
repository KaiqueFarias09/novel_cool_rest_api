class ScrapperHelper:
    def create_advanced_search_mangas_dict(self, manga_containers):
        mangas = []
        index = 0
        for manga in manga_containers:
            if self.is_not_a_novel(manga):
                if self.manga_has_chapters(manga):
                    manga_details = {
                        "index": index,
                        "title": manga.select_one(
                            "div:nth-child(4) > a:nth-child(1) > div:nth-child(1)").text.strip(),
                        "img": manga.findNext("img")["src"],
                        "src": manga.findNext("a")["href"],
                    }
                    mangas.append(manga_details)
                    index += 1

        return mangas

    @staticmethod
    def is_not_a_novel(manga):
        category = manga.select_one("div:nth-child(1) > a:nth-child(1) > div:nth-child(2)").text
        name = manga.select_one("div:nth-child(4) > a:nth-child(1) > div:nth-child(1)").text.strip()
        if category == "Manga" or category == "Mangá" or category == "Манга" and "novel" not in name.lower():
            return True
        else:
            return False

    @staticmethod
    def manga_has_chapters(manga):
        views = manga.find_next("div", "row-item book-data-num").text
        try:
            views = int(views)
        except ValueError:
            views = int(float(views.replace(",", ".")))

        if views >= 2:
            return True
        else:
            return False

    def create_manga_info_dict(self, manga_page):
        manga_info = {
            "title": manga_page.find("h1", class_="bookinfo-title").text,
            "img": manga_page.select_one("div.bookinfo-pic:nth-child(1) > a:nth-child(1) > img:nth-child(1)")["src"],
            "status": self.check_if_exists_and_returns_value(manga_page.select_one(".bk-cate-type1")),
            "lastUpdated": self.check_if_exists_and_returns_value(manga_page.select_one("div.chp-item")
                                                                  .find_next("span", class_="chapter-item-time")),
            "synopsis": self.check_if_exists_and_returns_value(manga_page.select_one("div.for-pc:nth-child(3) "
                                                                                     "> div:nth-child(2) > "
                                                                                     "div:nth-child(1)")),
            "genres": self.get_genres(manga_page),
            "chapters": self.get_chapters(manga_page),
        }
        return manga_info

    @staticmethod
    def check_if_exists_and_returns_value(html_element):
        try:
            info = html_element.text
        except AttributeError:
            return ""
        else:
            return info.strip()

    @staticmethod
    def get_genres(manga_page):
        genres = manga_page.select(
            "div.for-pc:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > a > span")
        try:
            genres_list = [{"genre": genre.text} for genre in genres]

        except TypeError:
            return ""
        else:
            return genres_list

    @staticmethod
    def get_chapters(manga_page):
        chapters_list = []
        chapters = manga_page.select("div.chp-item")
        for chapter in chapters:
            chapter_info = {
                "chapterTitle": chapter.find_next("a")["title"],
                "uploadedDate": chapter.find_next("span", class_="chapter-item-time").text,
                "chapterLink": chapter.find_next("a")["href"],
            }
            chapters_list.append(chapter_info)

        return chapters_list

    @staticmethod
    def create_recent_mangas_dict(manga_containers):
        mangas = []
        index = 0
        for manga in manga_containers:
            manga_details = {
                "index": index,
                "title": manga.find_next("div", class_="book-pic")["title"],
                "img": manga.find_next("img", class_="lazy-img")["lazy_url"],
                "src": manga.find_next("a")["href"],
            }
            mangas.append(manga_details)
            index += 1

        return mangas
