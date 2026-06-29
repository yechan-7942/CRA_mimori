import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from crawlers.tavily_crawler import crawl

if __name__ == "__main__":
    keyword = input("검색할 밈/신조어 입력: ")
    docs = crawl(keyword)
    print(f"\n총 {len(docs)}개 문서 수집 완료")

