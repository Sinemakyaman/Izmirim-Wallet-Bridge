def calculate_esg_impact(amount, users_count=1):
    """
    Atıl paranın sisteme kazandırılmasının yarattığı 
    dolaylı çevresel ve ekonomik etki simülasyonu.
    """
    # Varsayımsal: Her 100 TL'lik dijitalleşme, plastik kart basımı ve 
    # fiziksel dolum makinelerinin enerji yükünü %0.1 azaltır.
    energy_saved = amount * 0.05 # kWh cinsinden
    plastic_waste_prevented = 0.005 # kg (kart ömrü üzerinden)
    
    return {
        "energy_saved_kwh": round(energy_saved, 2),
        "plastic_saved_kg": plastic_waste_prevented if amount > 0 else 0
    }