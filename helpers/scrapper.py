from helpers.networker import Networker
from helpers.scrapper_helper import ScrapperHelper


class Scrapper:
    @staticmethod
    def scrape_advanced_search_mangas(result_page_link):
        main_page = Networker.get_soup(result_page_link)
        mangas_containers = main_page.select("div.book-item")

        scrapper_helper = ScrapperHelper()
        mangas = scrapper_helper.create_advanced_search_mangas_dict(mangas_containers)
        data = [
            {
                "data": mangas,
            }
        ]

        return data

    @staticmethod
    def scrape_recent_mangas(recent_page_link):
        main_page = Networker.get_soup(recent_page_link)
        mangas_containers = main_page.select("div.book-item")

        mangas = ScrapperHelper.create_recent_mangas_dict(mangas_containers)
        data = [
            {
                "data": mangas,
            }
        ]

        return data

    @staticmethod
    def scrape_manga_info(url):
        manga_page = Networker.get_soup(url)
        scrapper_helper = ScrapperHelper()
        manga_info = scrapper_helper.create_manga_info_dict(manga_page)

        return [
            manga_info
        ]

    @staticmethod
    def scrape_chapter_imgs(chapter_url):
        chapter_page = Networker.get_soup(f"{chapter_url}-10-1.html")
        imgs = chapter_page.select("div.pic_box")

        images_links = [{"img": img.find_next("img")["src"]} for img in imgs]
        page_numbers = chapter_page.select_one("div.mangaread-pagenav:nth-child(1) > "
                                               "select:nth-child(5) > option").text.split("/")
        if page_numbers[0] != page_numbers[1]:
            for page in range(int(page_numbers[0]) + 1, int(page_numbers[1]) + 1):
                new_chapter_page = Networker.get_soup(f"{chapter_url}-10-{page}.html")
                imgs = new_chapter_page.select("div.pic_box")

                for img in imgs:
                    images_links.append({"img": img.find_next("img")["src"]})

        return images_links
