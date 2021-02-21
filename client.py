import requests

BASE = "http://localhost:8080/analyze"

payload = {"text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."}
response = requests.post(BASE, data=payload)


print(response.text)

