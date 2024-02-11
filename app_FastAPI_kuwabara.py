from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextData(BaseModel):
    text: str

@app.post("/count_words")
def count_words(text_data: TextData):

    words = text_data.text.split()
    count = len(words)
    return {"word_count": count}
