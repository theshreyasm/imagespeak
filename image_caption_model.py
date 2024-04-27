import torch
from transformers import AutoModelForCausalLM, AutoProcessor
import PIL

model = AutoModelForCausalLM.from_pretrained("microsoft/git-base")
model.load_state_dict(torch.load("3_ep_batch16.pth", map_location=torch.device('cpu')))

processor = AutoProcessor.from_pretrained("microsoft/git-base")

def generate_caption(image_path):
    image = PIL.Image.open(image_path)
    inputs = processor(images=image, return_tensors="pt")
    pixel_values = inputs.pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_caption
