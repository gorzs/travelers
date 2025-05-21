# Travel Planner - MCP-Style Agent System

## Overview

This project implements a modular, collaborative agent system for generating, optimizing, and evaluating travel plans using large language models (LLMs) and external APIs. The solution was built as part of the CloudFactory Technical Case Study and fully satisfies the outlined requirements.

-------

## Agent Architecture

The system follows the **MCP-style agent pattern**, with three collaborating agents:

| Agent   | Responsibility                                      |
|---------|------------------------------------------------------|
| planner | Generates the travel prompt based on user intent    |
| optimizer | Uses GPT-4 to produce a travel plan from the prompt |
| reporter | Evaluates the plan using an LLM and scoring rubric  |

Agents share information via structured prompts and inputs, forming a coherent pipeline.

----

##  Prompt Variants

Three distinct prompt styles are used to explore model behavior:

- **Casual** – conversational tone, scenic routes and food stops
- **Precise** – minimal breaks, fastest route
- **Weather-sensitive** – scenic route that avoids bad weather and includes natural attractions

Each prompt is dynamically generated using the `planner` agent.

-------

##  Evaluation Criteria

For each plan, the following are evaluated:

- Valid route generation via Google Maps API
- Weather data from OpenWeather API
- POIs near destination via Google Places API
- LLM-based score on:
    - Completeness
    - Clarity
    - Relevance
    - Consideration of POIs and weather

The reporter uses GPT-4 to score the plan from 1 to 5 and generate rationale.

---

## Token Cost & Performance

The system calculates token usage and estimated cost per prompt:

- GPT-4 pricing (as of May 2025):
    - $0.03 / 1K input tokens
    - $0.06 / 1K output tokens
- Latency and cost are logged for each prompt evaluation

---

## Unit Tests

Tests included using Python’s `unittest`:

- API coverage: Routes, Weather, Places
- Prompt effectiveness: Ensures scoring logic runs for all prompt types

---

## Setup


### Requirements

- Python 3.10+
- API keys from:
    - OpenAI
    - Google Maps (Directions, Geocoding, Places)
    - OpenWeatherMap

### Install Dependencies

```bash
pip install -r requirements.txt
```
### .env File
Create a .env file with:
OPENAI_API_KEY=your-openai-key
GOOGLE_MAPS_KEY=your-google-maps-key
OPENWEATHER_API_KEY=your-openweather-key

---------------
### How to Run
Launch the program from terminal:
```bash
python runner.py
```
Then, follow the prompts:
```
Travel Planner - Powered by GPT
Enter starting location (e.g. San Francisco, CA):
Enter destination location (e.g. Los Angeles, CA):
Enter units (metric/imperial) [default: metric]: 
```


-----

## File Structure



```
travel_experience_app/
├── agents.py              # planner, optimizer, reporter agents
├── api_utils.py           # weather, geocoding, directions, POIs
├── cost_utils.py          # token counting and cost estimation
├── prompts.py             # styles of prompt templates
├── runner.py              # console input + main execution logic
├── test_travel.py         # unit tests
├── .env                   # environment variables
├── requirements.txt       # dependencies
└── README.md              # this file
```

## Conversation example

(.venv) PS E:\Users\gabrielaortiz\Downloads\Travel_experience_app> python.exe .\runner.py
Travel Planner - Powered by GPT
Enter starting location (e.g. San Francisco, CA): Mexico City
Enter destination location (e.g. Los Angeles, CA): Aguascalientes
Enter units (metric/imperial) [default: metric]:
E:\Users\gabrielaortiz\Downloads\Travel_experience_app\agents.py:15: LangChainDeprecationWarning: The class `ChatOpenAI` was deprecated in LangChain 0.0.10 and will be removed in 1.0. An updated version of the class exists in the :class:`~langchain-openai package and should be used instead. To use it run `pip install -U :class:`~langchain-openai` and import as `from :class:`~langchain_openai import ChatOpenAI``.
  llm = ChatOpenAI(model="gpt-4", openai_api_key=api_key)
E:\Users\gabrielaortiz\Downloads\Travel_experience_app\agents.py:41: LangChainDeprecationWarning: The class `LLMChain` was deprecated in LangChain 0.1.17 and will be removed in 1.0. Use :meth:`~RunnableSequence, e.g., `prompt | llm`` instead.
chain = LLMChain(llm=llm, prompt=eval_prompt)

====================
Prompt Style: casual
Prompt: Hey! I wanna go on a road trip from Mexico City to Aguascalientes with great views. Can you make it cool and chill, maybe with some good food stops?
Scratchpad: [OPTIMIZER] Received prompt: Hey! I wanna go on a road trip from Mexico City to Aguascalientes with great views. Can you make it cool and chill, maybe with some good food stops?
Score: 4
Latency (sec): 18.003 | Estimated Cost: $0.0267
Route OK: True | Weather OK: True | POI OK: True
Agent Response: Sure, that sounds like a great adventure! Here's a suggested itinerary for your road trip from Mexico City to Aguascalientes that includes some interesting and beautiful stops along the way:

Day 1: Mexico City to Queretaro - 3 hours drive

Start your road trip by heading to Queretaro. This city is known for its well-preserved Spanish colonial architecture. Take a walk around the city center and enjoy its beautiful plazas and historic buildings. For food, try "Pacholas Queretanas", a traditional dish made from ground beef.

Day 2: Queretaro to San Miguel de Allende - 1 hour drive

Drive to San Miguel de Allende, a charming colonial-era town known for its baroque Spanish architecture, thriving arts scene, and cultural festivals. Have lunch at one of the many traditional Mexican restaurants in the city.

Day 3: San Miguel de Allende to Guanajuato - 1.5 hours drive

Guanajuato is a beautiful city with colorful houses and narrow, winding streets. It's also a UNESCO World Heritage site. Try the local dish "Enchiladas Mineras", a type of enchilada that is a specialty of Guanajuato.

Day 4: Guanajuato to Leon - 1 hour drive

Leon is known as the leather capital of Mexico. Take some time to browse the leather goods in the Zona Piel district. For food, try "Guacamayas", a traditional sandwich made with pork rind, avocado, and hot sauce.

Day 5: Leon to Aguascalientes - 2 hours drive

Finally, you'll reach your destination, Aguascalientes. This city is known for its hot springs, hence the name "Hot Waters". Check out the Museo Nac
ional de la Muerte, a museum dedicated to the cultural significance of death in Mexico. For food, try the "Birria", a spicy stew made from goat meat or mutton.

Remember to take your time and enjoy the scenery along the way. Happy road tripping!
Evaluation: {'response': 'Sure, that sounds like a great adventure! Here\'s a suggested itinerary for your road trip from Mexico City to Aguascalien
tes that includes some interesting and beautiful stops along the way:\n\nDay 1: Mexico City to Queretaro - 3 hours drive\n\nStart your road trip by
heading to Queretaro. This city is known for its well-preserved Spanish colonial architecture. Take a walk around the city center and enjoy its beau
tiful plazas and historic buildings. For food, try "Pacholas Queretanas", a traditional dish made from ground beef.\n\nDay 2: Queretaro to San Migue
l de Allende - 1 hour drive\n\nDrive to San Miguel de Allende, a charming colonial-era town known for its baroque Spanish architecture, thriving art
s scene, and cultural festivals. Have lunch at one of the many traditional Mexican restaurants in the city. \n\nDay 3: San Miguel de Allende to Guan
ajuato - 1.5 hours drive\n\nGuanajuato is a beautiful city with colorful houses and narrow, winding streets. It\'s also a UNESCO World Heritage site
. Try the local dish "Enchiladas Mineras", a type of enchilada that is a specialty of Guanajuato.\n\nDay 4: Guanajuato to Leon - 1 hour drive \n\nLe
on is known as the leather capital of Mexico. Take some time to browse the leather goods in the Zona Piel district. For food, try "Guacamayas", a tr
aditional sandwich made with pork rind, avocado, and hot sauce.\n\nDay 5: Leon to Aguascalientes - 2 hours drive\n\nFinally, you\'ll reach your dest
ination, Aguascalientes. This city is known for its hot springs, hence the name "Hot Waters". Check out the Museo Nacional de la Muerte, a museum de
dicated to the cultural significance of death in Mexico. For food, try the "Birria", a spicy stew made from goat meat or mutton.\n\nRemember to take
your time and enjoy the scenery along the way. Happy road tripping!', 
'text':
'Score: 4.5. 
Reason: The response is well-structured, clear, and relevant to the plan of a road trip from Mexico City to Aguascalientes. It provides a detailed day by day itinerary including driving times, description
of each city, and local food recommendations which is helpful. However, the response lacks information regarding weather considerations and detailed information about Points of Interest (POIs). These aspects are important for a travel plan to be fully complete.'}


====================
Prompt Style: precise
Prompt: Plan the fastest driving route from Mexico City to Aguascalientes, minimizing traffic and stopping only for fuel and restroom breaks.       
Scratchpad: [OPTIMIZER] Received prompt: Plan the fastest driving route from Mexico City to Aguascalientes, minimizing traffic and stopping only for fuel and restroom breaks.
Score: 4
Latency (sec): 12.759 | Estimated Cost: $0.0186
Route OK: True | Weather OK: True | POI OK: True
Agent Response: Starting from Mexico City, here are the steps to reach Aguascalientes:

1. Get on Autopista Paseo de la Reforma/México 57D from Calle Moliere and Calle Kepler (7 min - 2.4 km).
2. Follow Autopista Paseo de la Reforma/México 57D and Mexico 57D to San Juan del Río. Take the exit toward Qro. Centro/San Juan Del Río from Mexico 57D (1 hr 57 min - 163 km).
3. Take Av. Central and Mexico 120 to your destination in La Estancia (3 min - 1.7 km).
4. Continue on Mexico 120. Take Mexico 45D to Calle Nieto in Barrio de la Estación, Aguascalientes (3 hr 19 min - 312 km).
5. Follow Calle Nieto and Calle Moctezuma to Calle Primo Verdad (6 min - 1.7 km).

This route takes approximately 5 hours and 32 minutes, and covers a distance of 481 kilometers. This route is the fastest, and it also considers the traffic. However, traffic conditions can vary, so it's always a good idea to check before you leave.

The route also includes tolls. Make sure to plan your fuel and restroom breaks according to your personal needs and the availability of services along the route.
Evaluation: {'response': "Starting from Mexico City, here are the steps to reach Aguascalientes:\n\n1. Get on Autopista Paseo de la Reforma/México 5
7D from Calle Moliere and Calle Kepler (7 min - 2.4 km).\n2. Follow Autopista Paseo de la Reforma/México 57D and Mexico 57D to San Juan del Río. Tak
e the exit toward Qro. Centro/San Juan Del Río from Mexico 57D (1 hr 57 min - 163 km).\n3. Take Av. Central and Mexico 120 to your destination in La
Estancia (3 min - 1.7 km).\n4. Continue on Mexico 120. Take Mexico 45D to Calle Nieto in Barrio de la Estación, Aguascalientes (3 hr 19 min - 312 k
m).\n5. Follow Calle Nieto and Calle Moctezuma to Calle Primo Verdad (6 min - 1.7 km).\n\nThis route takes approximately 5 hours and 32 minutes, and
covers a distance of 481 kilometers. This route is the fastest, and it also considers the traffic. However, traffic conditions can vary, so it's al
ways a good idea to check before you leave.\n\nThe route also includes tolls. Make sure to plan your fuel and restroom breaks according to your pers
onal needs and the availability of services along the route.", 
'text': 
'Score: 4.5. 
Reason: The response is very detailed and gives clear directions. It is also relevant and includes information about tolls, travel time, and distance. However, it does not consider weather conditions or points of interest along the route. It also does not provide alternatives for different travel preferences or conditions.'}


====================
Prompt Style: weather_sensitive
Prompt: Plan a scenic drive from Mexico City to Aguascalientes, avoiding bad weather. I’d like to stop at natural attractions and only travel during good conditions.
Scratchpad: [OPTIMIZER] Received prompt: Plan a scenic drive from Mexico City to Aguascalientes, avoiding bad weather. I’d like to stop at natural attractions and only travel during good conditions.
Score: 4
Latency (sec): 17.44 | Estimated Cost: $0.0295
Route OK: True | Weather OK: True | POI OK: True
Agent Response: Day 1: Depart Mexico City

Start your trip in the vibrant heart of Mexico City. Before you leave, you may want to explore the city's rich history and culture, such as the Palacio Nacional, Templo Mayor or the Frida Kahlo Museum.

From Mexico City, start your drive northwest on the 57D towards Querétaro. This will take you approximately two hours, depending on traffic.

Stop 1: Querétaro

Querétaro is a small city known for its Spanish colonial architecture. You can stroll through the historic city center, visit the aqueduct, or explore the local parks.

Day 2: Depart Querétaro

Leave Querétaro and continue your journey on the 57D. This will take you through the Sierra Gorda Biosphere Reserve, which is a great spot for hiking and bird-watching.

Stop 2: Sierra Gorda Biosphere Reserve

Sierra Gorda is home to a diverse range of wildlife and plant species. Here, you can take a break from your drive and immerse yourself in nature. There are various hiking trails and viewpoints, where you can admire the stunning landscapes.

Day 3: Depart Sierra Gorda Biosphere Reserve

After spending a day in the Sierra Gorda Biosphere Reserve, continue your journey to San Luis Potosí. This part of the drive will take you approximately 4 hours, on the 57D and then the 80D.

Stop 3: San Luis Potosí

San Luis Potosí is known for its beautiful colonial architecture and vibrant culture. You may want to visit the city center, the Cathedral of San Luis Potosí, or the Museum of Contemporary Art.

Day 4: Depart San Luis Potosí

Leave San Luis Potosí and head south on the 54 towards Aguascalientes. This drive will take you approximately 2 hours.

Arrival: Aguascalientes

Aguascalientes is a charming city known for its hot springs, colonial architecture, and lively festivals. You may want to visit the National Museum of Death, the Aguascalientes Museum, or the San Marcos Garden.

Please note, this plan is subject to change depending on the weather conditions. Always check the weather forecast for each day and adjust your plans accordingly. Safe travels!
Evaluation: {'response': "Day 1: Depart Mexico City \n\nStart your trip in the vibrant heart of Mexico City. Before you leave, you may want to explo
re the city's rich history and culture, such as the Palacio Nacional, Templo Mayor or the Frida Kahlo Museum. \n\nFrom Mexico City, start your drive
northwest on the 57D towards Querétaro. This will take you approximately two hours, depending on traffic.\n\nStop 1: Querétaro\n\nQuerétaro is a sm
all city known for its Spanish colonial architecture. You can stroll through the historic city center, visit the aqueduct, or explore the local park
s. \n\nDay 2: Depart Querétaro\n\nLeave Querétaro and continue your journey on the 57D. This will take you through the Sierra Gorda Biosphere Reserv
e, which is a great spot for hiking and bird-watching. \n\nStop 2: Sierra Gorda Biosphere Reserve\n\nSierra Gorda is home to a diverse range of wild
life and plant species. Here, you can take a break from your drive and immerse yourself in nature. There are various hiking trails and viewpoints, w
here you can admire the stunning landscapes.\n\nDay 3: Depart Sierra Gorda Biosphere Reserve\n\nAfter spending a day in the Sierra Gorda Biosphere R
eserve, continue your journey to San Luis Potosí. This part of the drive will take you approximately 4 hours, on the 57D and then the 80D.\n\nStop 3
: San Luis Potosí\n\nSan Luis Potosí is known for its beautiful colonial architecture and vibrant culture. You may want to visit the city center, th
e Cathedral of San Luis Potosí, or the Museum of Contemporary Art.\n\nDay 4: Depart San Luis Potosí\n\nLeave San Luis Potosí and head south on the 5
4 towards Aguascalientes. This drive will take you approximately 2 hours. \n\nArrival: Aguascalientes\n\nAguascalientes is a charming city known for
its hot springs, colonial architecture, and lively festivals. You may want to visit the National Museum of Death, the Aguascalientes Museum, or the
San Marcos Garden.\n\nPlease note, this plan is subject to change depending on the weather conditions. Always check the weather forecast for each d
ay and adjust your plans accordingly. Safe travels!", 
'text': 
'Score: 4.5. 
Reason: The response is very detailed and well organized. It provides cle
ar instructions on the route to take and estimated travel times. It also suggests a variety of interesting points of interest at each stop, catering
to a range of tastes. The response also sensibly advises the traveler to check the weather forecast and adjust their plans accordingly. The only minor issue is that it does not mention any accommodation or meal planning, which are usually included in a complete travel plan, thus the slight reduction in score.'}

(.venv) PS E:\Users\gabrielaortiz\Downloads\Travel_experience_app> 