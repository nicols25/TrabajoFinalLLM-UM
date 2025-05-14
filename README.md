# 🧑‍⚖️ Asistente Legal LUC

Este proyecto consiste en la creación de un chatbot especializado en la Ley de Urgente Consideración (Ley N.º 19.889) de Uruguay, utilizando una arquitectura RAG combinada con un modelo LLM. El sistema permite hacer preguntas en lenguaje natural y obtener respuestas basadas exclusivamente en el contenido de la ley.

---

## ⚙️ Requisitos previos

- Tener Docker instalado en la máquina.

¿Qué es Docker?  
Docker se utiliza para empaquetar todo el sistema (modelo, API, frontend y dependencias) en un contenedor portátil y reproducible. Esto garantiza que el proyecto pueda ejecutarse de forma consistente en cualquier entorno, sin necesidad de instalar manualmente bibliotecas ni configurar entornos específicos. Es ideal para evitar errores del estilo "en mi PC funcionaba".

---

## 🚀 Instrucciones para instalación y ejecución (vía Docker)

1. Clonar este repositorio:

```bash
git clone https://github.com/tu-usuario/asistente-legal-luc.git
cd asistente-legal-luc
```

2. Construir la imagen Docker:

```bash
docker build -t asistente-luc .
```

3. Ejecutar el contenedor:

```bash
docker run -p 8000:8000 -p 8501:8501 asistente-luc
```

4. Abrir el navegador en:

http://localhost:8501

---

## 🧪 Instrucciones para ejecución local (sin Docker)

1. Ejecutar el script de configuración:

```bash
bash setup_api.sh
```

2. Iniciar el backend:

```bash
python FP.py
```

3. Iniciar el frontend:

```bash
streamlit run front_streamlit.py
```

Al hacerlo, se debería abrir automáticamente una ventana en el navegador con la interfaz de usuario.

Todos los requisitos del entorno y las dependencias están en el archivo requirements.txt.

---

## 🧠 Descripción técnica del sistema

El sistema implementa una arquitectura RAG con los siguientes componentes:

- Chunking legal por artículos
- Embeddings con el modelo intfloat/e5-base
- Indexado con FAISS
- LLM generativo: meta-llama/Llama-3.2-1B

El pipeline sigue este flujo:

1. Extracción del texto completo del PDF de la LUC
2. Limpieza y partición por artículos
3. Generación de embeddings y construcción del índice FAISS
4. Recuperación del contexto más relevante
5. Generación de respuesta final con el modelo LLM

---

## 🔍 Justificación de decisiones técnicas

- Parseo: Al tratarse de un documento legal en formato PDF, se utilizó la librería pdfminer.six para extraer el texto de forma automatizada.

- Chunking: Se optó por dividir el texto artículo por artículo para mantener el sentido completo de cada norma y evitar cortes arbitrarios. Esto mejoró significativamente la precisión en la recuperación.

- Embeddings: Usamos el modelo intfloat/e5-base porque fue el utilizado en el curso y nos permitió implementar la solución sin mayores complicaciones.

- Índice vectorial: Utilizamos FAISS por la misma razón. Ya lo habíamos usado en clase y sabíamos integrarlo bien con NumPy y embeddings.

- Modelo generativo: Probamos otros modelos como Phi-2, LLaMA 3–8B y TinyLLaMA, pero resultaron demasiado pesados o poco precisos. LLaMA 3.2–1B fue el que ofreció mejor equilibrio entre tiempo de respuesta y calidad, y además se pudo ejecutar localmente sin problemas.

- Prompting: Probamos diferentes estilos y ajustes en el prompt. Si bien no seguimos una metodología formal, fuimos afinando la redacción hasta encontrar una variante que generara respuestas coherentes, claras y ajustadas al contexto legal. El prompt final le pide al modelo actuar como un abogado especializado, evitar inventar información y responder solo si encuentra contenido suficiente en el contexto.

---

## 📚 Créditos y fuentes

- Ley de Urgente Consideración (LUC):  
  https://www.impo.com.uy/bases/leyes/19889-2020