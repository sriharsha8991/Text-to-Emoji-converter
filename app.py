import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt = PromptTemplate.from_template("""You are an Emoji specialist who can convert any sentence into set of Emojis.Create most suitable emojis for {topic} Make sure to have check on number of Emojis you are using, Use the emojis only to required amount according to the sentence framed""")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

if __name__=="__main__":
    topic = "Try Something"
    resp = tweet_chain.run(topic=topic)
    print(resp)