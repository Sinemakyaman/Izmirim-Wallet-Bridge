from bridge_logic import IzmirimBridge

def main():
    bridge = IzmirimBridge()
    print("--- İzmirim Kart Dijital Köprü Sistemine Hoş Geldiniz ---")
    
    # Yöntem seçimi simülasyonu
    print("1- NFC ile Oku\n2- Kart ID ile Gir")
    choice = input("Seçiminiz: ")

    if choice == "1":
        card_id = "12345-67890" # NFC'den gelen simüle edilmiş ID
        print(f"NFC Okundu: {card_id}")
    else:
        card_id = input("Lütfen 11 haneli Kart ID giriniz: ")

    # Aktarım Başlat
    result = bridge.transfer_to_digital(card_id, "user_sinem_1")

    if result["status"] == "Success":
        print(f"\n✅ İşlem Başarılı!")
        print(f"Aktarılan Tutar: {result['amount']} TL")
        print(f"Yeni Dijital Bakiyeniz: {result['new_balance']} TL")
        print(f"İşlem Tarihi: {result['date']}")
    else:
        print(f"\n❌ Hata: {result['message']}")

if __name__ == "__main__":
    main()