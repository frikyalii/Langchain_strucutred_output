from json import load
import struct
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional

load_dotenv()

model = ChatOpenAI()


#schema 
class Review(TypedDict):
    key_themes:Annotated[list[str],'write down key theme of the list as discussed in the review']
    summary:Annotated[str,'A brief summary of review']
    sentiment:Annotated[str,'A brief sentiment of the review either positive,negative,neutral']
    pros:Annotated[Optional[list[str]],'write down all the pros of the review']
    cons:Annotated[Optional[list[str]],'write down all the cons of the review']
    name:Annotated[Optional[str],'write a reviewer name']

structured_model =   model.with_structured_output(Review)

result = structured_model.invoke("""The Samsung Galaxy S25 is a premium smartphone with a 6.2-inch AMOLED display, Snapdragon processor, 50MP main camera, 4000mAh battery, 
and 25W fast charging. It offers excellent performance, a bright and 
smooth display, good cameras, and a compact design. However, the battery is
 relatively small, charging is slower than some competitors, and the base model 
 has limited storage options. Overall, it is a great choice for users who want a
  compact flagship phone with strong performance and cameras, but it may not be 
  ideal for heavy users who prioritize battery life and fast charging.
  review by asad ali""")

print(result)
print(result['summary'])
print(result['sentiment'])
print(result['name'])