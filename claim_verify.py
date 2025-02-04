from models import Claims,Claim
import requests
claims=Claims(claims=[Claim(description='Trump recently signed an executive order to start a trade war with Canada, Mexico, and China.', verifiable=True, opinion=False), Claim(description='Trump announced new tariffs on China, Canada, and Mexico.', verifiable=True, opinion=False), Claim(description='There is a claim that 83% of Trump supporters support the tariffs.', verifiable=True, opinion=False), Claim(description='The speaker claims that tariffs are like an aggressive universal sales tax because importers will pass the cost onto consumers.', verifiable=True, opinion=True), Claim(description='The speaker suggests Trump wants to destroy income tax and replace it with tariffs,A which are seen as regressive tax.', verifiable=False, opinion=True), Claim(description="The Chamber of Commerce released a statement opposing Trump's tariffs, saying they will only raise prices for American families and disrupt supply chains.", verifiable=True, opinion=False), Claim(description='The speaker argues tariffs do not work as Trump claims and instead increase costs for consumers.', verifiable=True, opinion=True), Claim(description='The United States has a significant trade relationship with Canada for materials like wood.', verifiable=True, opinion=False), Claim(description='Tariffs can lead to retaliatory measures from other countries like when China imposed tariffs on soybeans in response to US tariffs on steel.', verifiable=True, opinion=False), Claim(description='There is an opinion that if there are tariffs, consumers will not recognize higher prices are due to those tariffs.', verifiable=False, opinion=True), Claim(description='The US Chamber of Commerce warns that tariffs will harm mainstream businesses and not solve issues like the border crisis and fentanyl.', verifiable=True, opinion=False), Claim(description='A large percentage of products imported from Canada and Mexico are essential in US manufacturing, including auto parts.', verifiable=True, opinion=False), Claim(description='The speaker claims the current global trade system maximizes profits but can lead to significant cost increases and supply shortages with tariffs.', verifiable=True, opinion=True), Claim(description='The parts for cars manufactured in the United States often come from Canada and Mexico, leading to potential cost increases if tariffs are applied.', verifiable=True, opinion=False), Claim(description='In the United States, 54% of adults have literacy below a sixth-grade level, and 21% are illiterate.', verifiable=True, opinion=False), Claim(description='Newsmax host taunted people by eating a taco on the air while discussing Latino migrant deportations.', verifiable=True, opinion=False), Claim(description='The speaker expresses disdain for certain media personalities and their tactics, indicating they believe it results from spite and hate.', verifiable=False, opinion=True)])
import asyncio
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

async def verify_claim(claim: Claim):
    params = {
            "api_key": SERPAPI_KEY,
            "engine": "google",
            "q": claim.description,
            "location": "Austin, Texas, United States",
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en"
                }

    search = await GoogleSearch(params)
    results = search.get_dict()
    return results

async def verify_claims(claims: Claims):
    return await asyncio.gather(
        *[verify_claim(claim) for claim in claims.claims if claim.verifiable]
    )