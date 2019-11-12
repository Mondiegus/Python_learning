m = 1
km = 1000 *m
mile = 1608 *m
naut = 1852 * m

val = 1337 * m
val_km = val / km
val_miles = val / mile
val_naut = val / naut

print(f'Meters: {int(val)}')                              # int
print(f'Kilometers: {int(val_km)}')                          # int
print(f'Miles: {round(val_miles,3)}')                               # float
print(f'Nautical Miles: {round(val_naut,3)}')                      # float
print(f'm: {val}, km: {val_km}, mi: {val_miles}, nm: {val_naut}')  # int, int, float, float


# skafander

ata_hPa = 1013.25 # hPa
ata_Pa = ata_hPa/1_00
PSI = 6894.757 # Pa
EMU = 4.3 #PSI
ORLAN = 4_00 # hPa
pressure_gradient = -11.3 # Pa

EMU_kPa = (EMU * PSI)/1000
ORLAN_PSI = (ORLAN * 100)/PSI
partial = 20.946/100 *ata_Pa
the_last_one = (partial-ata_Pa) / pressure_gradient1


