## Discord Bot

Egy Open Source projekt, melyhez nyugodtan közreműködhettek, csak nyissatok egy PR-t ha valamit hozzá szeretnétek adni.

Eddig az alábbiakat tartalmazza:
- Join - Leave
- Meme (Reddit API-t használ)
- 2 Minigame (KPÓ és BJ)
- Autoreakció üzenetekre adott csatornában

### Követelmények

Mielőtt elkezdenéd, győződj meg arról, hogy a következő eszközök telepítve vannak a gépeden:

1. **Python 3.8 vagy újabb**: A bot futtatásához Python szükséges. Ellenőrizheted, hogy a Python telepítve van-e a gépeden, ha a parancssorban vagy terminálban beírod:

    ```bash
    python --version
    ```

    Ha nincs telepítve, letöltheted innen: [Python letöltési oldal](https://www.python.org/downloads/).

2. **pip**: A Python csomagkezelője, ami általában a Python telepítésével együtt érkezik. Ezzel fogod telepíteni a szükséges Python könyvtárakat.

### Bot létrehozása a Discord Developer Portálon

Mielőtt elindítod a botodat, regisztrálnod kell egy botot a Discord fejlesztői portálján:

1. Látogass el a [Discord Developer Portal](https://discord.com/developers/applications) oldalra.
2. Jelentkezz be a Discord fiókoddal.
3. Kattints a **New Application** gombra, és nevezd el az alkalmazásodat.
4. A bal oldali menüben válaszd ki a **Bot** opciót, majd kattints az **Add Bot** gombra.
5. Jegyezd fel a botod **Tokenjét**, mivel erre szükséged lesz a kódodban. **Ne oszd meg senkivel a tokenedet!**

### Telepítés

A következő lépések segítenek abban, hogy telepítsd a szükséges csomagokat és beállítsd a botodat.

1. **Csomagok telepítése**: A bothoz több package is kell. Ezek az alábbiak:
- discord.py
- asyncio
- itertools
- asyncpraw

2. **Kód konfigurálása**: Nyisd meg a botod kódját, és illeszd be a botod Tokenjét a megfelelő helyre. Példa:
    A `config.py` fileban tudod beállítani a csatornák ID-jét, illetve a bottoken.py-ban a Discord Botod Tokenjét. 
    Fontos, hogy a TOKEN-t senkivel se osszad meg!

3. **A bot futtatása**: A botot a következő parancs kiadásával tudod elindítani:

    ```bash
    python main.py
    ```

### Használat

Miután a botod sikeresen elindult, megjelenik online a Discord szervereden.

### Hibakeresés

Ha bármilyen hibát tapasztalsz a bot futtatása közben, győződj meg róla, hogy:

- A Python és pip megfelelően telepítve van.
- A bot tokenje helyesen van megadva a kódban.
- A szükséges csomagok telepítve vannak a `pip install` parancs segítségével.

További információkért és segítségért látogass el a [Discord.py dokumentációjára](https://discordpy.readthedocs.io/).
