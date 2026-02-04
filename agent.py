from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

def load_llm():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        torch_dtype=torch.float16
    )

    text_gen = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.2
    )

    return HuggingFacePipeline(pipeline=text_gen)

llm = load_llm()

SYSTEM_PROMPT = """
You are an agentic AI assistant.
You extract intent and slots.
Tasks:
- Uber booking
- Amazon ordering
- Blinkit grocery purchase
Never execute without explicit consent.
"""

agent = create_react_agent(
    llm=llm,
    tools=[],
    prompt=SYSTEM_PROMPT
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[],
    verbose=True
)
