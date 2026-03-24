import ollama

def main():
    model_a = 'phi3'
    model_b = 'llama3'

    # The starting prompt
    prompt_text = "Make an ascii painting of dog. Respond ONLY with this ascii painting."


    history_a = [{"role": "user", "content": prompt_text}]
    history_b = [{"role": "system", "content": "Correct the given image to make it look more like a dog. "
                                               "DON'T send corrected image. "
                                               "SEND ONLY instructions."
                                               "DON'T write things like 'good job'"
                                               "Make the feedback comment as short as possible"}]

    print("--- Starting Conversation ---")

    for i in range(10):
        # MODEL A
        response_a = ollama.chat(model=model_a, messages=history_a)
        msg_a = response_a['message']['content']
        print(f"AI A ({model_a}): {msg_a}\n")

        history_a.append({"role": "assistant", "content": msg_a})
        history_b.append({"role": "user", "content": msg_a})

        # MODEL B
        response_b = ollama.chat(model=model_b, messages=history_b)
        msg_b = response_b['message']['content']
        print(f"AI B ({model_b}): {msg_b}\n")

        history_b.append({"role": "assistant", "content": msg_b})
        history_a.append({"role": "user", "content": msg_b})

if __name__ == "__main__":
    main()