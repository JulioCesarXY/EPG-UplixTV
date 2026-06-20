import json
import requests

# Configurações de URL
API_URL = "https://uplixtv.r98.com.br/api/content.php?type=channels"
BASE_DOMAIN = "https://uplixtv.r98.com.br"
OUTPUT_FILE = "uplixtv_playlist.m3u"


def fetch_channels():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(API_URL, headers=headers, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None


def build_m3u(data):
    if not data or not data.get("success") or "data" not in data:
        print("Estrutura de dados inválida ou falha na resposta.")
        return

    m3u_lines = ["#EXTM3U\n"]

    for channel in data["data"]:
        # Ignora canais inativos
        if channel.get("is_active") != 1:
            continue

        name = channel.get("name", "Canal Sem Nome")
        stream_url = channel.get("stream_url", "").strip()
        logo = channel.get("logo", "").strip()
        category = channel.get("category", "Variedades").strip()

        # Fallback para categorias vazias
        if not category:
            category = "Variedades"

        # Se não houver URL de transmissão, ignora o canal
        if not stream_url:
            continue

        # Correção de URLs relativas para a stream
        if stream_url.startswith("/"):
            stream_url = f"{BASE_DOMAIN}{stream_url}"

        # Correção de URLs relativas para o logo
        if logo and not logo.startswith("http"):
            # Trata casos em que o caminho não começa com barra
            if logo.startswith("uploads/"):
                logo = f"{BASE_DOMAIN}/{logo}"
            elif logo.startswith("/"):
                logo = f"{BASE_DOMAIN}{logo}"

        # Validação: Ignorar erros na API onde colocaram imagens no stream_url
        if any(
            stream_url.lower().endswith(ext)
            for ext in [".png", ".jpg", ".jpeg", ".webp", ".svg"]
        ):
            print(f"[*] Ignorando link de imagem no stream_url do canal: {name}")
            continue

        # Monta a metatag do M3U
        m3u_lines.append(
            f'#EXTINF:-1 tvg-id="{channel.get("id")}" tvg-name="{name}" tvg-logo="{logo}" group-title="{category}",{name}\n'
        )
        m3u_lines.append(f"{stream_url}\n")

    # Salva o arquivo final
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(m3u_lines)

    print(f"\n[+] Sucesso! Playlist salva com segurança em: {OUTPUT_FILE}")


if __name__ == "__main__":
    print("Iniciando a extração de streams do UplixTV...")
    channel_data = fetch_channels()
    if channel_data:
        build_m3u(channel_data)
