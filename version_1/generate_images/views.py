from django.shortcuts import render
from django.http import HttpResponse
import replicate,openai,os

# Create your views here.

def generate_image_from_stable_diffusion(request):
    output = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={"prompt": "a vision of paradise. unreal engine"}
)
    return HttpResponse(output)

def generate_image_from_midjourney(request):
    output = replicate.run(
    "tstramer/midjourney-diffusion:436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b",
    input={"prompt": "a photo of an astronaut riding a horse on mars"}
)
    return HttpResponse(output)

def generate_image_from_DALLE(request):
    PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(openai.api_key)

    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
    )

    return HttpResponse(response["data"][0]["url"])