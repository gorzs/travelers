# planner, optimizer, reporter
import time
import re
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from cost_utils import count_tokens_and_cost
from prompts import prompt_variations

def planner(start, end, style):
    return prompt_variations[style].format(start=start, end=end)

def optimizer(prompt_text, api_key):
    start_time = time.time()
    llm = ChatOpenAI(model="gpt-4", openai_api_key=api_key)
    response_obj = llm.invoke(prompt_text)
    response = str(response_obj.content) if hasattr(response_obj, "content") else str(response_obj)
    input_toks, output_toks, cost = count_tokens_and_cost(prompt_text, response)
    latency = round(time.time() - start_time, 3)
    return response, f"[OPTIMIZER] Received prompt: {prompt_text}", latency, cost

def reporter(response, api_key):
    llm = ChatOpenAI(model="gpt-4", openai_api_key=api_key)
    eval_prompt = PromptTemplate(
        input_variables=["response"],
        template="""
Evaluate the following travel plan response.

Response:
{response}

Criteria:
- Completeness
- Clarity
- Relevance
- Weather and POI considerations

Rate from 1 to 5 and explain. Format: Score: <1-5>. Reason: <...>
"""
    )
    chain = LLMChain(llm=llm, prompt=eval_prompt)
    evaluation = chain.invoke({"response": response})
    text = evaluation.get("answer", str(evaluation))
    match = re.search(r"Score:\s*(\d)", text)
    score = int(match.group(1)) if match else 3
    return score, evaluation
