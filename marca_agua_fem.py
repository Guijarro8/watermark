import streamlit as st
from PIL import Image
from io import BytesIO
import base64

# Función para agregar la marca de agua
def agregar_marca_de_agua(original_image, watermark_image):
    # Redimensionar la marca de agua al 20% del tamaño original (ajusta según sea necesario)
    resized_watermark = watermark_image.resize((int(watermark_image.width * 0.2), int(watermark_image.height * 0.2)))

    # Superponer la marca de agua en la esquina inferior derecha
    original_image.paste(resized_watermark, (original_image.width - resized_watermark.width, original_image.height - resized_watermark.height), resized_watermark)
    return original_image

def main():
    st.title("Agregador de Marca de Agua")

    # Subir la imagen original
    uploaded_file = st.file_uploader("Subir imagen original", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        original_image = Image.open(uploaded_file)

        # Subir la marca de agua
        watermark_file = st.file_uploader("Subir marca de agua", type=["png"])
        if watermark_file is not None:
            watermark_image = Image.open(watermark_file).convert("RGBA")

            # Agregar la marca de agua
            watermarked_image = agregar_marca_de_agua(original_image.copy(), watermark_image)

            # Mostrar la imagen con la marca de agua
            img_data = BytesIO()
            watermarked_image.save(img_data, format="PNG")
            img_data.seek(0)

            # Crear el enlace de descarga
            encoded_img = base64.b64encode(img_data.getvalue()).decode()
            href = f'<a href="data:file/png;base64,{encoded_img}" download="watermarked_image.png">Descargar Imagen con Marca de Agua</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
