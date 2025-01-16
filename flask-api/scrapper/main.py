import feedparser
from sentence_transformers import SentenceTransformer
from bs4 import BeautifulSoup
import numpy as np
import json


RSS_VSD = [
    "https://vsd.fr/actu-people/feed/",
    "https://vsd.fr/tele/feed/",
    "https://vsd.fr/societe/feed/",
    "https://vsd.fr/culture/feed/",
    "https://vsd.fr/loisirs/feed/"
]

RSS_PUBLIC = [
    "https://www.public.fr/feed",
    "https://www.public.fr/people/feed",
    "https://www.public.fr/tele/feed",
    "https://www.public.fr/lifestyle/mode-beaute/feed",
    "https://www.public.fr/people/royaute/feed"
]


class Article:
    def __init__(self, url: str, title: str, author: str, summary: str, content: str):
        self.url = url
        self.title = title
        self.author = author,
        self.summary = summary
        self.content = content

    def to_dict(self):
        return {
            "url": self.url,
            "title": self.title,
            "author": self.author,
            "summary": self.summary,
            "content": self.content
        }

    def __hash__(self):
        return hash(self.url)

    def __eq__(self, other):
        if isinstance(other, Article):
            return self.url == other.url
        return False

    def __str__(self):
        return f"{self.title}\n{self.url}\n{self.author}\n{self.summary}\n{self.content}"


def purge_html(content: str) -> str:
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text()


def extract_all_articles():
    print("Extracting all the articles from RSS feeds...")
    # Making a set to avoid duplicates
    articles: set[Article] = set()
    fake_content = [{"value": ""}]
    for url in RSS_VSD + RSS_PUBLIC:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            article_url = entry.get("id", "")
            title = entry.get("title", "")
            author = entry.get("author", "")
            summary = entry.get("summary", "")
            content = purge_html(entry.get("content", fake_content)[
                                 0].get("value", ""))
            articles.add(Article(article_url, title, author, summary, content))
    print(f"Articles extracted ✅ ({len(articles)} total)")
    return list(articles)


def main():
    articles = extract_all_articles()

    model_name = "all-MiniLM-L6-v2"
    print(f"Loading the '{model_name}' model...")
    model = SentenceTransformer(model_name)
    print("Model loaded ✅")

    print("Creating all embeddings for the articles...")
    embeddings = model.encode([str(article)for article in articles], show_progress_bar=True)
    print("Articles embeddings created ✅")

    np.save("embeddings.npy", embeddings)
    print("All tensor data saved in the 'embeddings.npy' file ✅")

    data = [article.to_dict() for article in articles]
    with open("articles.json", "w") as file:
        json.dump(data, file)
    print("All articles saved in the 'articles.json' file ✅")


if __name__ == "__main__":
    main()
