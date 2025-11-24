import streamlit as st

# Import your chatbot function
from myscript import rag_chat   # change filename if different

st.set_page_config(page_title="Urvika's AI Chatbot")

st.title("🤖 Urvika's RAG Chatbot")
st.write("Talk to your personal AI assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if user_input.strip():
        response = rag_chat(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display chat
for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
