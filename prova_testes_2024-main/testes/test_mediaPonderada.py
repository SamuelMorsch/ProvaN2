from stat_funcs import StatsN2
import pytest

@pytest.fixture
def stats():
    return StatsN2()

@pytest.fixture
def lista_pesos_exemplo():
    return [0.2, 0.3, 0.5]

@pytest.fixture
def lista_numeros_exemplo():
    return [1, 2, 3]

class TestMediaPonderada:
    @pytest.mark.media_ponderada
    def test_media_ponderada_lista_vazia(self, stats, lista_numeros_exemplo, lista_pesos_exemplo):
        assert stats.media_ponderada([], []) == 0

    @pytest.mark.media_ponderada
    def test_media_ponderada_lista_nao_vazia(self, stats, lista_numeros_exemplo, lista_pesos_exemplo):
        assert stats.media_ponderada(lista_numeros_exemplo, lista_pesos_exemplo) == 2.2

    @pytest.mark.xfail
    @pytest.mark.media_ponderada
    def test_media_ponderada_erro_proposital(self, stats, lista_numeros_exemplo, lista_pesos_exemplo):
        assert stats.media_ponderada(lista_numeros_exemplo, lista_pesos_exemplo) == 10