import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_summary(text):
    trimmed_text = text[:12000]

    prompt = f"""
You are a research paper assistant.

Read the paper content and produce a structured summary:

1. Title
2. Authors
3. One-paragraph overview
4. Research problem
5. Method / approach
6. Key findings
7. Why it matters
8. Limitations
9. Key takeaways
10. 3 suggested follow-up questions

Rules:
- Use plain English
- Do not invent information
- If something is unclear, say so
- Base everything only on the provided text

Paper:
{trimmed_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content