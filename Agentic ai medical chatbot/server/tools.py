# Step1: Setup Ollama with Medgemma tool
import ollama

def query_medicalbot(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    
    try:
        response = ollama.chat(
            model='llama3.2:latest',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."

from twilio.rest import Client
def call_emergency(emergencynumber):
    client = Client("your_account_sid", "your_auth_token")
    call = client.calls.create(
        to="give_911_number_or_your_own_number",
        from_="number_given_by_twilio",
        url="http://demo.twilio.com/docs/voice.xml"  # Can customize message
    )

