from g4f.client import Client


client = Client()


class AIChat:
    models = ['gpt-4o', 'gpt-4o-mini']

    @staticmethod
    def generate_compliment() -> str:
        user_message = "Сделай не наигранный, не пошлый, не слишком банальный комплимент милой девушке"

        response = client.chat.completions.create(
            model= AIChat.models[0],
            messages=[{"role": "user", "content": f"{user_message}"}],
            web_search=False
        )

        return response.choices[0].message.content

