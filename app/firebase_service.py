import firebase_admin
from typing import Dict
from uuid import uuid4

from firebase_admin import credentials
from firebase_admin import db

class FirebaseHandler:

    def __init__(self):
        self.cred_path = "app/serviceAccountKey.json"
        self.database_url = "https://gerentedeforms-b7987-default-rtdb.firebaseio.com/"
        self.credemtials = credentials.Certificate(self.cred_path)
        self.firebase_app = firebase_admin.initialize_app(self.credemtials, {
            'databaseURL': self.database_url
        })


    def insert_data(self, data: Dict):
        try:
            data_id = str(uuid4())
            db_table = db.reference(data_id)
            db_table.set(data)
            print(f"Dados com id {data_id} salvo com sucesso !")
            return data_id
        except Exception as erro:
            print(f"Erro ao salvador os dados com id {data_id} !")


# data = {"usename": "admin", "password": "admin", "location": "brasil"}
#
# firebase_handler = FirebaseHandler()
# firebase_handler.insert_data(data)
#
