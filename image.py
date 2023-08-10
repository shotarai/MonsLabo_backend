import io
import os
import warnings

from dotenv import load_dotenv
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


load_dotenv('.env')
STABILITY_API_KEY = os.getenv('STABILITY_API_KEY')

stability_api = client.StabilityInference(
    key=STABILITY_API_KEY,
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0", 
)

def generate_image(description):
    #
    res = stability_api.generate(
        prompt=description,
        seed=123463446,
        steps=50,
        cfg_scale=8.0,
        width=1024,
        height=1024,
        samples=1,
        sampler=generation.SAMPLER_K_DPMPP_2M
    )

    for resp in res:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                )
            if artifact.type == generation.ARTIFACT_IMAGE:
                byte_image = io.BytesIO(artifact.binary)

    return byte_image

"""
if __name__ == "__main__":
    generate_image("浴衣を着ている星の王子さま")
"""