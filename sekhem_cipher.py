import datetime

# --- اختبار الزمن الحقيقي لـ Sekhem-CC ---
current_time = "2026-04-07 10:50 PM" # الوقت الحالي بدقة
MY_KEY = "SK-TR-2026-X99"

# الرسالة التي نريد حمايتها الآن
my_message = "نظام Sekhem-CC يعمل بنجاح في الزمن الحقيقي"

# عملية التشفير
cipher = triad_encrypt(my_message, MY_KEY)

# طباعة النتيجة النهائية للتأكد
print(f"--- [REAL-TIME LOG: {current_time}] ---")
print(f"📡 الإدخال: {my_message}")
print(f"🔐 التشفير: {cipher}")
print(f"🔓 التحقق: {triad_decrypt(cipher, MY_KEY)}")

