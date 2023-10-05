from aiogram import types
from loader import dp, bot
import openai

openai.api_key = os.environ.get('OPENAI_KEY')


def answer_process(person, category, question):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f"Bro you are {person} in {category} major and don't send dangerous information "
               f"and you need to answer to this question - {question}. Also and don't begin conversation with ? or , or .",
        max_tokens=1000,
    )
    if response['choices'][0]['text']:
        answer = response['choices'][0]['text']
        answer.replace("_", "\\_")
        answer.replace("*", "\\*")
        answer.replace("[", "\\[")
        answer.replace("`", "\\`")
        answer.replace("=", "\\=")
        return answer
    text = 'Я совсем не понял вас :('
    return text


@dp.message_handler(content_types=['web_app_data'])
async def hey(message: types.Message):
    await message.answer('Accepted!')