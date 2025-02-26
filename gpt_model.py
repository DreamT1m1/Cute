from g4f.client import Client


client = Client()


class AIChat:
    models = {
        'gpt-4o': 'gpt-4o',
        'gpt-4o-mini': 'gpt-4o-mini',
    }

    @staticmethod
    def generate_compliment() -> str:
        user_message = "Сделай комплимент девушке, только не банальный, и не слишком сентиментальный"

        response = client.chat.completions.create(
            model= AIChat.models['gpt-4o'],
            messages=[{"role": "user", "content": f"{user_message}"}],
            web_search=False
        )

        return response.choices[0].message.content
