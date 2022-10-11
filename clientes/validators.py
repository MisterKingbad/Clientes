import re
from validate_docbr import CPF


 
def cpf_valido(numero_do_cpf):
    cpf = CPF()
    mask_cpf = cpf.generate(numero_do_cpf)
    return cpf.validate(mask_cpf)
        
def nome_valido(nome):
    return nome.isalpha() #se o nome não for alfabético
        
        
def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9 #se o tamanho do rg for diferente de 9
            
    
def celular_valido(celular):
    modelo =  '[0-9]{2} [0-9]{5}-[0-9]{4}' #padrão de celular
    resposta = re.findall(modelo, celular) #verifica se o celular está no padrão	
    return resposta
    
        