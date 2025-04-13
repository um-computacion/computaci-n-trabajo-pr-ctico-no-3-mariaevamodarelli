class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    pass

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.
    También permite salir escribiendo 'salir'.

    Returns:
        int: El número ingresado si es válido.
        None: Si el usuario desea salir.

    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
    """
    entrada = input("Ingrese un número (o 'salir' para terminar): ")
    if entrada.lower() == 'salir':
        return None

    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")
