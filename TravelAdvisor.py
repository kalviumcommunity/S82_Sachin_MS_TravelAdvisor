import config
import google.generativeai as genai

genai.configure(api_key=config.GOOGLE_API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")

user_prompt = """
Plan a 5-day budget-friendly trip to Italy in October.
The traveler loves history and food. Respond in JSON.

Think step by step:
1. Analyze the travel month (October) and suggest suitable cities.
2. Consider the budget and how it affects travel style.
3. Pick activities related to history and food.
4. Allocate activities across 5 days logically.
5. Estimate costs, bookings, and tips.
Finally, present the output in this JSON structure:
1) Destination(s)
2) Day-by-day Plan
3) Costs (rough estimates)
4) Booking Tips
5) Local Do's & Don'ts
"""

chat = model.start_chat()
response = chat.send_message(user_prompt)
print(response.text)