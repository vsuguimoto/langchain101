import streamlit as st
from langchain101 import ChefDesenrolado



st.title('👨‍🍳💬 Chef Desenrolado')

ingredientes = st.multiselect(
    label='Ingredientes na geladeira',
    options=['Leite', 'Ovos', 'Queijo', 'Presunto', 'Tomate', 'Cebola', 'Alho', 'Batata', 'Cenoura', 'Abobrinha', 'Repolho', 'Couve-Flor', 'Brócolis', 'Frango', 'Carne Moída', 'Peixe', 'Arroz', 'Feijão', 'Pão', 'Manteiga']
)

refeicao = st.selectbox(
    label='Refeição',
    options=['Café da manhã', 'Almoço', 'Jantar']
)

submit_chef = st.button('O que consigo fazer Chef Desenrolado?')

if submit_chef:
    st.markdown(
        ChefDesenrolado.Resposta_ChefDesenrolado(
        REFEICAO=refeicao,
        INGREDIENTES=', '.join(ingredientes)
        )
    )
    
