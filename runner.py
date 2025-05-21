# run_evaluation and main
import os
from dotenv import load_dotenv
from agents import planner, optimizer, reporter
from api_utils import get_route_google, get_weather, get_places_google, geocode_location
from prompts import prompt_variations

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def run_evaluation(start, end, units="metric"):
    results = []
    geo_ok, (lat, lon) = geocode_location(end)

    for style in prompt_variations:
        prompt = planner(start, end, style)
        response, scratchpad, latency, cost = optimizer(prompt, OPENAI_API_KEY)
        score, evaluation = reporter(response, OPENAI_API_KEY)
        route_ok, _ = get_route_google(start, end)
        weather_ok, _ = get_weather(lat, lon, units) if geo_ok else (False, {})
        poi_ok, _ = get_places_google(lat, lon) if geo_ok else (False, {})

        results.append({
            "style": style,
            "prompt": prompt,
            "response": response,
            "score": score,
            "evaluation": evaluation,
            "scratchpad": scratchpad,
            "latency_sec": latency,
            "estimated_cost_usd": cost,
            "route_ok": route_ok,
            "weather_ok": weather_ok,
            "poi_ok": poi_ok
        })

    return results



if __name__ == "__main__":
    print("Travel Planner - Powered by GPT")
    start = input("Enter starting location (e.g. San Francisco, CA): ")
    end = input("Enter destination location (e.g. Los Angeles, CA): ")
    units = input("Enter units (metric/imperial) [default: metric]: ") or "metric"

    evaluations = run_evaluation(start, end, units)

    for r in evaluations:
        print("\n====================")
        print(f"Prompt Style: {r['style']}")
        print(f"Prompt: {r['prompt']}")
        print(f"Scratchpad: {r['scratchpad']}")
        print(f"Score: {r['score']}")
        print(f"Latency (sec): {r['latency_sec']} | Estimated Cost: ${r['estimated_cost_usd']:.4f}")
        print(f"Route OK: {r['route_ok']} | Weather OK: {r['weather_ok']} | POI OK: {r['poi_ok']}")
        print(f"Agent Response: {r['response']}")
        print(f"Evaluation: {r['evaluation']}\n")