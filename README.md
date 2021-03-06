# Novel Cool API

This api is based on [novel cool](https://www.novelcool.com/) manga reading api to give you a better experience for your app.

## Table of Contents

**[Api Walkthrough](#api-walkthrough)**<br>
**[Request & Response Examples](#request--response-examples)**<br>

## API Walkthrough

### Common Formats

#### List / Pagination

```json
[
        "data": [
            {...},
            {...},
            ...
       ]
]
```

### GET /manga_list

#### Query Parameters & Headers

Parameters can be used to query, filter and control the results returned by the Mangato API. They can be passed as normal query parameters.

| Parameter          | Description                                                                                                                                                                                                                                                    |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `orby` (string)    | filter results by `Latest updates, top view, new manga, A-Z`. default: `Latest updates`                                                                                                                                                                        |
| `inGenre` (string) | filter results by genres. all genres are included by default. for example: If you include Historical , it will filter only mangas with Historical genre. (You can include multiple genres). for example: `inGenre=_15_` **NOTE: Genres list available below.** |
| `keyw` (string)    | filter results by manga name. for example: `keyw=one piece`                                                                                                                                                                                                    |
| `page` (int)       | by default page starts from 1. pages limit may vary                                                                                                                                                                                                            |

#### Genres

Every genre have a specific value which you can put in your Get Request query. therefore here is a list of genres in ascending order.

| Genre         | Value |
| :------------ | :---- |
| Action        | 2     |
| Adventure     | 4     |
| Ecchi         | 11    |
| Horror        | 16    |
| Mature        | 20    |
| Romance       | 27    |
| Shoujo        | 31    |
| Shounen       | 33    |
| Webtoons      | 40    |
| Yaoi          | 41    |
| Manhwa        | 43    |
| Manhua        | 44    |
| RecentDrama   | 50    |
| RecentAdventure | 51    |
| RecentShounen | 52    |
| RecentIsekai  | 53    |
| RecentHorror  | 54    |
| RecentManhwa  | 55    |
| RecentSuperPowers | 56    |
| RecentDemons  | 57    |
| RecentGames   | 58    |
| RecentSeinen  | 59    |

### GET /manga_info

#### Headers


| Header         | Description |
| :------------- | :---------- |
| `url` (string) | manga url   |

### GET /read_manga

#### Headers

chapter url can be accessed by making `GET /manga_info` request. [see exmaples below](#get-manga_info-1)

| Header         | Description |
| :------------- | :---------- |
| `url` (string) | chapter url |

## Request & Response Examples

### GET /manga_list

#### Example 1:

This query will filter results by genre

Example:

```command
curl 'http://localhost:3000/manga_list?inGenre=_2_'
```

Response body:

```json
[
    {
        "data": [
            {
                "index": 0,
                "title": "Ancient Godly Monarch (Novel)",
                "img": "https://img.novelcool.com/logo/201807/b7/Ancient_Godly_Monarch7127.jpg",
                "src": "https://br.novelcool.com/novel/Ancient_Godly_Monarch_Novel.html",
            },
            {
                "index": 1,
                "title": "The World Of Otome Games Is Tough For Mobs",
                "img": "https://avt.mkklcdnv6temp.com/13/q/17-1583495755.jpg",
                "src": "https://readmanganato.com/manga-cb980036",
            },
            {...},
            ...
        ]
    }
]
```

### GET /manga_info

#### Example 1:

"id" parameter and "host-name" header can be found in `GET /manga_list` response body as seen in the above sample.

Example:

```command
curl --header "host-name: readmanganato.com" http://localhost:3000/manga_info?id=manga-cb980036
```

Response body:

```json
[
    {
        "title": "The World Of Otome Games Is Tough For Mobs",
        "img": "https://avt.mkklcdnv6temp.com/13/q/17-1583495755.jpg",
        "alt": "Otome Game Sekai wa Mob ni Kibishii Sekai Desu",
        "authors": [
            {
                "authorName": "Yomu Mishima",
                "authorLink": "https://manganato.com/author/story/eW9tdV9taXNoaW1h"
            },
            {...},
            ...
        ],
        "status": "Ongoing",
        "lastUpdated": "Dec 04,2021 - 07:21 AM",
        "views": "20,764,407",
        "synopsis": "Leon, a former Japanese worker, was reincarnated into an ...",
        "rating": "4.8",
        "totalVotes": "8688",
        "genres": [
            {
                "genre": "Adventure",
                "genreLink": "https://manganato.com/genre-4"
            },
            {
                "genre": "Comedy",
                "genreLink": "https://manganato.com/genre-6"
            },
            {...},
            ...
        ],
        "chapters": [
            {
                "chapterTitle": "Chapter 38",
                "chapterViews": "30,031",
                "uploadedDate": "2 hour ago ",
                "chapterLink": "https://readmanganato.com/manga-cb980036/chapter-38"
            },
            {...},
            ...
        ]
    }
]
```

or you can use the `url` header instead like the below example to achieve the same result.

#### Example 2:

Example:

```command
curl --header "url: https://readmanganato.com/manga-cb980036" http://localhost:3000/manga_info
```

Response body:

```json
[
    {
        "title": "The World Of Otome Games Is Tough For Mobs",
        "img": "https://avt.mkklcdnv6temp.com/13/q/17-1583495755.jpg",
        "alt": "Otome Game Sekai wa Mob ni Kibishii Sekai Desu",
        "authors": [
            {
                "authorName": "Yomu Mishima",
                "authorLink": "https://manganato.com/author/story/eW9tdV9taXNoaW1h"
            },
            {...},
            ...
        ],
        "status": "Ongoing",
        "lastUpdated": "Dec 04,2021 - 07:21 AM",
        ...
        "genres": [
            {
                "genre": "Adventure",
                "genreLink": "https://manganato.com/genre-4"
            },
            {...},
            ...
        ],
        "chapters": [
            {
                "chapterTitle": "Chapter 38",
                "chapterViews": "30,031",
                "uploadedDate": "2 hour ago ",
                "chapterLink": "https://readmanganato.com/manga-cb980036/chapter-38"
            },
            {...},
            ...
        ]
    }
]
```

### GET /read_manga

Finally, as seen in the sample below, you will be able to receive chapter pages as jpg images.

#### Example 1:

`url` header can be seen in the example above.

Example:

```command
curl --header "url: https://readmanganato.com/manga-cb980036/chapter-38" http://localhost:3000/read_manga
```

Response body:

```json
[
    {
        "img": "https://s8.mkklcdnv6temp.com/mangakakalot/v1/vk917567/chapter_38/1.jpg",
        "pageTitle": "The World of Otome Games is Tough for Mobs Chapter 38 page 1"
    },
    {
        "img": "https://s8.mkklcdnv6temp.com/mangakakalot/v1/vk917567/chapter_38/2.jpg",
        "pageTitle": "The World of Otome Games is Tough for Mobs Chapter 38 page 2"
    },
    {
        "img": "https://s8.mkklcdnv6temp.com/mangakakalot/v1/vk917567/chapter_38/3.jpg",
        "pageTitle": "The World of Otome Games is Tough for Mobs Chapter 38 page 3"
    },
    {...},
    ...
]
```

## Contributing

[Pull requests](https://github.com/riimuru/Mangato-api/pulls) are welcome. For major changes, please open an [issue](https://github.com/riimuru/Mangato-api/issues/new) first to discuss what you would like to change.

Please make sure to update tests as appropriate.
