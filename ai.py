# continuous_qa.py
# AI har naya sawaal poochega aur jawab dega, repeat nahi karega
# Stop karne ke liye Ctrl+C dabao

import json
import os

KNOWLEDGE_FILE = "knowledge_dynamic.json"

# load previous Q/A if exists
if os.path.exists(KNOWLEDGE_FILE):
    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        knowledge = json.load(f)
else:
    knowledge = {}

print("SimpleAI Dynamic — har naya sawaal ka jawab dega (exit likho band karne ke liye)")

try:
    while True:
        question = input("\nTum: ").strip()
        if question.lower() in ("exit", "quit"):
            print("SimpleAI: Alvida! (knowledge save ho gaya)")
            break

        # agar question already pucha ja chuka hai to use new reply pooche
        if question in knowledge:
            print(f"SimpleAI: Pehle seekha hua jawab: {knowledge[question]}")
        else:
            answer = input("SimpleAI: Is ka jawab kya hai? (tum mujhe sikhado): ").strip()
            if answer:
                knowledge[question] = answer
                # save immediately
                with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
                    json.dump(knowledge, f, ensure_ascii=False, indent=2)
                print(f"SimpleAI: Shukriya! Maine seekh liya: {answer}")
            else:
                print("SimpleAI: Koi jawab nahi diya, main seekh nahi paaya.")

except KeyboardInterrupt:
    print("\nSimpleAI: Program band hua. (Ctrl+C detected)")
# knowledge_dynamic.json mein save ho gaya