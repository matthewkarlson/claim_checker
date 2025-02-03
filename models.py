from pydantic import BaseModel
# Define Claim models
class Claim(BaseModel):
    description: str
    verifiable: bool
    opinion: bool

class Claims(BaseModel):
    claims: list[Claim]