# Setup & Start Anleitung für alle Teammitglieder (Windows & macOS/Linux)
1. # Projekt klonen
bash
Kopieren
Bearbeiten
git clone <DEIN_REPOSITORY_URL>
cd <PROJEKT_ORDNER>

2. # Virtuelle Umgebung anlegen
Windows:

powershell
Kopieren
Bearbeiten
python -m venv env
macOS/Linux:

bash
Kopieren
Bearbeiten
python3 -m venv env
chmod +x start_app.sh

3. # Virtuelle Umgebung aktivieren
Windows (PowerShell):

powershell
Kopieren
Bearbeiten
.\env\Scripts\Activate.ps1
Falls Skripte blockiert sind, einmalig ausführen:

powershell
Kopieren
Bearbeiten
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
macOS/Linux:

bash
Kopieren
Bearbeiten
source env/bin/activate

4. # Abhängigkeiten installieren
bash
Kopieren
Bearbeiten
pip install -r requirements.txt

5. # API Schlüssel (.env) anlegen
Lege im Projektordner eine .env Datei an mit folgendem Inhalt:

ini
Kopieren
Bearbeiten
OPENAI_API_KEY=dein_openai_api_key
Wichtig: Diese Datei nicht ins Git-Repository hochladen!

6. # App starten
Windows:

Per Terminal mit aktivierter virtueller Umgebung:

powershell
Kopieren
Bearbeiten
streamlit run main.py
Oder Doppelklick auf start_app.bat (führt Aktivierung + Start automatisch aus)

macOS/Linux:

bash
Kopieren
Bearbeiten
./start_app.sh

7. # Entwicklung & Updates
Nach Pull oder Klonen die virtuelle Umgebung aktivieren (Schritt 3).

Falls requirements.txt aktualisiert wurde, mit

bash
Kopieren
Bearbeiten
pip install -r requirements.txt
die neuen Pakete installieren. 