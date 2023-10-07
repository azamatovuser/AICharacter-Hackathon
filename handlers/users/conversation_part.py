from aiogram import types
from loader import dp, bot
import openai

openai.api_key = os.environ.get('OPENAI_KEY')

category = ''
person = ''


def answer_process(p, c, q):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=f"Bro you are {p} in {c} major and don't send dangerous information "
               f"and you need to answer to this question - {q}. Also and don't begin conversation with ? or , or .",
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
    text = 'I am not sure I understand :('
    return text


@dp.message_handler(content_types=['web_app_data'])
async def analyze_person(message: types.Message):
    category = message.text['category']
    person = message.text['person']
    await message.answer(f"I am {person} who specializes in {category}. "
                         f"It seems you want a conversation with me, "
                         f"is there anything that I can help? :0")


@dp.message_handler(content_types='text')
async def conversation(message: types.Message):
    if person == '':
        await message.answer('First Person needs to be chosen')
    else:
        temporary_message = await message.answer("Well give me time..")
        answer = answer_process(person, category, message.text)
        await bot.edit_message_text(chat_id=message.from_user.id, message_id=temporary_message.message_id, text=answer)