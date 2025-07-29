# Setting Up the Environment with `uv` (a Fast Python Package Manager)

## 1. Install `uv` using brew (if you don't already have it)

```bash
brew install uv
```

## 2. Create and Activate a Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

## 3. Install Project Dependencies

```bash
uv pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file in the root directory of the project and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

> **Note:** Never commit your `.env` file to version control. Add it to your `.gitignore`.
