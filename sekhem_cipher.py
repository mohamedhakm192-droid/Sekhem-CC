# SEKHEM-CC: Interactive Command Center
import base64
import datetime

# --- المحرك الرئيسي ---
def triad_encrypt(text, key):
    combined = f"{text}::{key}"
    return base64.b64encode(combined.encode("utf-8")).decode("utf-8")

def triad_decrypt(cipher, key):
    try:
        decoded = base64.b64decode(cipher).decode("utf-8")
        if key in decoded:
            return decoded.replace(f"::{key}", "")
        return "❌ الوصول مرفوض: مفتاح خاطئ!"
    except:
        return "⚠️ خطأ في بنية الشفرة!"

# --- واجهة التفاعل في الزمن الحقيقي ---
def run_sekhem_console():
    MY_KEY = "SK-TR-2026-X99"
    ADMIN = "M_ABD_EL_NABY"
    
    print("="*40)
    print(f"🛡️  SEKHEM-CC SYSTEM | ADMIN: {ADMIN}")
    print(f"⏰ TIME: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*40)
    
    while True:
        print("\n[1] تشفير رسالة جديدة")
        print("[2] فك تشفير رسالة")
        print("[3] الخروج من المنظومة")
        
        choice = input("\n👤 اختر رقم المهمة: ")
        
        if choice == "1":
            msg = input("📝 أدخل النص المراد حمايته: ")
            result = triad_encrypt(msg, MY_KEY)
            print(f"🔐 الشفرة الناتجة: {result}")
            
        elif choice == "2":
            code = input("🔐 أدخل الشفرة لفكها: ")
            result = triad_decrypt(code, MY_KEY)
            print(f"🔓 النتيجة: {result}")
            
        elif choice == "3":
            print("👋 تم تسجيل الخروج. نظام Sekhem-CC في وضع الاستعداد.")
            break
        else:
            print("⚠️ اختيار غير صحيح!")

# تفعيل المنظومة
if __name__ == "__main__":
    run_sekhem_console()
