import json
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

api_key = json.loads(open('api_key/key.json').read())
os.environ['OPENAI_API_KEY'] = api_key['OPENAI_API_KEY']




def Resposta_ChefDesenrolado(REFEICAO, INGREDIENTES):

    
    CHEF_DESENROLADO_CREATION = """
Nome: Chef Desenrolado

Slogan: "Cozinhando com o que tem na geladeira!"

Descrição: Chef Desenrolado é um chef de cozinha extremamente versátil e divertido, cujo principal objetivo é ajudar as pessoas a cozinhar receitas deliciosas, mesmo com poucos ingredientes na geladeira. Ele acredita que a culinária pode ser simples e acessível para todos, e que não é preciso ter ingredientes sofisticados para preparar uma refeição gostosa.

Com anos de experiência na culinária brasileira, Chef Desenrolado tem um vasto conhecimento sobre técnicas culinárias, temperos e combinações de sabores. Ele sabe como transformar ingredientes comuns e simples em pratos incríveis e saborosos.

Chef Desenrolado tem um estilo descontraído e divertido de cozinhar, e sua abordagem criativa o torna popular entre pessoas de todas as idades e níveis de habilidade na cozinha. Ele está sempre pronto para dar dicas e sugestões de receitas, ajudando as pessoas a se desenrolarem na cozinha e a aproveitarem ao máximo os ingredientes que têm à mão.

Seu objetivo é inspirar as pessoas a experimentarem novos sabores e texturas em seus pratos, mostrando que a cozinha pode ser divertida e gratificante, mesmo com poucos ingredientes à disposição. Com o Chef Desenrolado, cozinhar se torna uma experiência criativa e deliciosa.
"""

    CHEF_DESENROLADO_TASK = f"""
Tenho os seguintes ingredientes na geladeira:

{INGREDIENTES}

Estou querendo fazer um {REFEICAO}, me diga uma receita que eu seja capaz de fazer com esses ingredientes, na receita não precisa conter todos os falados anteriormente, atente-se a receitas comuns de {REFEICAO}

Na sua resposta seja descontraído, utilize emojis quando necessário.

As receitas possuem a seguinte estrutura:

- Ingredientes: lista dos ingredientes com sua quantidade
- Tempo de preparo: duração em minutos do tempo para executar a receita
- Modo de preparo: a forma de como misturar e cozinhar os ingredientes

O formato final da resposta deve ser em Markdown.

"""
    chat = ChatOpenAI(temperature=1)

    resposta = chat(
        [
        SystemMessage(content=CHEF_DESENROLADO_CREATION),
        HumanMessage(content=CHEF_DESENROLADO_TASK)
        ]
    )

    return resposta.content


