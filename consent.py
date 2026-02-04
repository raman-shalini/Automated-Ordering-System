def verify_consent(user_input: str) -> bool:
    consent_keywords = ["yes", "confirm", "proceed", "ha", "haan"]
    return any(word in user_input.lower() for word in consent_keywords)
