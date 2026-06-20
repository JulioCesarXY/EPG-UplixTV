<div align="center">
  <img src="https://uplixtv.r98.com.br/logo.png" alt="UplixTV Logo" width="120px" style="border-radius: 20%; margin-bottom: 20px;"/>

  # 📺 UplixTV M3U Automation

  [![Atualizar Playlist UplixTV](https://github.com/JulioCesarXY/EPG-UplixTV/actions/workflows/atualizar_lista.yml/badge.svg)](https://github.com/JulioCesarXY/NOME_DO_REPOSITORIO/actions/workflows/atualizar_lista.yml)
  [![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

  <p align="center">
    <b>Script automatizado que consome a API do UplixTV, trata metadados e caminhos de arquivos corrompidos, e compila uma playlist M3U atualizada via GitHub Actions.</b>
  </p>
</div>

---

## 🚀 Funcionalidades

* **Filtro Ativo:** Varre e valida se o canal está ativo na origem.
* **Resolução de URLs:** Resolve caminhos relativos de m3u8/mp4 e logotipos locais.
* **Higienização de Dados:** Ignora automaticamente bugs da API onde links de imagens são injetados no lugar do stream.
* **Automação Diária:** Cron Job configurado para rodar de forma serverless às **03:00 AM BRT**.

---

## 🔗 Link M3U Direto

```text
https://raw.githubusercontent.com/JulioCesarXY/EPG-UplixTV/main/uplixtv_playlist.m3u
