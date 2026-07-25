# 🛍️ Agente Inteligente para E-Commerce - Challenge ONE / Alura

## -agentIA-

## 📝 Descripción General
Esta aplicación consiste en un Agente de Inteligencia Artificial diseñado para automatizar la atención al cliente de una tienda en línea (*TechStore*). El agente procesa la documentación oficial del e-commerce (Políticas de envío, devoluciones, garantías y privacidad) para resolver dudas de los clientes en tiempo real y con alta precisión.

## 🏗️ Arquitectura de la Solución
La solución utiliza una arquitectura **RAG (Retrieval-Augmented Generation)** completamente basada en código abierto (Open Source):
1. **Ingesta de Documentos:** Procesamiento de archivos normativos internos mediante `LangChain`.
2. **Chunking & Embeddings:** División semántica del texto y generación de vectores
3. **Almacenamiento Vectorial:** Indexación en `ChromaDB` para búsqueda por similitud.
4. **Recuperación y Respuesta:** La consulta del usuario recupera el contexto exacto del documento y lo envía a un LLM Open Source (`Zephyr-7B` a través de HuggingFace) para generar la respuesta final.
5. **Interfaz de Usuario:** Desplegada en `Streamlit`.

## 🛠️ Tecnologías y Herramientas Utilizadas
* **Lenguaje:** Python 3.10+
* **Framework RAG:** LangChain
* **Vector Database:** ChromaDB
* **Frontend:** Streamlit
* **Infraestructura Cloud:** Oracle Cloud Infrastructure (OCI Compute Instance)

## 🚀 Instrucciones para Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone <TU_URL_DE_GITHUB>
   cd challenge-alura-agente
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   streamlit run app.py
   ```

---

## ☁️ Evidencia del Deploy en OCI (Oracle Cloud Infrastructure)

* **Enlace público a la aplicación:**
A conrinuación se muestra el enlace publico del deploy en OCI
* **Captura de Pantalla del Deploy:**