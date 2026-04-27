#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv
from competitor_intelligence.crew import CompetitorIntelligence

load_dotenv()

def run():
    market      = sys.argv[1] if len(sys.argv) > 1 else "Mumbai ready-to-eat healthy snacks market"
    competitors = sys.argv[2] if len(sys.argv) > 2 else "EatFit, Slurrp Farm"

    os.makedirs("output", exist_ok=True)

    result = CompetitorIntelligence().crew().kickoff(inputs={
        "market":      market,
        "competitors": competitors,
    })

    print(result.raw)

if __name__ == "__main__":
    run()