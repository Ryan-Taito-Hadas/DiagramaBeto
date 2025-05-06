from functools import wraps

#Login Method Decorator_____________________________________________________________________________________________________
def requer_login(login):
        @wraps(login)
        def wrapper(self, *args, **kwargs):
            if hasattr(self, 'esta_autenticado') and callable(self.esta_autenticado):
                if not self.esta_autenticado():
                    print("Acesso negado: login necessário.")
                    return
            else:
                raise AttributeError("Classe não possui método 'esta_autenticado'")
            return login(self, *args, **kwargs)
        return wrapper