# aiogram-bot-template<br/><br/><br/>

<img height="30em" src="https://raw.githubusercontent.com/anki-geo/ultimate-geography/a44a569a922e1d241517113e2917736af808eed7/src/media/flags/ug-flag-united_kingdom.svg" alt="English" align = "center"/>
This template is recommended to use in your Telegram bots written on <a href='https://github.com/aiogram/aiogram'>AIOgram</a>.
<br/><br/><br/>


<img height="30em" src="https://user-images.githubusercontent.com/104998959/210187883-4b95cab0-eb1c-4cba-98bf-29ccdb1d6716.png" alt="Uzbekistan" align = "center"/>
Ushbu shablondan Telegram botlarida foydalanish tavsiya etiladi <a href='https://github.com/aiogram/aiogram'>AIOgram</a>.
<br/><br/><br/>

<img height="30em" src="https://raw.githubusercontent.com/anki-geo/ultimate-geography/a44a569a922e1d241517113e2917736af808eed7/src/media/flags/ug-flag-russia.svg" alt="Russian" align = "center"/>
Этот шаблон рекомендуется использовать для создания ваших Telegram-ботов, написанных на <a href='https://github.com/aiogram/aiogram'>AIOgram</a>.

## About the template

**Structure:**

```
aiogram-bot-template/
├── app.py
├── __init__.py
├── config.py
├── loader.py
├── filters/
├── handlers/
└── middlewares/
```

- `aiogram-bot-template` is a project template that contains subpackages for **filters**, **handlers**,
    and **middleware**.

- The `filters` package contains classes that define **custom filters** for the bot's message handlers.

- The `handlers` package contains classes that define the bot's **message handlers**, which specify the actions to take
  in response to incoming messages.

- The `middlewares` package contains classes that define **custom middlewares** for the bot's dispatcher, which can be
  used to perform additional processing on incoming messages.
  
## Dockerfile
The `Dockerfile` defines the instructions for building the Docker image that is used by the bot service. The file begins
by specifying the base image that should be used for the image, which in this case is `python:3.9-buster`. The `ENV`
instruction sets the value of the `BOT_NAME` environment variable, which is used by the `WORKDIR` instruction to specify the
working directory for the container.

The `COPY` instructions are used to copy the `requirements.txt` file and the entire project directory into the image. The
`RUN` instruction is used to install the Python dependencies from the `requirements.txt` file. This allows the application
to run in the container with all the necessary dependencies.
