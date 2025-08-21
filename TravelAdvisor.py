import config
import google.generativeai as genai

genai.configure(api_key=config.GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()



destination = "Switzerland"
days = 5
budget = "mid-budget"
month = "April"
interests = ["mountains","skiing"]
origin = "Japan"

user_prompt = f"""
Plan a {days}-day {budget} trip to {destination} in {month}.
The traveler is coming from {origin} and enjoys {", ".join(interests)}.
Respond in JSON with this structure:

1) Destination(s)
2) Day-by-day Plan
3) Costs (rough estimates)
4) Booking Tips
5) Local Do's & Don'ts
"""



chat = model.start_chat()


response = chat.send_message(user_prompt)

print(response.text)