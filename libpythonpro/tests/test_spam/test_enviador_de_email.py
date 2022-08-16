import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['fpmrocha@yahoo.com.br', 'fpmrocha@hotmail.com']
)
def test_remetente(destinatario):
    enviador= Enviador()
    destinatarios = ['fpmrocha@yahoo.com.br', 'fpmrocha@hotmail.com']
    destinatario in destinatarios
    resultado = enviador.enviar(
        destinatario,
        'fpmrocha@gmail.com',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'fpmrochahotmail.com']
)
def test_remetente_invlido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'fpmrocha@gmail.com',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
