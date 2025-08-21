import config
import google.generativeai as genai

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

system_prompt = (
    "You are a professional Travel Advisor. "
    "Your job is to propose destinations, day-by-day itineraries, and practical travel tips. "
    "ALWAYS consider: budget, trip duration, origin (if provided), time of year/season, and traveler interests. "
    "Respond in this exact structure:\n"
    "1) Destination(s)\n2) Day-by-day Plan\n3) Costs (rough estimates)\n"
    "4) Booking Tips\n5) Local Do's & Don'ts\n"
    "Be concise, friendly, and specific. Avoid filler text."
    "In Json format with no comments"
)

user_prompt = "Plan a 5-day mid-budget trip to Italy in October. We love history and food.We are from India"

chat = model.start_chat(history=[
    {"role": "user", "parts": [system_prompt]}  
])


response = chat.send_message(user_prompt)
print(response.text)