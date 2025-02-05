from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Auto-Complete API",
    description="Generate relevant sentence completions based on context sentences"
)

class AutoCompleteRequest(BaseModel):
    user_sentence: str = Field(
        ...,
        description="The sentence to auto-complete",
        example="Please pray for my"
    )
    context_sentences: List[str] = Field(
        ...,
        description="The list of context sentences",
        example=["John has been sick", "The family needs support"]
    )
    sentence_type: Optional[str] = Field(
        None,
        description="The purpose of the sentence (e.g., 'Prayer Request', 'Gratitude')",
        example="Prayer Request"
    )

    class Config:
        schema_extra = {
            "example": {
                "user_sentence": "Please pray for my",
                "context_sentences": ["John has been sick", "The family needs support"],
                "sentence_type": "Prayer Request"
            }
        }

class AutoCompleteResponse(BaseModel):
    completions: List[str] = Field(
        ...,
        description="The list of completions/replacements ordered by relevance",
        example=[
            "Please pray for my brother John who is sick",
            "Please pray for my family during this difficult time"
        ]
    )

@app.post(
    "/autocomplete",
    response_model=AutoCompleteResponse,
    summary="Auto-complete a sentence based on context",
    response_description="Returns a list of potential completions"
)
async def autocomplete(request: AutoCompleteRequest) -> AutoCompleteResponse:
    try:
        # Your completion logic would go here
        # This is just a placeholder implementation
        completions = [
            f"{request.user_sentence} [completion 1]",
            f"{request.user_sentence} [completion 2]"
        ]
        
        return AutoCompleteResponse(completions=completions)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating completions: {str(e)}"
        )
