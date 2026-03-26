
# Ofuscador JavaScript

É uma ferramenta robusta de ofuscação JavaScript com interface moderna em CustomTkinter, projetada para
elevar a segurança do código-fonte e dificultar a engenharia reversa. Seguindo preceitos de conformidade OWASP, o 
software automatiza a renomeação de variáveis para identificadores hexadecimais complexos, converte strings para o 
formato hexadecimal e aplica uma minificação agressiva através da remoção de espaços e comentários. É a solução ideal para 
desenvolvedores que precisam proteger a lógica de negócio no front-end de forma rápida, intuitiva e eficiente.

## Autora

- [@leticiazooe](https://www.github.com/leticiazooe)

## Interface

<img width="1101" height="797" alt="image" src="https://github.com/user-attachments/assets/7e1c6aa3-fad9-49ea-97d8-26cbcf70052d" />

## Características

- Auto-Instalação de Dependências: O script verifica e instala automaticamente as bibliotecas necessárias (customtkinter e pyperclip) ao ser executado, facilitando o uso em diferentes ambientes.
- Ofuscação de Variáveis (Renomeação): Identifica nomes de variáveis e funções (com mais de 2 caracteres) e os substitui por identificadores hexadecimais aleatórios (ex: _0x541), preservando as palavras reservadas do JavaScript.
- Criptografia de Strings em Hex: Converte automaticamente textos entre aspas para sequências de escape hexadecimais (\xHH), impedindo a leitura direta de mensagens e endpoints no código.
- Minificação Agressiva: Remove espaços em branco desnecessários, quebras de linha e reduz o espaçamento ao redor de operadores lógicos e aritméticos.
- Limpeza de Comentários: Varre o código para eliminar comentários de linha única (//) e de bloco (/* ... */), removendo informações sensíveis ou explicativas.
- Interface Gráfica Moderna (GUI): Utiliza a biblioteca CustomTkinter para oferecer uma experiência de usuário intuitiva, com tema escuro e layout responsivo.
    
## Tech Stack

- Linguagem Core: Python 3.x – Utilizado como o motor principal para o processamento de texto e lógica de ofuscação.
- Interface Gráfica (GUI): CustomTkinter – Uma evolução da biblioteca Tkinter padrão, fornecendo componentes visuais modernos, suporte nativo a temas (Dark/Light mode) e design responsivo.
- Processamento de Texto: Regular Expressions (Regex) – O coração da ferramenta, utilizado para identificar padrões de código, capturar nomes de variáveis, remover comentários e transformar strings em hexadecimais.
- Gerenciamento de Ambiente: Subprocess & Sys – Implementação de uma rotina de auto-instalação que garante que todas as dependências estejam presentes no sistema do usuário sem necessidade de configuração manual.
- Segurança e Ofuscação: Algoritmos de Ofuscação Customizados – Lógica própria para mapeamento de identificadores e conversão de caracteres para o padrão de escape hexadecimal.

