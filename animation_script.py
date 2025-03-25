import base64
import json

animation_frames = [
    r"""
     .--.
    |o_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 \___)=(___/
    """,
    r"""
     .--.
    |o_o |
    |:_/ |
   //   \ \
  (|     | )
 /'\_   _/`\
 ___)=(___/
    """,
]

animation_json = json.dumps({
    "frames": animation_frames,
    "speed": 0.5 # speed
})
animation_base64 = base64.b64encode(animation_json.encode()).decode()

curl_command = f"""https://raw.githubusercontent.com/Isaki12/xanimate/main/animation_script.py | python3 - {animation_base64}"""

print(curl_command)
