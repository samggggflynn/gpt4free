import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

import streamlit as st
from gpt4free import you
from gpt4free import quora, forefront, theb


def get_answer(question: str) -> str:
    # Set cloudflare clearance cookie and get answer from GPT-4 model
    try:
        # result = you.Completion.create(prompt=question)
        # result = quora.Completion.create(prompt=question)
        result = quora.StreamingCompletion.create(prompt=question)  # Streaming mode
        # result2 = forefront.StreamingCompletion.create(prompt=question)  # Streaming mode for forefront
        # return result.text   # if Completion is used
        return result

    except Exception as e:
        # Return error message if an exception occurs
        return (
            f'An error occurred: {e}. Please make sure you are using a valid cloudflare clearance token and user agent.'
        )


# Set page configuration and add header
st.set_page_config(
    page_title="GPT API GUI \n current version: gpt-3.5-turbo",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    menu_items={
        'Get Help': 'https://github.com/samggggflynn/gpt4free/blob/main/README.md',
        'Report a bug': "https://github.com/xtekky/gpt4free/issues",
        'About': "### gptfree GUI",
    },
)
st.header('GPT GUI')

# Add text area for user input and button to get answer
question_text_area = st.text_area('🤖 Ask Any Question :', placeholder='Explain quantum computing in 50 words')
if st.button('🧠 Think'):
    answer = get_answer(question_text_area)
    # escaped = answer.encode('utf-8').decode('unicode-escape')
    escaped = answer
    # Display answer
    st.caption("Answer :")
    # st.markdown(escaped, unsafe_allow_html=True)
    container = st.empty()
    res = ''
    for value in escaped:
        container.write(value.text)
        res += value.text
        # fake stream out 
        container.markdown(res)


# Hide Streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# poe_url = "poe.com"

# while True:
#     # 发送GET请求访问网页
#     refresh_page = requests.get(poe_url)
    
#     # 指定刷新时间,单位秒
#     time.sleep(3000)  
