import config
import google.generativeai as genai

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

system_prompt = (
        "You are a professional Travel Advisor.\n"
    "Here are examples of how you should respond:\n\n"

    "Example 1 Request: Plan a 3-day mid-budget trip to Rome in September. "
    "The traveler enjoys history and Italian food.\n"
    "Example 1 Response (JSON):\n"
    "{\n"
    "  'Destination(s)': 'Rome',\n"
    "  'Day-by-day Plan': [\n"
    "    'Day 1: Colosseum, Roman Forum, dinner in Trastevere',\n"
    "    'Day 2: Vatican Museums, St. Peter’s Basilica, pizza-making class',\n"
    "    'Day 3: Pantheon, Trevi Fountain, shopping, farewell dinner'\n"
    "  ],\n"
    "  'Costs (rough estimates)': '$700–$1000',\n"
    "  'Booking Tips': 'Book Vatican tickets in advance, use local trattorias for food',\n"
    "  'Local Do\\'s & Don\\'ts': 'Do learn Italian phrases; Don’t eat near tourist traps'\n"
    "}\n\n"
    
    "Now follow this style for any new request."
)

user_prompt = "Plan a 5-day mid-budget trip to Japan in October. We love history and food"

chat = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]}  
])


response = chat.send_message(user_prompt)
print(response.text)