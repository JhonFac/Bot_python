#!/bin/sh

set -e
# start Container
echo "Contenedor iniciado"
echo "$(date): Ejecutando proceso"
echo $PORT
python estadoAnimoMascota.py 0.0.0.0:$PORT
# python estadoAnimoMascota.py 0.0.0.0:5000
