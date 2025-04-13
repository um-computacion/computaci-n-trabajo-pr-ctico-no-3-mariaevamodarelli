class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    pass

class SalirDelPrograma(Exception):
    """Excepción personalizada para salir del programa."""
    pass

def ingrese_numero():
    """
    Solicita al usuario ingresar un número y valida que sea positivo.

    Returns:
        int: El número ingresado si es válido.

    Raises:
        ValueError: Si la entrada no es un número válido.
        NumeroDebeSerPositivo: Si el número ingresado es negativo.
        SalirDelPrograma: Si el usuario desea salir.
    """
    entrada = input("Ingrese un número (o escriba 'salir' para salir): ")
    if entrada.lower() == "salir":
        raise SalirDelPrograma("El usuario decidió salir.")
    try:
        numero = int(entrada)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo")
        return numero
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")
