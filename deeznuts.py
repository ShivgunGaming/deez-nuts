import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import imageio
import pygame
from pygame import mixer
import tempfile

def show_deez_nuts_gif():
    # URL of the GIF
    gif_url = "https://media1.tenor.com/m/e9HQLoVOLCIAAAAd/hirxha-hahaha.gif"
    
    # Fetch the GIF from the URL
    response = requests.get(gif_url)
    gif_data = response.content
    
    # Create a temporary file to save the audio
    audio_file = "deez-nuts.mp3"
    # Initialize Pygame mixer
    pygame.init()
    mixer.init()
    
    # Load the audio file
    mixer.music.load(audio_file)
    
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Deez Nuts GIF with Audio")
    
    # Create a label for displaying the GIF frames
    label = tk.Label(root)
    label.pack()
    
    # Create an imageio reader for the GIF data
    gif_reader = imageio.get_reader(BytesIO(gif_data))
    
    # Function to update the GIF frames
    def update_frame():
        try:
            frame = gif_reader.get_next_data()
            frame_image = ImageTk.PhotoImage(Image.fromarray(frame))
            label.configure(image=frame_image)
            label.image = frame_image
            root.after(10, update_frame)  # Update frame every 10 milliseconds
        except EOFError:
            root.destroy()
    
    # Start updating the GIF frames
    update_frame()
    
    # Play the audio
    mixer.music.play()
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    show_deez_nuts_gif()
