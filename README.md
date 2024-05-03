# Verificador de Badblocks em Disco Rígido

Este é um script Python simples para verificar setores defeituosos (bad blocks) em um disco rígido usando o comando `badblocks`.

## Como Usar

1. **Baixe o Script:**
   - Clone este repositório ou baixe o arquivo `badblocks.py` diretamente.

2. **Garanta Permissões de Root:**
   - Este script precisa ser executado com privilégios de root para acessar diretamente o disco rígido. Portanto, antes de executar o script, verifique se você tem permissões de root.

3. **Execute o Script:**
   - Abra um terminal e navegue até o diretório onde o script `badblocks.py` está localizado.
   - Execute o script usando o seguinte comando:
     ```
     sudo python3 badblocks.py <caminho_do_dispositivo>
     ```
     Substitua `<caminho_do_dispositivo>` pelo caminho correto do dispositivo que você deseja verificar (por exemplo, `/dev/sda`).

4. **Acompanhe o Progresso:**
   - O script exibirá informações sobre a verificação em andamento, incluindo o número de setores defeituosos encontrados, se houver. Aguarde até que a verificação seja concluída.

5. **Interpretação dos Resultados:**
   - Após a conclusão da verificação, o script exibirá uma mensagem indicando que a verificação de setores defeituosos foi concluída. Se nenhum setor defeituoso for encontrado, o script indicará que nenhum badblock foi encontrado. Caso contrário, ele listará os setores defeituosos encontrados.

## Requisitos

- Python 3.x
- Permissões de root

## Autor

- Nome: Romulo Pavanello

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
