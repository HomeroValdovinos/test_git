# Se instalo PIP y el paquete requests
# Para hacer peticiones request a traves de internet

import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

# r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE')

print r.status_code