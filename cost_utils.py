# tokens and costs calculations
import tiktoken

def count_tokens_and_cost(prompt, response, model="gpt-4"):
    if model == "gpt-4":
        encoding = tiktoken.encoding_for_model("gpt-4")
        input_tokens = len(encoding.encode(prompt))
        output_tokens = len(encoding.encode(response))
        cost = (input_tokens / 1000 * 0.03) + (output_tokens / 1000 * 0.06)
        return input_tokens, output_tokens, round(cost, 4)
    return 0, 0, 0.0
