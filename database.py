import sqlite3
from typing import List
from audio_converter import AudioFile

class Database:
    def __init__(self, db_path: str = "audio_conversions.db"):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversions (
                file_path TEXT,
                format TEXT,
                text TEXT
            )
        """)

    def save_conversion(self, audio_file: AudioFile):
        self.cursor.execute("""
            INSERT INTO conversions (file_path, format, text) VALUES (?, ?, ?)
        """, (audio_file.file_path, audio_file.format, audio_file.text))
        self.connection.commit()

    def get_previous_conversions(self) -> List[AudioFile]:
        self.cursor.execute("""
            SELECT * FROM conversions
        """)
        rows = self.cursor.fetchall()
        audio_files = [AudioFile(row[0], row[1], row[2]) for row in rows]
        return audio_files

    def close(self):
        self.connection.close()
