from animaux.chat import Chat
from animaux.lion import Lion

# Création des threads
lion1 = Lion()
lion2 = Lion()
chat1 = Chat()
chat2 = Chat()

# Lancement des threads
lion1.start()
lion2.start()
chat1.start()
chat2.start()

# Attend que les threads se terminent
lion1.join()
lion2.join()
chat1.join()
chat2.join()
