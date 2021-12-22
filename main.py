from conf import MODEL
import random
from random import randint
import faker
from faker import Faker
import json


pk = 1
model = MODEL
faker = Faker()


def title_gen() -> str:
    k = open("books.txt")
    data = k.read()
    lines = data.split("\n")
    line = random.randrange(len(lines))
    book_title = lines[line]
    return book_title


def year_gen() -> int:
    year = randint(1900, 2010)
    return year


def pages_gen() -> int:
    pages = randint(150, 300)
    return pages


def isbn13_gen()-> str:
    isbn13 = faker.isbn13()
    return isbn13


def rating_gen() -> float:
    rating = random.uniform(0.0, 5.0)
    return rating


def price_gen() -> float:
    price = random.uniform(0.60, 13.0)
    return price


def author_gen() -> str:
    author = faker.name()
    return author


def book_gen(k=1) -> dict:
    while True:
        yield {
            "model": model,
            "pk": k,
            "fields": {
                "title": title_gen(),
                "year": year_gen(),
                "pages": pages_gen(),
                "isbn13": isbn13_gen(),
                "rating": rating_gen(),
                "price": price_gen(),
                "author":
                    author_gen()
                }
            }

        k += 1


list_books =[]


def main() -> None:
    book_generator = book_gen()
    for i in range(10):
        list_books.append(next(book_generator))


def _json() -> json:
    with open("data.json", "w") as file:
        json.dump(list_books, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
    _json()
