import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFarmaciaValidacao:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://loismiguel15.github.io/farmacia/")
        self.driver.set_window_size(1936, 1048)

    def teardown_method(self):
        self.driver.quit()

    def test_cadastro_com_campos_vazios(self):
        # Tenta cadastrar sem preencher campos obrigatórios
        self.driver.find_element(By.ID, "id").send_keys("")
        self.driver.find_element(By.ID, "nome").send_keys("")
        self.driver.find_element(By.ID, "quantidade").send_keys("")
        self.driver.find_element(By.ID, "preco").send_keys("")

    def test_venda_com_quantidade_negativa(self):
        self.driver.find_element(By.ID, "idVenda").send_keys("1")
        self.driver.find_element(By.ID, "quantidadeVenda").send_keys("-5")

       
