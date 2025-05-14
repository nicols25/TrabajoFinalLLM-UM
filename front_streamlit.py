import streamlit as st
import requests
 
st.set_page_config(page_title="Asistente Legal LUC", layout="centered")
st.title("⚖️ Asistente Legal LUC")
 
st.write(
    "Consultá artículos de la Ley de Urgente Consideración (LUC) de Uruguay.\n"
    "Escribí una pregunta y el sistema legal responderá en base a la ley."
)
 
# Entrada del usuario
pregunta = st.text_input(
    "📘 ¿Cuál es tu consulta legal?",
    placeholder="¿Qué dice la ley sobre legítima defensa?"
)
 
# Valor fijo de k (sin mostrarlo)
k = 1
 
# Botón para consultar
if st.button("Consultar"):
    if not pregunta.strip():
        st.warning("Por favor ingresá una pregunta.")
    else:
        with st.spinner("Consultando al asistente legal..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/preguntar",
                    json={"pregunta": pregunta, "k": k},
                    timeout=600
                )
                if response.status_code == 200:
                    respuesta = response.json().get("respuesta", "")
                    st.success("✅ Respuesta encontrada:")
                    st.markdown(respuesta)
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f"❌ No se pudo conectar al backend: {e}")