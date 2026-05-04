import json
import re
from langchain_ollama import ChatOllama
from decouple import config
from ddgs import DDGS

def search(query: str) -> str:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
    if not results:
        return "no results found"
    return "\n\n".join(
        f"Title: {r['title']}\nSnippet: {r['body']}"
        for r in results
    )

llm = ChatOllama(
    model=config("OLLAMA_MODEL", default="qwen2.5:7b-instruct"), 
    base_url=config("OLLAMA_BASE_URL", "http://localhost:11434/"),
    temperature=0
)

def getExtraPlayerInfo(player_name: str) -> dict:
    search_results = search(f"{player_name} NBA nicknames college university")

    prompt = f"""Based on these search results about NBA player {player_name}:

    {search_results}

    Return ONLY a valid JSON object in this exact format:
    {{"nicknames": ["nickname1", "nickname2"], "college": "University Name or null"}}

    Rules:
    - college should be null if they went straight from high school
    - nicknames should be an empty list if none are found
    - if the nickname is his name then dont include it
    """

    response = llm.invoke(prompt)
    text = response.content

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError(f"Could not parse response: {text}")