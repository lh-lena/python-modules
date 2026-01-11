import os
import sys

import openai
from dotenv import find_dotenv, load_dotenv
from langchain_community.document_loaders import (
    NotionDirectoryLoader,
    PyPDFLoader,
)
from langchain_text_splitters import (
    CharacterTextSplitter,
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter,
)

sys.path.append("../..")


_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ["OPENAI_API_KEY"]

# Document Splitting Examples
chunk_size = 26
chunk_overlap = 4

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

text1 = "abcdefghijklmnopqrstuvwxyz"
print("Text 1:", text1)
rc = r_splitter.split_text(text1)
print("Recursive splitter result:", rc)

text2 = "abcdefghijklmnopqrstuvwxyzabcdefg"
print("\nText 2:", text2)
rc = r_splitter.split_text(text2)
print("Recursive splitter result:", rc)

text3 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
print("\nText 3:", text3)
rc = r_splitter.split_text(text3)
print("Recursive splitter result:", rc)

print("\nCharacter splitter (default separator):")
rc = c_splitter.split_text(text3)
print("Result:", rc)

print("\nCharacter splitter (space separator):")
c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=" "
)
rc = c_splitter.split_text(text3)
print("Result:", rc)

some_text = (
    "LangChain is a framework for developing applications powered by "
    "language models. It enables developers to build applications that "
    "can interact with data, manage state, and perform complex tasks by "
    "leveraging the capabilities of large language models. With LangChain, "
    "developers can create chatbots, virtual assistants, and other "
    "AI-powered applications that can understand and generate human-like text."
)
print("\nSome longer text:")
print("Length:", len(some_text))
r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150, chunk_overlap=0, separators=["\n\n", "\n", r"\. ", " ", ""]
)
rc = r_splitter.split_text(some_text)
print("Recursive splitter result:\n", rc)

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150, chunk_overlap=0, separators=["\n\n", "\n", r"(?<=\. )", " ", ""]
)
rc = r_splitter.split_text(some_text)
print("Recursive splitter result with regex separator:\n", rc)

print("PDF Document Splitting Example:\n")

pdf_loader = PyPDFLoader("docs/sample.pdf")
pages = pdf_loader.load()
print(f"Loaded {len(pages)} pages from PDF")
text_splitter = CharacterTextSplitter(
    separator="\n", chunk_size=1000, chunk_overlap=150, length_function=len
)
docs = text_splitter.split_documents(pages)
print(f"Split into {len(docs)} documents")

print("Notion Document Splitting Example:\n")

notion_loader = NotionDirectoryLoader("docs/notes")
notion_docs = notion_loader.load()
print(f"Loaded {len(notion_docs)} Notion documents")
notion_split_docs = text_splitter.split_documents(notion_docs)
print(f"Split into {len(notion_split_docs)} documents")

print("\nToken splitting example")

text_splitter = TokenTextSplitter(chunk_size=1, chunk_overlap=0)
text1 = "foo bar bazzyfoo"
text_splitter.split_text(text1)
text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=0)
docs = text_splitter.split_documents(pages)
print(f"Split into {len(docs)} documents")
print(docs[0])
print(f"Metadata of first page: {pages[0].metadata}")

print("\nContext aware splitting example")
markdown_document = """# Title\n\n \
## Chapter 1\n\n \
Hi this is Jim\n\n Hi this is Joe\n\n \
### Section \n\n \
Hi this is Lance \n\n\
## Chapter 2\n\n \
Hi this is Molly"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(markdown_document)
print("Markdown Header Splitter result: ", len(md_header_splits))
for i, split in enumerate(md_header_splits):
    print(f"--- Split {i + 1} ---")
    print(split)
    print()

print("\nNotion Directory Loader Example")
loader = NotionDirectoryLoader("docs/notes")
docs = loader.load()
txt = " ".join([d.page_content for d in docs])

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]
markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
md_header_splits = markdown_splitter.split_text(txt)
print("Markdown Header Splitter result: ", len(md_header_splits))
print("First split content:")
print(md_header_splits[0])
