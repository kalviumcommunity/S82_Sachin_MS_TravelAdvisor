import config
import google.generativeai as genai

genai.configure(api_key=config.GOOGLE_API_KEY)


model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={
        "temperature": 0.9 
    }
)

def ask_model(prompt):
    response = model.generate_content(prompt)


    print("\nModel Response:\n", response.text)


    if hasattr(response, "usage_metadata"):
        tokens_in = response.usage_metadata.prompt_token_count
        tokens_out = response.usage_metadata.candidates_token_count
        total = response.usage_metadata.total_token_count

        print(f"\nToken Usage: Input={tokens_in}, Output={tokens_out}, Total={total}\n")
    else:
        print("\n Token usage metadata not available in this SDK.\n")

    return response


ask_model("Plan a 3-day trip to Rome focusing on history and food.")