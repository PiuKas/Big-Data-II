Cuando ejecutemos aquí, hay que poner en el terminal:  python3 main.py
```Python
from twitchAPI.twitch import Twitch #carga su propia libreria  
twitch = Twitch('352e2ul58dwnjz5aua1kxuhyi2cvpq', 'i55ygvu0l1ozkhq48l3p99dukx28ch')  #variable que contiene las credenciales
print(twitch.get_users(logins=['your_twitch_username'])) #imprime el resultado de una función
```