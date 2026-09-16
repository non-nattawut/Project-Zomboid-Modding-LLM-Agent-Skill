-- media/lua/shared/MyMod_Shared.lua

MyMod = MyMod or {}
MyMod.VERSION = "1.0.0"

function MyMod.CalculateDurabilityBonus(player, item)
    if not player or not item then return 1.0 end
    local maintenance = player:getPerkLevel(Perks.Maintenance) or 0
    return 1.0 + (maintenance * 0.05)
end
