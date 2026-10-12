import os
import shutil

def configurar_icono_android():
    """Copia el icono pre-generado a las carpetas de densidad y actualiza el manifiesto."""
    base_path = 'android/app/src/main/res'
    densidades = ['mipmap-hdpi', 'mipmap-mdpi', 'mipmap-xhdpi', 'mipmap-xxhdpi', 'mipmap-xxxhdpi']

    # Asegurar que existan las carpetas
    for carpeta in densidades:
        os.makedirs(f"{base_path}/{carpeta}", exist_ok=True)
        if os.path.exists('www/icon.png'):
            shutil.copy('www/icon.png', f"{base_path}/{carpeta}/icon.png")

    # Actualizar AndroidManifest.xml
    manifest_path = f"{base_path}/AndroidManifest.xml"
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            content = f.read()

        if 'android:icon' in content:
            content = content.replace('android:icon="@mipmap/ic_launcher"', 'android:icon="@mipmap/icon"')
        else:
            content = content.replace('<application', '<application android:icon="@mipmap/icon"')

        with open(manifest_path, 'w') as f:
            f.write(content)
        print("[OK] Icono configurado en AndroidManifest.xml")
    else:
        print("[Aviso] AndroidManifest.xml no encontrado. El icono se copiará pero no se configurará.")

def configurar_permisos():
    """Agrega los permisos de cámara al manifiesto."""
    manifest_path = 'android/app/src/main/AndroidManifest.xml'
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            content = f.read()

        permisos = '\n    <uses-permission android:name="android.permission.CAMERA" />\n    <uses-feature android:name="android.hardware.camera" />\n</manifest>'
        if "android.permission.CAMERA" not in content:
            content = content.replace('</manifest>', permisos)
            with open(manifest_path, 'w') as f:
                f.write(content)
        print("[OK] Permisos de cámara agregados.")
    else:
        print("[Aviso] No se pudieron configurar los permisos (AndroidManifest.xml no encontrado).")

if __name__ == "__main__":
    configurar_icono_android()
    configurar_permisos()
