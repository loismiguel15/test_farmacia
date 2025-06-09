# test_validacao_farmacia.py
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class TestValidacaoFarmacia:

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

    # --- Testes de Validação para Cadastro de Medicamento ---
    def test_validacao_cadastro_id_obrigatorio(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "nome").send_keys("TesteNomeVal")
        self.driver.find_element(By.ID, "quantidade").send_keys("1")
        self.driver.find_element(By.ID, "preco").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert "ID é obrigatório" in alert_text if alert_text else False, \
               "Alerta de ID obrigatório para cadastro não apareceu ou mensagem incorreta."

    def test_validacao_cadastro_nome_obrigatorio(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "id").send_keys("VAL001")
        self.driver.find_element(By.ID, "quantidade").send_keys("1")
        self.driver.find_element(By.ID, "preco").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert "Nome é obrigatório" in alert_text if alert_text else False, \
               "Alerta de nome obrigatório para cadastro não apareceu ou mensagem incorreta."

    def test_validacao_cadastro_quantidade_negativa(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "id").send_keys("VAL002")
        self.driver.find_element(By.ID, "nome").send_keys("TesteNomeVal")
        self.driver.find_element(By.ID, "quantidade").send_keys("-5") # Quantidade negativa
        self.driver.find_element(By.ID, "preco").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert "Quantidade inválida" in alert_text if alert_text else False, \
               "Alerta de quantidade de cadastro inválida (negativa) não apareceu ou mensagem incorreta."

    def test_validacao_cadastro_preco_nao_numerico(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "id").send_keys("VAL003")
        self.driver.find_element(By.ID, "nome").send_keys("TesteNomeVal")
        self.driver.find_element(By.ID, "quantidade").send_keys("1")
        self.driver.find_element(By.ID, "preco").send_keys("abc") # Preço não numérico
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert "Preço inválido" in alert_text if alert_text else False, \
               "Alerta de preço de cadastro inválido (não numérico) não apareceu ou mensagem incorreta."

    # --- Testes de Validação para Venda de Medicamento ---
    def test_validacao_venda_id_obrigatorio(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click() # Botão Vender
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert "ID do medicamento para venda é obrigatório" in alert_text if alert_text else False, \
               "Alerta de ID de venda obrigatório não apareceu ou mensagem incorreta."

    def test_validacao_venda_quantidade_zero(self):
        self.driver.get(self.base_url)
        # Primeiro, cadastra um medicamento para ter um ID válido para tentar vender
        self.driver.find_element(By.ID, "id").send_keys("VALV01")
        self.driver.find_element(By.ID, "nome").send_keys("ParaVendaVal")
        self.driver.find_element(By.ID, "quantidade").send_keys("5")
        self.driver.find_element(By.ID, "preco").send_keys("10")
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(6)").click() # Botão Cadastrar
        self._aceitar_alerta_se_presente() # Aceita o alerta de cadastro

        # Tenta vender com quantidade zero
        self.driver.find_element(By.ID, "idVenda").send_keys("VALV01")
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys("0") # Quantidade zero
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click() # Botão Vender
        alert_text = self._aceitar_alerta_se_presente()
        # Adapte a mensagem de erro conforme a aplicação
        assert "Quantidade para venda deve ser maior que zero" in alert_text if alert_text else False, \
               "Alerta de quantidade de venda inválida (zero) não apareceu ou mensagem incorreta."