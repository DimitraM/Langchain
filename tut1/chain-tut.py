from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
import os
import httpx

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key and base URL
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE_URL")
ca_bundle = os.getenv("REQUESTS_CA_BUNDLE")

# Create a custom HTTP client with SSL verification using the CA bundle
class CustomHTTPClient(httpx.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verify = ca_bundle

# Initialize the custom HTTP client
custom_client = CustomHTTPClient()

# Initialize the ChatOpenAI model with the custom HTTP client
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=api_key,
    base_url=base_url,
    temperature=0,
    client=custom_client  # Pass the custom HTTP client
)


template = "calculate the square of {x}"

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({ "x": 12 })
result = model.invoke(prompt)

# Print the response
print(result)
