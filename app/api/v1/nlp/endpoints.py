from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.model import autocomplete_pipeline
from app.core.settings import settings

router = APIRouter()


class TextResponse(BaseModel):
    generated_texts: list[str]

@router.get("/autocomplete", response_model=TextResponse)
async def get_autocomplete(query: str):
    try:
        results = autocomplete_pipeline(
            query, 
            max_length=settings.max_length, 
            num_return_sequences=settings.num_return_sequences,
            truncation=True,  # Asegurarse de truncar las entradas
            pad_token_id=autocomplete_pipeline.tokenizer.eos_token_id  # Establecer pad_token_id
        )
        generated_texts = [result["generated_text"] for result in results]
        return TextResponse(generated_texts=generated_texts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
