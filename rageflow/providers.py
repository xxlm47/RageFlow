import requests
from .config import Config
class OfflineProvider:
    def generate(self,system,user): return user
class OpenAICompatibleProvider:
    def generate(self,system,user):
        if not all([Config.api_base,Config.api_key,Config.model]):
            raise RuntimeError("Set RAGEFLOW_API_BASE, RAGEFLOW_API_KEY and RAGEFLOW_MODEL")
        r=requests.post(Config.api_base+"/chat/completions",headers={"Authorization":f"Bearer {Config.api_key}","Content-Type":"application/json"},json={"model":Config.model,"messages":[{"role":"system","content":system},{"role":"user","content":user}],"temperature":0.8},timeout=90)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
def provider():
    return OpenAICompatibleProvider() if Config.provider!="offline" else OfflineProvider()
