# Universal Playlist Transfer

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Spotify API](https://img.shields.io/badge/Spotify-Web%20API-1DB954?logo=spotify&logoColor=white)
![YouTube API](https://img.shields.io/badge/YouTube-Data%20API-FF0000?logo=youtube&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-02569B)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A Python-based application that enables seamless playlist transfer between multiple music streaming platforms using a **platform-independent transfer engine**.

The project follows a modular architecture where authentication, platform services, and the transfer engine are completely separated, making it easy to add support for new music platforms in the future.

---

## Features

- 🔄 Transfer playlists across supported platforms
- 🎵 Spotify → Spotify
- 📺 YouTube → YouTube
- 🔀 Spotify → YouTube
- 🔀 YouTube → Spotify
- 🔐 OAuth 2.0 Authentication
- ⚙️ Universal Transfer Engine
- 🧩 Modular and extensible architecture
- 📄 Transfer summary report

---

## Project Architecture

```
                main.py
                   │
                   ▼
      Universal Transfer Engine
         │                   │
         ▼                   ▼
 Spotify Service      YouTube Service
         │                   │
         ▼                   ▼
 Spotify Auth         YouTube Auth
```

The transfer engine remains completely independent of any music platform. Each platform implements the same service interface, allowing the engine to perform transfers without platform-specific logic.

---

## Project Structure

```text
playlist-transfer/
│
├── auth/
│   ├── spotify_auth.py
│   └── youtube_auth.py
│
├── services/
│   ├── spotify_service.py
│   └── youtube_service.py
│
├── engine/
│   └── transfer_engine.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

### Language

- Python 3

### APIs

- Spotify Web API
- YouTube Data API v3

### Libraries

- Spotipy
- google-api-python-client
- google-auth-oauthlib
- Requests

### Concepts

- OAuth 2.0 Authentication
- REST APIs
- Modular Software Design
- Service-Based Architecture

---

## Installation

Clone the repository

```bash
git clone https://github.com/quincy082/playlist-transfer.git
```

Navigate to the project directory

```bash
cd playlist-transfer
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## Configuration

Create the required API credentials for:

- Spotify Developer Dashboard
- Google Cloud Console

Add the credentials to the project as instructed in the authentication modules before running the application.

---

## Usage

Run the application

```bash
python main.py
```

Choose:

- Source Platform
- Destination Platform
- Source Playlist
- Destination Playlist Name

The application authenticates both platforms, transfers the playlist, and generates a transfer summary.

---

## Currently Supported Platforms

| Platform | Read Playlists | Create Playlist | Transfer |
|-----------|---------------|-----------------|----------|
| Spotify | ✅ | ✅ | ✅ |
| YouTube | ✅ | ✅ | ✅ |

---

## Future Enhancements

- 🖥️ Desktop GUI *(Currently in Development)*
- 🎯 Improved song matching
- 🚫 Duplicate song detection
- ☁️ Web-based version
- 📊 Transfer statistics and analytics

---

## Contributing

Contributions, suggestions, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Quincy Vadi**
