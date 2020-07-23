from typing import List

from pypro.modulos.models import Modulo


def litar_modelos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """
    return list(Modulo.objects.order_by('titulo').all())
