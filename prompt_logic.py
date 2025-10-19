# prompt_logic.py
# SmartPitch UI - Outreach Message Generator (Offline Logic)
# Built by Eva & Rohan 💛

import random

def generate_pitch(client_name, client_type, service, platform, tone):
    """
    Generates a personalized outreach message using given user inputs.
    Works offline – no API keys required.
    """

    tone_styles = {
        "friendly": [
            f"Hey {client_name}! I came across your {client_type} and instantly loved the vibe.",
            f"Hi {client_name}, hope you’re doing great! I saw your {client_type} and wanted to share a quick idea."
        ],
        "professional": [
            f"Hello {client_name}, I recently viewed your {client_type} and thought to reach out with a valuable idea.",
            f"Dear {client_name}, I noticed your work in {client_type} and I believe my service could enhance it."
        ],
        "confident": [
            f"Hi {client_name}, I’ve helped several {client_type}s like yours boost results — I can do the same for you.",
            f"Hey {client_name}, your {client_type} caught my attention, and I’m confident I can help scale it."
        ]
    }

    tone = tone.lower().strip() if tone else "friendly"
    intro = random.choice(tone_styles.get(tone, tone_styles["friendly"]))

    body = f"I specialize in {service}, and I’ve built tools that make client work faster and more efficient."

    closings = {
        "linkedin": "Would you be open to a short chat here on LinkedIn this week?",
        "upwork": "I’ve sent a proposal on Upwork as well – would love to discuss your project there!",
        "email": "If you’d like more details, I can share quick examples via email.",
        "instagram": "Your page really inspired me — would love to collab sometime!",
        "default": "Let me know if this sounds useful!"
    }

    closing = closings.get(platform.lower(), closings["default"])

    message = f"{intro}\n\n{body}\n\n{closing}\n\n– {service.title()} Specialist, Rohan 💛"
    return message

