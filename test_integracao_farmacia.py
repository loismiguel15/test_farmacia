import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestIntegracaoFarmacia:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://loismiguel15.github.io/farmacia/?classId=6af7bdb9-1401-486f-a029-2ec8ab7d1110&assignmentId=305218df-2c0f-4cd3-886e-14f9fce75209&submissionId=6fe38fef-ca98-4906-fd2b-4d32196890cb")
        self.driver.set_window_size(1936, 1048)
        yield
        self.driver.quit()

    def test_insercao_e_venda_produto(self):
        # Preenchendo os campos
        self.driver.find_element(By.ID, "id").send_keys("10")
        self.driver.find_element(By.ID, "nome").send_keys("Dipirona")
        self.driver.find_element(By.ID, "quantidade").send_keys("100")
        self.driver.find_element(By.ID, "preco").send_keys("5")
        
        # Simula uma venda
        self.driver.find_element(By.ID, "idVenda").send_keys("10")
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys("2")

        # Verifica se os campos foram preenchidos corretamente
        assert self.driver.find_element(By.ID, "id").get_attribute("value") == "10"
        assert self.driver.find_element(By.ID, "nome").get_attribute("value") == "Dipirona"
        assert self.driver.find_element(By.ID, "quantidade").get_attribute("value") == "100"
        assert self.driver.find_element(By.ID, "preco").get_attribute("value") == "5"
