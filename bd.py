import random
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw
import io

# Function to generate a flower image
def generate_flower():
    size = (100, 100)
    image = Image.new("RGB", size, "#FFB6C1")  # Create a white image
    draw = ImageDraw.Draw(image)

    # Draw a simple flower shape with multiple petals
    draw.ellipse((30, 20, 70, 60), fill="#ff69b4")  # Pink center
    for angle in range(0, 360, 40):  # Draw petals around the center
        x = 50 + 20 * np.cos(np.radians(angle))
        y = 40 + 20 * np.sin(np.radians(angle))
        draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill="#ff69b4")  # Pink petals
    draw.ellipse((40, 30, 60, 50), fill="#ffff00")  # Yellow center

    # Save the image to a byte buffer
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr


# Function to generate a heart shape
def generate_heart(name, background_color="#FFB6C1"):
    t = np.linspace(0, 2*np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.add_patch(plt.Rectangle((-20, -20), 40, 40, color=background_color))
    ax.plot(x, y, color='red', linewidth=3)
    ax.set_facecolor("#FFB6C1")  # Set background color
    ax.axis('off')
    plt.text(0, 0, name, fontname='Lucida Handwriting', fontsize=12, color='black', ha='center')
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.tight_layout()

    return fig

def generate_birthday_wish(name):
    messages = [
        f"Happy birthday, Mummy {name}! I hope your special day is filled with love and happiness 😊",

        f"Wishing you a wonderful birthday Noni! May all your dreams come true.",

        f"Happy birthday to the best {name} in the world! Enjoy your day to the fullest.",

        f"Sending you my warmest wishes on your birthday, {name}! May this year be full of amazing opportunities and experiences. 🤩",

        f"On your special day and every single day, Vanvouna, I wish you health, happiness, and success. Happy birthday! 🥳",

        f"كل سنة وحضرتك طيبة يا أمي! قلبي يحبك جدا جدا",

        f" Your love is the light that brightens my darkest days. I cherish every moment with you and I am grateful for you. Happiest of birthdays Nino! 😁", 

        f'''Today, I make a promise to you - a vow to make you proud, to care for you as you have cared for me, and to strive to give back even a fraction 
        of the love and support you've showered upon me. Your sacrifices and endless devotion will always be my guiding light. I pledge to cherish you, 
        to honor your teachings, and to walk in the path you've illuminated for me. With every breath, I will endeavor to repay the immeasurable debt of 
        love you've showered me with throughout my entire life. I love you so so much habibty, and I will make you proud. 😍''', 

        f'''As I stand before you today, I vow to be the daughter you've raised me to be—filled with strength, compassion, and determination. I promise to always carry your love 
        in my heart, to honor your sacrifices with my actions, and to make you proud in every step I take. I love you to the moon and beyond, and I will strive to reflect back to you
        the love and guidance you've always shown me. 😘''', 

        f'''My goal is to repay your boundless love with every beat of my heart. Your wisdom will be my compass, your love my guiding star. 
        I cherish you beyond words, and I will strive to be the daughter you've always dreamed of and raised me to be. 🌟''', 

        f'''I promise to show you the depths of my capabilities, to rise and shine in a way that reflects the love and strength you've instilled in me. I will never allow those who wish 
        ill upon me and doubted me the satisfaction of telling you "I told you so." Your faith in me fuels my determination, and I will strive to exceed all your expectations for me, 
        both personal and professional, and to honor your sacrifices, with your love as my guiding force. 🥰''', 

        f'''You have no idea how incredibly happy I am when I see you laughing or smiling. I will always strive to see that sweet smile of yours light up your face and I swear that 
        any achievement I've ever done in my life is remembered with your face of joy and pleasure. I always try to make you laugh even by being silly sometimes, just 
        because I count your laugh as a personal victory and a feeling of satisfaction washes all over me. I love you Vanvouny and always wish to see you smile and laugh! 😄'''
    ]

    wishes = [
        f'''To the most amazing woman in my life, my mother. Your love is a treasure that I cherish every day. Your warmth and tenderness have been a source of comfort 
        and motivation. On your special day, I want to thank you for being not just a mother but a friend, a confidante, and a role model. Here's to celebrating you
        and the exquisite person you are. Happy birthday, Mom! 🎊''',

        f'''Dearest Mom, I want to remind you of the incredible impact you have just by being present in a room. Your strength, kindness, and wisdom have been 
        a guiding light in my life. Today, I wish for you all the beauty and joy in the world. May this birthday be the beginning of a year filled with blessings 
        and unforgettable moments. Happy birthday, Mom! 🎁''', 

        f'''Happy birthday to the queen of my heart, Vanvouny. Your grace, resilience, and unconditional love have no bounds. Today, I wish for you all the happiness in the world, 
        all the peace in your heart, and all the love that you have bestowed upon me to be returned to you a hundredfold. May your life be as bright and beautiful as your spirit. 
        Thank you for being you. I love you more than you can ever imagine. 💖''',

        f"عزيزتي أمي، أريدك أن تعلمي أنني أحبك بشكل لا يمكن وصفه بالكلمات وأقدر كل تضحية قدمتيها من أجلي. حبك هو الضوء الذي يهديني خلال رحلة الحياة. أنا أقدرك أكثر مما تتصورين", 

        f'''May the universe conspire to bring you all the joy, peace, and prosperity that you so richly deserve. Here's to a year filled with laughter, love, and 
        endless possibilities. You are not just my mother but my hero, my rock, and my inspiration. 
        Wishing you all the best today and always. I love you beyond measure. Happy Birthday Mummy Vanvouna! 🎈''',

        f'''I want you to know that if there were moments I caused you sadness, it was never intentional and I deeply regret every moment. Every second of anger or frustration 
        you endure pains me since your happiness means everything to me. My occasional stubbornness doesn't diminish the love and appreciation I hold for you, nor will it 
        ever lead me to neglect or be selfish towards you. Your joy is my joy, and your comfort my priority. Always be sure of this. I love you forever and 
        hope that I can make all your wishes come true and that our future together is so bright, full of joy and health with us being side by side. 
        Together forever Vanvouny - happy birthday! 🎀'''
    ]

    things_done = [
        f"Dear Mummy {name}, on your birthday, I want to express my deepest gratitude for all the amazing things you've done for me. Your kindness and support mean the world to me.",
        f"Happy birthday, {name}! Thank you for always being there for me and going above and beyond to make me feel loved and cared for.😌",

        f"Mummy Vanvouny, your birthday is a perfect occasion to let you know how much I appreciate everything you've done for me. You're truly an incredible person. 😻",

        f'''Mom, on this special day and everyday, I want you to be sure that I appreciate all the love, care, and sacrifices you've made for me. 
        Your unwavering support and endless affection have shaped me into the person I am today. May your days always be filled with joy, laughter, and all 
        the happiness you truly deserve. I love you more than words can say 💜''',

        f'''I want to take a moment to thank you, Vanvouny, for being the rock of this family of two, for your endless patience, and for your unwavering love. 
        Your presence in my life is a gift beyond measure that I do not take for granted and truly count as a blessing. May your birthday be a reflection of the joy and love 
        you bring to everyone around you. Here's to another year of laughter, memories, and cherished moments. Happy birthday Mummy! ❤️''', 

        f"حضرتك رمز السمو والحب. وجودك يضيء حياتي بطرق لا تستطيع الكلمات التعبير عنها وأريد أن أشكرك على كل ما تقومين به. عيد ميلاد سعيد لأجمل روح في الدنيا",

        f'''I believe it's impossible to count the number of sacrifices, blessings, and things you have done for me throughout my entire life. I believe it's more stones than those 
        used to build the Pyramids, taller than the Eiffel Tower, longer than the Great Wall of China; for these are all stationary objects regarded as the Wonders of the World. 
        But to me you are the most special, greatest, and most important wonder of my life. What did I ever do to deserve you? I have no idea but I genuinely love you and
        cannot live without you in my life. Nothing can ever change that - this is a constant. Static. Permanent. I don't want you to ever regret your choice to keep me and
        bring me to this world and I assure you that I will do everything in my willpower to make you feel comfortable and happy and healthy. Happy birthday, Mummy Vanvouna! 🙌'''
    
    ]

    categories = {
        "Messages": messages,
        "Wishes": wishes,
        "Thank You": things_done
    }

    if "selected" not in st.session_state:
        st.session_state.selected = {key: [] for key in categories}

    selected_category = st.selectbox("Select a category:", list(categories.keys()))

    # Check if all messages in the category have been shown
    if len(st.session_state.selected[selected_category]) == len(categories[selected_category]):
        st.write("You have viewed all messages in this category.")
        return

    # Shuffle the messages if they haven't all been shown yet
    if not st.session_state.selected[selected_category]:
        st.session_state.selected[selected_category] = categories[selected_category][:]
        random.shuffle(st.session_state.selected[selected_category])

    # Pop and return the next message
    return st.session_state.selected[selected_category].pop()


# Streamlit app
def main():
    st.markdown(
        """
    <style>
    .reportview-container .markdown-text-container {
        font-family: monospace;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #FFB6C1; /* Light Pink background */
    }

    [data-testid="stVerticalBlockBorderWrapper"]{
        background-color: #FFB6C1;}

    [class="st-emotion-cache-1kyxreq e115fcil2"]{
        background-color: #FFB6C1;}
   
    .st-bb {
        background-color: transparent;
    }
    .st-at {
        background-color: #FFB6C1;
    }
    footer {
        font-family: monospace;
    }
    .reportview-container .main footer, .reportview-container .main footer a {
        color: #0c0080;
    }
    header .decoration {
        background-image: none;
    }

    [class="st-emotion-cache-10trblm e1nzilvr1"]{
    text-align: center; font-family: "Lucida Handwriting"; font-size:38px;
    }

    [class="st-emotion-cache-1jmvea6 e1nzilvr5"]{
    font-family: "Roboto"; font-size:38px; color: #fff; border = 2px solid #000 radius: 100px;
    }

    [data-testid="stMarkdownContainer"]{
    font-family: "Lucida Handwriting"; font-size:28px; color: #000; 

    }

    </style>
    """,
        unsafe_allow_html=True,
    )
    
    # backgroundColor = "#F0F0F0"

    st.title("Happy Birthday Mummy Nervana! 🤍🥰🎉")
    st.markdown("<title style='text-align: center;", unsafe_allow_html=True)


    # Generate and display heart shape with name inside
    name = "Nervana"  # Hardcoded name for demonstration
    heart_fig = generate_heart("Nervana", background_color='#FFB6C1')
    st.pyplot(heart_fig)

     # Generate and display flower image
    flower_img = generate_flower()
    st.image(flower_img, use_column_width=True)

    # Input name
    birthday_wish = generate_birthday_wish("Nervana")
    st.write(birthday_wish)

if __name__ == "__main__":
    main()