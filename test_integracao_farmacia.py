# test_integracao_farmacia.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

class TestIntegracaoFarmacia:

    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.base_url = "https://loismiguel15.github.io/farmacia/?classId=6af7bdb9-1401-486f-a029-2ec8ab7d1110&assignmentId=305218df-2c0f-4cd3-886e-14f9fce75209&submissionId=6fe38fef-ca98-4906-fd2b-4d32196890cb"
        self.driver.implicitly_wait(5) # Espera implícita

    def teardown_method(self, method):
        self.driver.quit()

    def _aceitar_alerta_se_presente(self):
        """Tenta aceitar um alerta e retorna o texto, ou None se não houver alerta."""
        try:
            alert = WebDriverWait(self.driver, 3).until(expected_conditions.alert_is_present())
            text = alert.text
            alert.accept()
            return text
        except TimeoutException:
            return None

    def test_integracao_cadastro_e_venda_sucesso(self):
        """
        Testa o fluxo completo de cadastrar um medicamento e realizar uma venda com sucesso.
        """
        self.driver.get(self.base_url)
        self.driver.set_window_size(1382, 744)

        # Cadastro de Medicamento
        id_med_sucesso = "INT001"
        nome_med_sucesso = "DipironaPlus"
        self.driver.find_element(By.ID, "id").send_keys(id_med_sucesso)
        self.driver.find_element(By.ID, "nome").send_keys(nome_med_sucesso)
        self.driver.find_element(By.ID, "quantidade").send_keys("20")
        self.driver.find_element(By.ID, "preco").send_keys("7")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        alert_text_cadastro = self._aceitar_alerta_se_presente()
        assert alert_text_cadastro == f"Medicamento {nome_med_sucesso} cadastrado com sucesso!"

        # Venda de Medicamento
        self.driver.find_element(By.ID, "idVenda").send_keys(id_med_sucesso)
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click() # Botão Vender
        alert_text_venda = self._aceitar_alerta_se_presente()
        assert alert_text_venda == f"Venda de 3 unidades de {nome_med_sucesso} realizada com sucesso!"

    def test_integracao_venda_medicamento_inexistente(self):
        """
        Testa a tentativa de venda de um medicamento que não foi cadastrado.
        """
        self.driver.get(self.base_url)
        id_inexistente = "INT999"
        self.driver.find_element(By.ID, "idVenda").send_keys(id_inexistente)
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click() # Botão Vender
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert f"Medicamento com ID {id_inexistente} não encontrado" in alert_text if alert_text else False, \
               "Alerta de medicamento inexistente não apareceu ou mensagem incorreta."

    def test_integracao_venda_quantidade_maior_que_estoque(self):
        """
        Testa a tentativa de venda de uma quantidade maior do que a disponível em estoque.
        """
        self.driver.get(self.base_url)
        # Cadastra medicamento com quantidade limitada
        id_med_estoque = "INT002"
        nome_med_estoque = "EstoqueBaixo"
        qtd_inicial = 2
        self.driver.find_element(By.ID, "id").send_keys(id_med_estoque)
        self.driver.find_element(By.ID, "nome").send_keys(nome_med_estoque)
        self.driver.find_element(By.ID, "quantidade").send_keys(str(qtd_inicial))
        self.driver.find_element(By.ID, "preco").send_keys("10")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        self._aceitar_alerta_se_presente() # Aceita o alerta de cadastro

        # Tenta vender mais do que o disponível
        self.driver.find_element(By.ID, "idVenda").send_keys(id_med_estoque)
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys(str(qtd_inicial + 1))
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click() # Botão Vender
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert f"Estoque insuficiente para {nome_med_estoque}" in alert_text if alert_text else False, \
               "Alerta de estoque insuficiente não apareceu ou mensagem incorreta."