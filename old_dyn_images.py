import streamlit as st
import requests

UNSPLASH_ACCESS_KEY = 'axqzsCUgyumeqGjPAu2blRwRJCz3SJiFc6_xev8OZH0'  # Replace with your Unsplash access key

def fetch_image_url(title):
    # Search for images on Unsplash based on the title
    url = f"https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    params = {
        "query": title,
        "per_page": 1  # Number of images to retrieve
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            return data['results'][0]['urls']['regular']
    
    return None

def main():
    st.title("Search for Image by Title")
    user_input = st.text_input("Enter the title of the image:")

    resolution = st.slider("Select image resolution", 50, 1000, 300)  # Adjust resolution using a slider

    if user_input:
        image_url = fetch_image_url(user_input)
        if image_url:
            st.image(image_url, caption=user_input, use_column_width=True, output_format='JPEG', width=resolution)
        else:
            st.write("Image not found")


if __name__ == "__main__":
    main()
