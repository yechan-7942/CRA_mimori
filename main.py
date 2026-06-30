import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from crawlers.tavily_crawler import crawl
from crawlers.youtube_crawler import crawl_youtube

if __name__ == "__main__":
    keyword = input("검색할 밈/신조어 입력: ")
    tavily_crawler_docs = crawl(keyword)
    youtube_crawler_docs = crawl_youtube(keyword)

    docs = tavily_crawler_docs + youtube_crawler_docs
    print(f"\nTavily : {len(tavily_crawler_docs)}개, Youtube:{len(youtube_crawler_docs)}개")
    print(f"총{len(docs)}개 수집 완료")