import hashlib
import os
import json
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

waypoints = [
    { "name": "START GATE", "lat": 0.5142, "lng": 35.2697, "seed": "START GATE" },
    { "name": "WAYPOINT 1", "lat": 0.5212, "lng": 35.2601, "seed": "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT GOLF HOTEL INDIA JULIET KILO LIMA" },
    { "name": "WAYPOINT 2", "lat": 0.5115, "lng": 35.2814, "seed": "ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE" }
]

output = []
for wp in waypoints:
    seed = wp["seed"].upper().strip()
    seed = ' '.join(seed.split())
    seed_bytes = seed.encode('utf-8')
    
    h = hashlib.sha256()
    h.update(seed_bytes)
    key = h.digest()
    hash_hex = h.hexdigest()
    
    aesgcm = AESGCM(key)
    iv = os.urandom(12)
    payload = json.dumps({"lat": wp["lat"], "lng": wp["lng"]}, separators=(',', ':')).encode('utf-8')
    
    ciphertext = aesgcm.encrypt(iv, payload, None)
    
    iv_b64 = base64.b64encode(iv).decode('utf-8')
    data_b64 = base64.b64encode(ciphertext).decode('utf-8')
    
    output.append(f"""      {{
        name: "{wp['name']}",
        hash: "{hash_hex}",
        iv: "{iv_b64}",
        data: "{data_b64}"
      }}""")

print(",\n".join(output))
