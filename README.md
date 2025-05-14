                                                          Asistente Legal LUC

El siguiente proyecto consiste en la creación de un chatbot experto en la Ley de Urgente Consideracion (Ley N° 19.889) de Uruguay, basado en un sistema RAG + LLM.

Requisitos previos:
-Tener Docker instalado

¿Qué es Docker?
Docker se utiliza para empaquetar todo el sistema (modelo, API, frontend y dependencias) en un contenedor portátil y reproducible. Esto garantiza que el proyecto pueda ejecutarse de forma consistente en cualquier máquina, sin necesidad de instalar manualmente bibliotecas, entornos o configuraciones específicas.
Evita errores del estilo "en mi PC funcionaba".

Instrucciones para instalacion y ejecucion (Via Docker)
1.Clonar este respoitorio:

git clone https://github.com/tu-usuario/asistente-legal-luc.git

cd asistente-legal-luc

2.Construir imagen Docker:
docker build -t asistente-luc .

3.Ejecutar el contenedor:
docker run -p 8000:8000 -p 8501:8501 asistente-luc

4.Abrir en navegador para utilizar la interfaz:
http://localhost:8501

Instrucciones para ejecución local (sin Docker):

1.Ejecutar script de configuracion

bash setup_api.sh

2.Iniciar Backend

python FP.py

3.Iniciar Frontend

streamlit run front_streamlit.py
*se deberia abrir una ventana en el navegador con la interfaz de usuario*

Todos los requisitos del entorno y dependencias se encuentran en requirements.txt.

Descripción técnica del sistema:

El sistema utiliza un modelo RAG con:
Chunking legal por artículos
Embeddings con intfloat/e5-base
Indexado con FAISS
LLM generativo: meta-llama/Llama-3.2-1B


El pipeline consta de:
Extracción de texto del PDF de la LUC
Limpieza y partición por artículos
Generación de embeddings y construcción de índice FAISS
Recuperación de contexto relevante
Generación de respuesta con el modelo LLM

Justificaciones:
Parseo: Al tratarse de un documento legal disponible en formato .PDF, se utilizó la libreria PDFminer para limpiar el texto.
Chunking: El chunking legal por artículos fue elegido para preservar la estructura normativa del documento y mantener la semántica completa de cada artículo. Esto mejora la precisión en la recuperación frente a cortes arbitrarios de texto.
Embeddings: Se seleccionó el modelo intfloat/e5-base debido a que fue el utilizado en el curso.
Indice vectorial: La elección de FAISS corresponde a que fue el utilizado en el curso.
Modelo generativo: Se optó por utilizar el modelo LLaMA 3.2-1B por su equilibrio entre peso y rendimiento. Al probar con otros modelos más pesados(Phi-2, LLaMA 3-8B, TinyLLaMA), las consultas demoraban mucho lo cual no resulta atractivo para un chatbot. A su vez, este modelo podía ser ejecutado localmente y se encuentra disponible en HuggingFace.
Prompting: A lo largo del desarrollo. se exploraron distintos estilos de prompting, variando tono o restricciones. Si bien no se utilizó una técnica, se optó por un enfoque práctico: se probaron varios prompts hasta encontrar aquel que generara respuestas coherentes, sin alucinar y con mayor ajuste al contexto legal (LUC). El prompt final le pide al modelo actuar como un abogado especializado en la LUC, basarse únicamente en fragmentos del RAG, evitar inventar o formular nuevas preguntas y retornar una frase estandar si no encuentra contexto.

Créditos:
-Ley de Urgente Consideración https://www.impo.com.uy/bases/leyes/19889-2020

