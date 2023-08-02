# Projeto de Criptografia de Arquivos



## Descrição
Este projeto é um exemplo simples de criptografia de arquivos usando uma chave simétrica. Ele utiliza a biblioteca `cryptography` para gerar uma chave simétrica, que é salva em um arquivo `symmetric_key.txt`. O algoritmo AES em modo CTR é utilizado para criptografar os arquivos. Os arquivos criptografados recebem a extensão `.ransomwaretroll`.

## Requisitos
- Python 3.x
- Instalar as dependências usando o arquivo `requirements.txt` 



## Configuração
1. Clone o repositório para o seu computador:

    git clone https://github.com/Mauricios73/Criptografia-de-arquivos.git

2. Instale as dependências usando o `pip`:
`pip install -r requirements.txt`

## Uso
1. Execute o script `Encrypter.py` para criptografar uma pasta e gerar a chave simétrica:
`symmetric_key.txt`

2. Verifique o arquivo `symmetric_key.txt`, que contém a chave simétrica gerada.

3. Guarde a chave simétrica em um local seguro, pois ela é necessária para descriptografar os arquivos posteriormente.

4. Os arquivos criptografados serão salvos com a extensão `.ransomwaretroll`.

5. Para descriptografar os arquivos, execute o script `Decrypter.py`.

## Observações

- É importante destacar que o uso deste código e do conceito de ransomware para fins maliciosos ou sem o consentimento explícito do proprietário do arquivo é ilegal e antiético. Criptografar ou manipular os arquivos de outras pessoas sem a devida autorização é uma violação séria da privacidade e da lei. Esse código deve ser usado apenas para fins educacionais ou em situações legítimas em que você possui total consentimento para criptografar e manipular os arquivos.
- Mantenha a chave simétrica em segurança. Sem ela, não será possível descriptografar os arquivos.
- O algoritmo AES em modo CTR é utilizado para criptografar e descriptografar os arquivos.
