# LangChain Examples

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

## Document Loaders

### PDF Loader
- Loads PDF documents
- Uses `PyPDFLoader`

### Web Base Loader
- Scrapes web pages
- Requires `beautifulsoup4` and `lxml`

### Notion Directory Loader
- Loads exported Notion pages (Markdown format)
- Processes multiple files from a directory

### YouTube Audio Loader
- Downloads and transcribes YouTube videos
- Requires: `ffmpeg` (install via `brew install ffmpeg`)
- Requires: OpenAI API key for Whisper transcription

## Resources & Documentation

### LangChain
- [LangChain Documentation](https://python.langchain.com/)
- [Document Loaders Guide](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [LangChain Community Loaders](https://python.langchain.com/docs/integrations/document_loaders/)

### Libraries Used
- [PyPDF](https://pypdf.readthedocs.io/) - PDF processing
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web scraping
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloads
- [FFmpeg](https://ffmpeg.org/) - Audio/video processing

### Python Tools
- [Ruff](https://docs.astral.sh/ruff/) - Fast Python linter and formatter
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
