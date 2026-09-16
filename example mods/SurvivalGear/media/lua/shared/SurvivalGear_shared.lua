-- media/lua/shared/SurvivalGear_shared.lua
SurvivalGear = SurvivalGear or {}
SurvivalGear.VERSION = "1.0.0"

function SurvivalGear.GetMacheteBonus(character)
    if not character then return 1.0 end
    local bladeSkill = character:getPerkLevel(Perks.LongBlade) or 0
    return 1.0 + (bladeSkill * 0.08)
end
