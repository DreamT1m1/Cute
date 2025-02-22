from g4f.client import Client


client = Client()


class AIChat:
    models = ['gpt-4o', 'gpt-4o-mini']

    @staticmethod
    def generate_compliment() -> None:
        user_message = "Сделай незаурядный милый комплимент девушке, не слишком наигранный."

        response = client.chat.completions.create(
            model= AIChat.models[0],
            messages=[{"role": "user", "content": f"{user_message}"}],
            web_search=False
        )

        print(response.choices[0].message.content)
