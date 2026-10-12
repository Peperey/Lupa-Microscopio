import os
import shutil
from PIL import Image, ImageDraw

def generar_icono():
    """Genera un icono de lupa profesional de 512x512 píxeles."""
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Fondo circular verde
    draw.ellipse([40, 40, 472, 472], fill=(0, 255, 136, 255), outline=(255, 255, 255, 255), width=8)

    # Lupa blanca
    draw.ellipse([120, 120, 392, 392], outline=(255, 255, 255, 255), width=24)
    draw.line([340, 340, 430, 430], fill=(255, 255, 255, 255), width=28, joint='curve')

    img.save('www/icon.png')
    print("[OK] Icono de Lupa generado.")

def configurar_icono_android():
    """Copia el icono a las carpetas de densidad y actualiza el manifiesto."""
    base_path = 'android/app/src/main/res'
    densidades = {
        'mipmap-hdpi': 240,
        'mipmap-mdpi': 120,
        'mipmap-xhdpi': 320,
        'mipmap-xxhdpi': 480,
        'mipmap-xxxhdpi': 512
    }

    for carpeta, size in densidades.items():
        os.makedirs(f"{base_path}/{carpeta}", exist_ok=True)
        shutil.copy('www/icon.png', f"{base_path}/{carpeta}/icon.png")

    # Actualizar AndroidManifest.xml
    manifest_path = f"{base_path}/AndroidManifest.xml"
    with open(manifest_path, 'r') as f:
        content = f.read()

    if 'android:icon' in content:
        content = content.replace('android:icon="@mipmap/ic_launcher"', 'android:icon="@mipmap/icon"')
    else:
        content = content.replace('<application', '<application android:icon="@mipmap/icon"')

    with open(manifest_path, 'w') as f:
        f.write(content)
    print("[OK] Icono configurado en AndroidManifest.xml")

def configurar_permisos():
    """Agrega los permisos de cámara al manifiesto."""
    manifest_path = 'android/app/src/main/AndroidManifest.xml'
    with open(manifest_path, 'r') as f:
        content = f.read()

    permisos = '\n    <uses-permission android:name="android.permission.CAMERA" />\n    <uses-feature android:name="android.hardware.camera" />\n</manifest>'
    if "android.permission.CAMERA" not in content:
        content = content.replace('</manifest>', permisos)
        with open(manifest_path, 'w') as f:
            f.write(content)
    print("[OK] Permisos de cámara agregados.")

if __name__ == "__main__":
    if not os.path.exists('www/icon.png'):
        generar_icono()
    configurar_icono_android()
    configurar_permisos()
