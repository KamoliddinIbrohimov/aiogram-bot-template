from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states.test import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("You have started the test\n"
                         "Question 1.\n\n"
                         "Are you a programmer?")

    await Test.Q1.set()
    # await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    #Method 1
    await state.update_data(answer1=answer)
    ##Method 2
    # await state.update_data(
    #     {
    #         "answer1": answer
    #     }
    # )
    ##Method 3
    # async with state.proxy() as data:
    #     data["answer1"] = answer
    await message.answer("Question 2\n\n"
                         "Do you have a computer?")
    await Test.Q2.set()
    # await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Thanks for your reply!")
    await message.answer(f"Answer-1: {answer1}\n"
                         f"Answer-2: {answer2}")

    await state.reset_state()
    #await state.reset_state(with_data=False)