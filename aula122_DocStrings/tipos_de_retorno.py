"quando eu quero indicar que minha função pode retornar dois tipos de return eu faço o seguinte"

from typing import Union

#informo que minha função pode retornar ou uma lista ou um dicionario
def funcao() -> Union[list, dict]:
    return []