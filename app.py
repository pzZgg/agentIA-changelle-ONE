import streamlit as st
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

st.set_page_config(page_title="Agente IA - E-commerce", page_icon="🛍️")
st.title("🛍️ Asistente Virtual - TechStore")
st.write("Pregunta cualquier duda sobre envíos, devoluciones, garantías o métodos de pago.")

hf_token = os.getenv("hf_KjLxRmVpYwNzQsTuVaBcDeFgHiJkLmNoPq")
if not hf_token:
    hf_token = st.sidebar.text_input("Ingresa:", type="password")

if hf_token:
    os.environ["hf_KjLxRmVpYwNzQsTuVaBcDeFgHiJkLmNoPq"] = hf_token

    @st.cache_resource
    def init_agent():
        # Cargar documento
        loader = TextLoader("data/politicas_ecommerce.txt", encoding='utf-8')
        documents = loader.load()

        # Chunking
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = text_splitter.split_documents(documents)

        # Embeddings locales gratuitos
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectordb = Chroma.from_documents(texts, embeddings)

        # LLM Open Source a través de la API gratuita de Hugging Face
        llm = HuggingFaceEndpoint(
            repo_id="HuggingFaceH4/zephyr-7b-beta",
            temperature=0.1,
            max_new_tokens=250
        )
        return RetrievalQA.from_chain_type(
            llm=llm, 
            chain_type="stuff", 
            retriever=vectordb.as_retriever(search_kwargs={"k": 2})
        )

    try:
        qa_chain = init_agent()
        st.sidebar.success("Base de datos de conocimiento cargada exitosamente.")

        # Manejo del historial del chat en Streamlit
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Input del usuario
        if user_query := st.chat_input("Escribe tu consulta aquí..."):
            st.session_state.messages.append({"role": "user", "content": user_query})
            with st.chat_message("user"):
                st.markdown(user_query)

            with st.chat_message("assistant"):
                with st.spinner("Consultando documentación oficial..."):
                    res = qa_chain.invoke(user_query)
                    st.markdown(res['result'])
                    st.session_state.messages.append({"role": "assistant", "content": res['result']})
    except Exception as e:
        st.error(f"Error al inicializar el agente: {e}")
else:
    st.info("Por favor ingresa tu Token de Hugging Face en la barra lateral para comenzar.")
