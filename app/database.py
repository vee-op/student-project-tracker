import os
import motor.motor_asyncio
import hvac

# Connect to Vault
vault_client = hvac.Client(url='http://<vaultIP>:8200') #Ip will will be provided in the class or use localhost if you have a vault server on you host maching
vault_client.token = os.getenv("VAULT_TOKEN")

read_response = vault_client.secrets.kv.v2.read_secret_version(path="student01")
MONGO_URI = read_response['data']['data']['MONGO_URI']

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client["student_project_tracker"]
student_collection = database.get_collection("students")
