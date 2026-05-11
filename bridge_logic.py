import datetime

class IzmirimBridge:
    def __init__(self):
        # Simüle edilmiş veri tabanı
        self.physical_cards = {
            "12345-67890": {"balance": 50.0, "status": "active"},
            "55555-44444": {"balance": 15.5, "status": "active"}
        }
        self.digital_wallets = {
            "user_sinem_1": {"balance": 60.0}
        }

    def get_card_info(self, card_id):
        return self.physical_cards.get(card_id, None)

    def transfer_to_digital(self, card_id, user_id):
        card = self.get_card_info(card_id)
        
        if not card:
            return {"status": "Error", "message": "Kart bulunamadı!"}
        
        amount = card["balance"]
        if amount <= 0:
            return {"status": "Error", "message": "Aktarılacak bakiye yok!"}

        # Transfer işlemi
        card["balance"] = 0
        card["status"] = "transferred"
        self.digital_wallets[user_id]["balance"] += amount

        return {
            "status": "Success",
            "amount": amount,
            "new_balance": self.digital_wallets[user_id]["balance"],
            "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        }