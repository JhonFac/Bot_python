#!/bin/sh

set -e
# start Container
echo "Contenedor iniciado"
echo "$(date): Ejecutando proceso"

# python manage.py estadoAnimoMascota.py 0.0.0.0:$PORT
python estadoAnimoMascota.py 0.0.0.0:5000
