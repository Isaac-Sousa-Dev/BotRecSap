"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
import pyautogui
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        #self.browse("https://servicedesk.halexistar.com.br")
        pyautogui.alert('Não mexa em nada, o código vai começar')
        if not self.find( "iniciarWindows", matching=0.97, waiting_time=10000):
            self.not_found("iniciarWindows")
        self.click()
        self.sleep(5)
        self.paste("Sap")
        
        if not self.find( "iniciarSap", matching=0.97, waiting_time=10000):
            self.not_found("iniciarSap")
        self.click()
        
        if not self.find( "instanciaSap", matching=0.97, waiting_time=10000):
            self.not_found("instanciaSap")
        self.click()
        self.click()
       
        
        if not self.find( "teste", matching=0.97, waiting_time=10000):
            self.not_found("teste")
        self.click()
        
        self.sleep(5)
        self.kb_type("teste-ce")
        self.tab()
        self.kb_type("123@24")
        self.enter()
        
        if not self.find( "isofarma", matching=0.97, waiting_time=10000):
            self.not_found("isofarma")
        self.click()
        self.click()
        
        if not self.find( "criarRequisicao", matching=0.97, waiting_time=10000):
            self.not_found("criarRequisicao")
        self.click()
        self.click()
        self.click()
        
        if not self.find( "descricao", matching=0.97, waiting_time=10000):
            self.not_found("descricao")
        self.click()
        
        self.kb_type("AS INFORMATICA - ALUGUEL DE SERVIDOR\nVALOR: 1.034,00\nVENC: 15/03/2023\nNFº 19661")
        
        if not self.find( "seta", matching=0.97, waiting_time=10000):
            self.not_found("seta")
        self.click()
        self.type_down()
        self.type_right()
        self.type_right()
        self.type_right()
        self.kb_type('K')
        self.enter()
        self.sleep(4)
        
        if not self.find( "quant", matching=0.97, waiting_time=10000):
            self.not_found("quant")
        self.click()
        
        
        self.type_left()
        self.type_left()
        self.kb_type("9101000")
        self.enter()
        
        if not self.find( "quant2", matching=0.97, waiting_time=10000):
            self.not_found("quant2")
        self.click()
        
        
        self.type_right()
        self.type_right()
        self.type_right()
        self.kb_type("1.034,00")
        self.enter()
        self.sleep(5)
        
        if not self.find( "quant2", matching=0.97, waiting_time=10000):
            self.not_found("quant2")
        self.click()
        self.kb_type("1")
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.type_right()
        self.kb_type("ISAAC")
        self.type_right()
        self.kb_type("017")
        self.enter()
        self.sleep(3)
        
        if not self.find( "centroDeCusto", matching=0.97, waiting_time=10000):
            self.not_found("centroDeCusto")
        self.click()
        self.kb_type("82010203")
        self.enter()
        self.sleep(4)
        
        if not self.find( "verificar", matching=0.97, waiting_time=10000):
            self.not_found("verificar")
        self.click()
        self.click()
        self.sleep(5)
        
        if not self.find( "objetos", matching=0.97, waiting_time=10000):
            self.not_found("objetos")
        self.click()
        self.sleep(5)
        self.type_down()
        self.type_right()
        self.enter()
        
        pyautogui.alert("Escolha o(s) anexo(s) e não esqueça de alterar na descrição o N° da Nota e o Vencimento")
        
        
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()






