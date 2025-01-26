import os
import random
import requests
import numpy as np
from PIL import Image
from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip, ColorClip

# ========== CONFIGURATION ==========
API_KEY = "<your-api-key"
IMAGE_DIR = "./images"
SONG_DIR = "./sounds"
OUTPUT_DIR = "./video"

VIDEO_DURATION = 15
FONT_SIZE = 100
FONT_COLOR = "white"
FONT_STYLE = "Impact"
STROKE_COLOR = "black"
STROKE_WIDTH = 2
TEXT_VERTICAL_OFFSET = 0.6
BACKGROUND_COLOR = (0, 0, 0)  # Black background
FADE_DURATION = 2  # 2 seconds for fade in/out

# Gemini API configuration
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

# ========== GEMINI INTEGRATION ==========
def generate_text_from_prompt(prompt: str) -> str:
    """Generate text using direct Gemini API calls"""
    payload = {
        "contents": [{
            "parts": [{"text": f"Generate a short 10-15 word quote about: {prompt}"}]
        }]
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(GEMINI_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        # Parse response
        data = response.json()
        if 'candidates' in data and len(data['candidates']) > 0:
            return data['candidates'][0]['content']['parts'][0]['text'].strip()
        return None
        
    except requests.exceptions.HTTPError as e:
        print(f"Gemini API Error: {e.response.status_code}")
        print(e.response.text)
    except Exception as e:
        print(f"General Error: {str(e)}")
    
    return None

# ========== MEDIA HANDLING ========== 
def select_random_media():
    """Select random image and audio file"""
    images = [os.path.join(IMAGE_DIR, f) 
             for f in os.listdir(IMAGE_DIR) 
             if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    songs = [os.path.join(SONG_DIR, f) 
            for f in os.listdir(SONG_DIR) 
            if f.lower().endswith(('.mp3', '.wav'))]

    if not images:
        raise FileNotFoundError(f"No images found in {IMAGE_DIR}")
    if not songs:
        raise FileNotFoundError(f"No songs found in {SONG_DIR}")

    return random.choice(images), random.choice(songs)

# ========== VIDEO CREATION ==========
def create_video(image_path: str, song_path: str, text: str):
    """Create video with image, audio, and text"""
    # Load and process image
    img = Image.open(image_path).convert("RGB")
    img_width, img_height = img.size
    
    # Create background clip
    background = ColorClip(
        size=(img_width, img_height),
        color=BACKGROUND_COLOR,
        duration=VIDEO_DURATION
    ).set_opacity(1)
    
    # Create image clip with enhanced fade effects
    image_clip = (
        ImageClip(np.array(img))
        .set_duration(VIDEO_DURATION)
        .crossfadein(FADE_DURATION)
        .crossfadeout(FADE_DURATION)
        .set_position("center")
    )
    
    # Calculate text position
    text_y = int(img_height * TEXT_VERTICAL_OFFSET)
    
    # Create text clip with effects
    text_clip = (
        TextClip(
            text,
            fontsize=FONT_SIZE,
            color=FONT_COLOR,
            font=FONT_STYLE,
            size=(img_width * 0.8, None),
            stroke_color=STROKE_COLOR,
            stroke_width=STROKE_WIDTH,
            method="caption"
        )
        .set_position(("center", text_y))
        .set_duration(VIDEO_DURATION)
        .fadein(0.5)
        .fadeout(0.5)
    )
    
    # Combine elements with proper layering
    video = CompositeVideoClip([
        background,
        image_clip.set_start(0).crossfadein(FADE_DURATION),
        text_clip.set_start(FADE_DURATION/2)
    ])
    
    # Add audio
    audio = AudioFileClip(song_path).subclip(0, VIDEO_DURATION)
    video = video.set_audio(audio)
    
    # Render video
    output_path = os.path.join(OUTPUT_DIR, f"video_{random.randint(1000,9999)}.mp4")
    video.write_videofile(
        output_path,
        codec="libx264",
        fps=24,
        verbose=False,
        threads=4,
        preset='fast',
        ffmpeg_params=['-crf', '18']
    )
    return output_path

# ========== MAIN WORKFLOW ==========
if __name__ == "__main__":
    # Get user input
    prompt = input("Enter your video content prompt: ")
    
    # Generate text
    generated_text = generate_text_from_prompt(prompt)
    if not generated_text:
        print("Using fallback text")
        generated_text = "Stay motivated and keep pushing forward!"
    print(f"Generated Text: {generated_text}")
    
    # Select media
    try:
        image_path, song_path = select_random_media()
        print(f"Using Image: {image_path}\nUsing Audio: {song_path}")
    except Exception as e:
        print(e)
        exit()
    
    # Create video
    try:
        output_path = create_video(image_path, song_path, generated_text)
        print(f"Success! Video saved to: {output_path}")
    except Exception as e:
        print(f"Video creation failed: {e}")