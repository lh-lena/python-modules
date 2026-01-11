# LangChain Examples

The project demonstrates document loading and text splitting techniques using LangChain

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env`. See `.env.example`

## Examples

### 01 - Document Loading (`01_document_loading.py`)

Demonstrates various document loaders:

#### PDF Loader
- Loads PDF documents
- Uses `PyPDFLoader`

#### Web Base Loader
- Scrapes web pages
- Requires `beautifulsoup4` and `lxml`

#### Notion Directory Loader
- Loads exported Notion pages (Markdown format)
- Processes multiple files from a directory

#### YouTube Audio Loader
- Downloads and transcribes YouTube videos
- Requires: `ffmpeg` (install via `brew install ffmpeg`)
- Requires: OpenAI API key for Whisper transcription

### 02 - Document Splitting (`02_document_splitting.py`)

Demonstrates text splitting strategies:

#### RecursiveCharacterTextSplitter
- Splits text recursively using multiple separators
- Maintains semantic coherence
- Configurable chunk size and overlap

#### CharacterTextSplitter
- Splits text using a single separator
- Simple and predictable splitting

#### TokenTextSplitter
- Splits text based on token count
- Useful for LLM token limits

#### MarkdownHeaderTextSplitter
- Context-aware splitting for Markdown documents
- Preserves header hierarchy in metadata
- Splits based on header levels (#, ##, ###)

Examples include:
- Basic text splitting with different chunk sizes
- PDF document splitting
- Notion document splitting
- Custom separator configurations

## Resources & Documentation

### LangChain
- [LangChain Documentation](https://python.langchain.com/)
- [Document Loaders Guide](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Text Splitters Guide](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [LangChain Community Loaders](https://python.langchain.com/docs/integrations/document_loaders/)

### Libraries Used
- [PyPDF](https://pypdf.readthedocs.io/) - PDF processing
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scraping
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloads
- [FFmpeg](https://ffmpeg.org/) - Audio/video processing

### Python Tools
- [Ruff](https://docs.astral.sh/ruff/) - Fast Python linter and formatter
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
