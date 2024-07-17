"""
mgm_service

MGM (Meteoroloji Genel Müdürlüğü) servisleri ile etkileşim için modül.

Fonksiyonlar:
    - get_data(endpoint, params=None):
        MGM servisinden JSON verisi alır.

    - get_request(endpoint, params=None):
        MGM web sitesinden HTML verisi çeker.
"""

import requests


def get_data(endpoint, params=None):
    """
    MGM servisinden JSON verisi alır.

    Args:
        endpoint (str): Sorgulanacak endpoint.
        params (dict, optional): İsteğin parametreleri. Varsayılan: None.

    Returns:
        dict or None: MGM servisinden gelen JSON verisi, hata durumunda None.
    """
    base_url = "https://servis.mgm.gov.tr/web/"
    headers = {"Origin": "https://www.mgm.gov.tr"}
    url = f"{base_url}{endpoint}"

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # HTTP hatalarını kontrol et
        return response.json()

    except requests.exceptions.RequestException as e:
        return None

