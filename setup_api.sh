#!/bin/bash
 
echo "🛠️ Creando entorno virtual..."
python -m venv venv
 
echo "✅ Activando entorno virtual..."
source venv/Scripts/activate
 
echo "📦 Instalando dependencias..."
./venv/Scripts/pip.exe install --upgrade pip
./venv/Scripts/pip.exe install -r requirements.txt
 
echo "✅ Entorno listo. Para activarlo manualmente luego:"
echo "source venv/Scripts/activate && python entrega.py"



