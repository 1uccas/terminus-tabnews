# terminus-tabnews

Terminus-Tabnews é uma aplicação de linha de comando que busca e exibe artigos recentes do site "TabNews" usando um feed RSS. Ele permite que os usuários selecionem um artigo para abrir no navegador web padrão.

### Requisitos
- Python (A partir da versão 3.0)
- Módulos: `feedparser`, `rich`, `webbrowser`, `os`, `time`

### Instalação
1. **Clone o repositório ou baixe o script:**
   ```sh
   git clone <https://github.com/1uccas/terminus-tabnews.git>
   cd <terminus-tabnews>
   ```

2. **Instale os módulos Python necessários:**
   ```sh
   pip install feedparser rich
   ```

### Uso
1. **Execute o script:**
   ```sh
   python __main__.py
   ```

2. **Navegue pela interface:**
   - O script exibirá uma tabela com os artigos recentes.
   - Digite o número correspondente ao artigo que deseja abrir no navegador.
   - Digite `00` para sair do script.

### Contribuição
Sinta-se à vontade para fazer fork do repositório e enviar pull requests. Para mudanças maiores, abra uma issue primeiro para discutir o que você gostaria de alterar.

### Licença
Este projeto está licenciado sob a Licença MIT.