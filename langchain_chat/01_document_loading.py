import sys

sys.path.append("../..")

from dotenv import find_dotenv, load_dotenv
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader, NotionDirectoryLoader
from langchain_community.document_loaders.blob_loaders.youtube_audio import (
    YoutubeAudioLoader,
)
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import OpenAIWhisperParser

_ = load_dotenv(find_dotenv())

pdf_loader = PyPDFLoader("docs/sample.pdf")

pages = pdf_loader.load()
print("PDF Loader:\n")
print(len(pages))
page = pages[0]
# Print first 500 characters of the first page
print(page.page_content[:500])
print(page.metadata)

print("YouTube Audio Loader:\n")

# Rick Astley - Never Gonna Give You Up
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
save_dir = "docs/youtube"

try:
    youtube_loader = GenericLoader(
        YoutubeAudioLoader([url], save_dir), OpenAIWhisperParser()
    )
    youtube_docs = youtube_loader.load()
    print(len(youtube_docs))
    youtube_doc = youtube_docs[0]
    print(
        youtube_doc.page_content[:500]
    )  # Print first 500 characters of the transcript
    print(youtube_doc.metadata)
except Exception as e:
    print(f"Error loading YouTube video: {e}")
    print("To fix: brew install ffmpeg")

print("Web Base Loader:\n")

web_loader = WebBaseLoader("https://github.com/lh-lena/lh-lena/blob/main/README.md")
web_docs = web_loader.load()
print(len(web_docs))
web_doc = web_docs[0]
print(web_doc.metadata)

print("Notion Directory Loader:\n")

notion_loader = NotionDirectoryLoader("docs/notes")
notion_docs = notion_loader.load()
print(len(notion_docs))
if notion_docs:
    notion_doc = notion_docs[0]
    print(notion_doc.metadata)
else:
    print("No Notion documents found in docs/notes directory")

