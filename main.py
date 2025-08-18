from datetime import datetime
import platform

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    system_info = platform.platform()
    print("✅ Script ejecutado correctamente desde GitHub Actions")
    print(f"🕒 Fecha y hora actual: {now}")
    print(f"💻 Sistema detectado: {system_info}")

if __name__ == "__main__":
    main()
