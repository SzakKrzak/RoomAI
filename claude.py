from anthropic import Anthropic
from dotenv import load_dotenv

def main():
    load_dotenv()
    client = Anthropic()

    model_drawer = "claude-sonnet-4-6"
    model_trainer = "claude-haiku-4-5-20251001"

    prompt_text = (
        "Write a simple Python script for a user login system (username and password). "
        "Make it functional. Respond ONLY with the Python code inside ```python ``` blocks. "
        "Do not add any greetings or explanations."
    )

    system_b = (
        "You are a strict cybersecurity expert reviewing the provided Python code. "
        "Find the most critical security flaw (e.g., plaintext passwords, lack of rate limiting). "
        "DO NOT write the corrected code. Provide ONLY a short, direct instruction on what "
        "vulnerability to fix next. Be extremely concise."
        "Make the instructions more and more concise to inform with shortest message"
    )

    history_drawer = [{"role": "user", "content": prompt_text}]
    history_trainer = []


    for i in range(10):
        # DRAW
        response_a = client.messages.create(
            model=model_drawer,
            max_tokens=500,
            messages=history_drawer
        )
        msg_a = response_a.content[0].text
        print(f"AI A ({model_drawer}):\n{msg_a}\n")

        history_drawer.append({"role": "assistant", "content": msg_a})
        history_trainer.append({"role": "user", "content": msg_a})

        # Give feedback
        response_b = client.messages.create(
            model=model_trainer,
            max_tokens=200,
            system=system_b,
            messages=history_trainer
        )
        msg_b = response_b.content[0].text
        print(f"AI B ({model_trainer}):\n{msg_b}\n")
        print("-" * 40)

        history_trainer.append({"role": "assistant", "content": msg_b})
        history_drawer.append({"role": "user", "content": msg_b})


if __name__ == "__main__":
    main()