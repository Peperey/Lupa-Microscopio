manifest = "android/app/src/main/AndroidManifest.xml"
try:
    with open(manifest, "r", encoding="utf-8") as f:
        content = f.read()

    permisos = '\n    <uses-permission android:name="android.permission.CAMERA" />\n    <uses-feature android:name="android.hardware.camera" />\n</manifest>'
    if "android.permission.CAMERA" not in content:
        content = content.replace("</manifest>", permisos)
        with open(manifest, "w", encoding="utf-8") as f:
            f.write(content)
    print("Permisos agregados correctamente.")
except Exception as e:
    print(f"Aviso: {e}")
